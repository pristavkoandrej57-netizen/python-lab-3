
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad, dblquad

value1, err1 = quad(lambda x: x * np.sin(x), 0, np.pi)
exact1 = np.pi

print("Интеграл 1: x*sin(x) от 0 до pi")
print("  quad      =", value1)
print("  точное    =", exact1)
print("  погрешность =", abs(value1 - exact1))


value2, err2 = dblquad(lambda y, x: x + y, 0, 1, lambda x: 0, lambda x: x)
exact2 = 0.5

print("\nИнтеграл 2: (x + y) по области 0 <= y <= x <= 1")
print("  dblquad   =", value2)
print("  точное    =", exact2)
print("  погрешность =", abs(value2 - exact2))


rng = np.random.default_rng(42)   

N_values = [10 ** 3, 10 ** 4, 10 ** 5, 10 ** 6]
errors = []

print("\nМонте-Карло:")
for N in N_values:
    x = rng.random(N)
    y = rng.random(N)
    f = np.where(y <= x, x + y, 0)
    estimate = f.mean()
    error = abs(estimate - exact2)
    errors.append(error)
    print(f"  N = {N:>8}: оценка = {estimate:.6f}, погрешность = {error:.6f}")

plt.figure(figsize=(8, 6))
plt.loglog(N_values, errors, "o-", color="blue", label="погрешность Монте-Карло")


reference = 1 / np.sqrt(np.array(N_values))
plt.loglog(N_values, reference, "--", color="gray", label="1/√N (для сравнения)")

plt.title("Погрешность метода Монте-Карло")
plt.xlabel("Число точек N")
plt.ylabel("Абсолютная погрешность")
plt.grid(True, which="both")
plt.legend()

plt.savefig("task4_montecarlo.png", dpi=150)
plt.show()