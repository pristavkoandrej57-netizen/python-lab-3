
import argparse
import os
import sys

import numpy as np
import pandas as pd


class InvalidConfigError(Exception):
    """Неверные параметры запуска (годы, магазины, имя файла)."""


class OutputWriteError(Exception):
    """Не удалось записать результат в файл."""



START_DATE = "2022-01-01"  
PRICE_GROWTH = 0.06      
PAYMENT_METHODS = ["наличные", "карта", "онлайн"]
PAYMENT_PROBS = [0.3, 0.5, 0.2]


ALL_STORES = [
    ("S01", "Москва"), ("S02", "Санкт-Петербург"), ("S03", "Казань"),
    ("S04", "Новосибирск"), ("S05", "Екатеринбург"), ("S06", "Самара"),
    ("S07", "Нижний Новгород"), ("S08", "Краснодар"), ("S09", "Воронеж"),
    ("S10", "Пермь"),
]


PRODUCTS = [
    ("Напитки", "Лимонад", 90, 0.55, 30, 0.20, 0.45, 200),    
    ("Напитки", "Чай", 150, 0.50, 25, -0.10, 0.30, 15),     
    ("Напитки", "Кофе", 300, 0.60, 20, 0.25, 0.10, 15),
    ("Продукты", "Хлеб", 45, 0.70, 60, -0.05, 0.05, 100),
    ("Продукты", "Молоко", 80, 0.75, 50, 0.02, 0.05, 100),
    ("Продукты", "Сыр", 450, 0.65, 15, 0.15, 0.15, 350),     
    ("Бытовое", "Мыло", 60, 0.50, 22, 0.00, 0.05, 100),
    ("Бытовое", "Шампунь", 250, 0.55, 18, -0.20, 0.08, 100),
    ("Бытовое", "Зубная паста", 120, 0.50, 25, 0.12, 0.05, 100),
]


def check_args(years, stores, out):
    """Проверяет параметры командной строки.

    Если что-то неверно, вызывает InvalidConfigError с понятным текстом.
    """
    if years < 1 or years > 10:
        raise InvalidConfigError(f"--years должно быть от 1 до 10, получено {years}")
    if stores < 5 or stores > len(ALL_STORES):
        raise InvalidConfigError(f"--stores должно быть от 5 до {len(ALL_STORES)}, получено {stores}")
    if out is None or out.strip() == "":
        raise InvalidConfigError("--out не должно быть пустым")
    if not out.lower().endswith(".csv"):
        raise InvalidConfigError("--out должно оканчиваться на .csv")


