import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

m = 1.0
k = 10.0

c_critical = 2 * np.sqrt(m * k)

cases = {
    "Underdamped": 2.0,
    "Critically damped": c_critical,
    "Overdamped": 10.0
}

x0 = 1.0
v0 = 0.0

t = np.linspace(0, 10, 1000)

plt.figure(figsize=(10, 6))

for label, c in cases.items():
    def system(time, y):
        x = y[0]
        v = y[1]

        dxdt = v
        dvdt = -(c / m) * v - (k / m) * x

        return [dxdt, dvdt]

    sol = solve_ivp(system, [0, 10], [x0, v0], t_eval=t)
    plt.plot(sol.t, sol.y[0], label=f"{label} (c={c:.2f})")

plt.title("Mass-Spring-Damper Damping Cases")
plt.xlabel("Time")
plt.ylabel("Position")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("results/damping_cases.png", dpi=300)
plt.show()
