
import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-8, 8, 2000)


y = 4 / (x ** 2 - 4)



y_masked = np.ma.masked_where(np.abs(x ** 2 - 4) < 0.1, y)


plt.figure(figsize=(9, 6))
plt.plot(x, y_masked, color="blue", label="y = 4 / (x² - 4)")


plt.axvline(x=-2, color="gray", linestyle="--", label="асимптоты x = ±2")
plt.axvline(x=2, color="gray", linestyle="--")


plt.axhline(0, color="black", linewidth=0.8)


plt.xlim(-8, 8)
plt.ylim(-10, 10)


plt.title("График функции y = 4 / (x² - 4)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()


plt.savefig("img/task2.png", dpi=150)
plt.show()