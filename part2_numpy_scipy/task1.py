
import numpy as np


expenses = np.array([3200, 3100, 2600, 1900, 1500, 1300, 1250, 1400, 1800, 2300, 2900, 3500])


winter = expenses[[11, 0, 1]].sum()
summer = expenses[[5, 6, 7]].sum()

print("Расходы:", *expenses)
print(f"Зима: {winter}, лето: {summer}", end=" -> ")

if winter > summer:
    print("больше тратится зимой")
elif summer > winter:
    print("больше тратится летом")
else:
    print("расходы зимой и летом одинаковые")


max_value = expenses.max()
months = np.where(expenses == max_value)[0] + 1  

print(f"Максимум ({max_value}) в месяцах:", *months)