def generate_sales(years, n_stores, rng):
    """Создаёт таблицу продаж без выбросов и пропусков.

    years    - сколько лет данных;
    n_stores - сколько магазинов;
    rng      - генератор случайных чисел numpy (задаёт воспроизводимость).
    Возвращает pandas.DataFrame: одна строка = товар, магазин, день.
    """
    n_days = years * 365
    n_prod = len(PRODUCTS)
    shape = (n_days, n_stores, n_prod)

    dates = pd.date_range(START_DATE, periods=n_days)


    base_price = np.array([p[2] for p in PRODUCTS])[None, None, :]
    cost_share = np.array([p[3] for p in PRODUCTS])[None, None, :]
    base_qty = np.array([p[4] for p in PRODUCTS])[None, None, :]
    trend = np.array([p[5] for p in PRODUCTS])[None, None, :]
    season_amp = np.array([p[6] for p in PRODUCTS])[None, None, :]
    season_peak = np.array([p[7] for p in PRODUCTS])[None, None, :]


    t = (np.arange(n_days) / 365)[:, None, None]


    trend_factor = np.maximum(1 + trend * t, 0.1)

    day_of_year = dates.dayofyear.values[:, None, None]
    season_factor = 1 + season_amp * np.cos(2 * np.pi * (day_of_year - season_peak) / 365)

    week_factor = np.where(dates.dayofweek.values >= 5, 1.3, 1.0)[:, None, None]

    store_factor = rng.uniform(0.7, 1.3, size=n_stores)[None, :, None]

    starts = rng.random(shape) < 0.02
    promo = starts.copy()
    for shift in range(1, 5):
        promo[shift:] = promo[shift:] | starts[:-shift]

    promo_qty = np.where(promo, 1.4, 1.0)        
    noise = rng.normal(1, 0.15, size=shape)
    qty_mean = base_qty * store_factor * trend_factor * season_factor * week_factor * promo_qty
    qty = np.round(qty_mean * noise).clip(min=0).astype(int)

    price_trend = 1 + PRICE_GROWTH * t
    promo_price = np.where(promo, 0.85, 1.0)
    price = np.round(base_price * price_trend * promo_price * rng.normal(1, 0.02, size=shape), 2)

    cost = np.round(base_price * cost_share * price_trend * np.ones(shape), 2)

    d_idx, s_idx, p_idx = np.indices(shape)
    d_idx = d_idx.ravel()
    s_idx = s_idx.ravel()
    p_idx = p_idx.ravel()

    stores = ALL_STORES[:n_stores]
    n_rows = d_idx.size

    df = pd.DataFrame({
        "date": np.array(dates.strftime("%Y-%m-%d"))[d_idx],
        "store_id": np.array([s[0] for s in stores])[s_idx],
        "city": np.array([s[1] for s in stores])[s_idx],
        "category": np.array([p[0] for p in PRODUCTS])[p_idx],
        "product": np.array([p[1] for p in PRODUCTS])[p_idx],
        "qty": qty.ravel(),
        "price": price.ravel(),
        "cost": cost.ravel(),
        "promo": promo.ravel().astype(int),
        "payment_method": rng.choice(PAYMENT_METHODS, size=n_rows, p=PAYMENT_PROBS),
    })
    return df


def add_outliers(df, rng, share=0.012):
    """Делает выбросы: у share (1.2%) строк количество увеличивается в 5-10 раз."""
    mask = rng.random(len(df)) < share
    df.loc[mask, "qty"] = df.loc[mask, "qty"] * rng.integers(5, 11, size=mask.sum())
    return df


def add_missing(df, rng, share=0.007):
    """Делает пропуски: в share (0.7%) строк нет цены и в share строк нет способа оплаты."""
    mask_price = rng.random(len(df)) < share
    mask_pay = rng.random(len(df)) < share
    df.loc[mask_price, "price"] = np.nan
    df.loc[mask_pay, "payment_method"] = np.nan
    return df


def save_csv(df, out):
    """Сохраняет таблицу в CSV. При ошибке записи вызывает OutputWriteError."""
    try:
        folder = os.path.dirname(out)
        if folder != "":
            os.makedirs(folder, exist_ok=True)
        df.to_csv(out, index=False)
    except OSError as error:
        raise OutputWriteError(f"Не удалось записать файл '{out}': {error}")


def parse_args():
    """Читает параметры командной строки."""
    parser = argparse.ArgumentParser(description="Генератор синтетических данных о продажах")
    parser.add_argument("--seed", type=int, default=42, help="seed генератора (по умолчанию 42)")
    parser.add_argument("--years", type=int, default=3, help="сколько лет данных (1-10)")
    parser.add_argument("--stores", type=int, default=6, help="количество магазинов (5-10)")
    parser.add_argument("--out", type=str, default="data/sales.csv", help="путь к выходному CSV")
    return parser.parse_args()


def main():
    """Точка входа. Возвращает 0 при успехе и число больше 0 при ошибке."""
    args = parse_args()
    try:
        check_args(args.years, args.stores, args.out)
        rng = np.random.default_rng(args.seed)
        df = generate_sales(args.years, args.stores, rng)
        df = add_outliers(df, rng)
        df = add_missing(df, rng)
        save_csv(df, args.out)
    except InvalidConfigError as error:
        print(f"Ошибка параметров: {error}", file=sys.stderr)
        return 1
    except OutputWriteError as error:
        print(f"Ошибка записи: {error}", file=sys.stderr)
        return 2

    print(f"Готово: {len(df)} строк записано в {args.out}")
    print("Пропусков в price:", df["price"].isna().sum())
    print("Пропусков в payment_method:", df["payment_method"].isna().sum())
    return 0


if __name__ == "__main__":
    sys.exit(main())