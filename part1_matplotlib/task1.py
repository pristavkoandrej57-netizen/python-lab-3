
import numpy as np
import matplotlib.pyplot as plt


x_deg = np.linspace(-360, 360, 2000)

# 2. Переводим градусы в радианы, потому что sin и cos работают с радианами
x = np.deg2rad(x_deg)


# p(x) = e^(sin x) + ln(sin^2(0.5x) + 1) * cos x
p = np.exp(np.sin(x)) + np.log(np.sin(0.5 * x) ** 2 + 1) * np.cos(x)

# q(x) = -ln((sin x - cos x)^2 + 2) + 8
q = -np.log((np.sin(x) - np.cos(x)) ** 2 + 2) + 8


fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(10, 7))


ax1.plot(x_deg, p, color="blue", label="p(x)")
ax1.set_title("График функции p(x) = e^sin(x) + ln(sin²(0.5x) + 1) · cos(x)")
ax1.set_ylabel("p(x)")
ax1.grid(True)
ax1.legend()

ax2.plot(x_deg, q, color="red", label="q(x)")
ax2.set_title("График функции q(x) = -ln((sin(x) - cos(x))² + 2) + 8")
ax2.set_xlabel("x, градусы")
ax2.set_ylabel("q(x)")
ax2.grid(True)
ax2.legend()
ax2.set_xticks(np.arange(-360, 361, 90))
ax2.set_xlim(-360, 360)


plt.tight_layout()


plt.savefig("img/task1.png", dpi=150)
plt.show()