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

# Part 1: Free response
plt.figure(figsize=(10, 6))

underdamped_solution = None

for label, c in cases.items():
    def free_system(time, y):
        x = y[0]
        v = y[1]

        dxdt = v
        dvdt = -(c / m) * v - (k / m) * x

        return [dxdt, dvdt]

    sol = solve_ivp(free_system, [0, 10], [x0, v0], t_eval=t)
    plt.plot(sol.t, sol.y[0], label=f"{label} (c={c:.2f})")

    if label == "Underdamped":
        underdamped_solution = sol

plt.title("Free Response of Mass-Spring-Damper System")
plt.xlabel("Time")
plt.ylabel("Position")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("results/damping_cases.png", dpi=300)
plt.show()

# Part 2: Forced response
c = 2.0

def force_input(time):
    return np.sin(2 * time)

def forced_system(time, y):
    x = y[0]
    v = y[1]

    dxdt = v
    dvdt = (force_input(time) - c * v - k * x) / m

    return [dxdt, dvdt]

sol_forced = solve_ivp(forced_system, [0, 10], [0.0, 0.0], t_eval=t)

plt.figure(figsize=(10, 6))
plt.plot(sol_forced.t, sol_forced.y[0], label="Forced response")
plt.plot(t, force_input(t), "--", label="Input force")

plt.title("Forced Response of Mass-Spring-Damper System")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("results/forced_response.png", dpi=300)
plt.show()

# Part 3: Effect of mass
mass_values = [0.5, 1.0, 2.0]
c = 2.0
k = 10.0

plt.figure(figsize=(10, 6))

for m_value in mass_values:
    def mass_system(time, y):
        x = y[0]
        v = y[1]

        dxdt = v
        dvdt = -(c / m_value) * v - (k / m_value) * x

        return [dxdt, dvdt]

    sol_mass = solve_ivp(mass_system, [0, 10], [x0, v0], t_eval=t)
    plt.plot(sol_mass.t, sol_mass.y[0], label=f"m = {m_value}")

plt.title("Effect of Mass on Free Response")
plt.xlabel("Time")
plt.ylabel("Position")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("results/mass_effect.png", dpi=300)
plt.show()

# Part 4: Effect of spring constant
spring_values = [5.0, 10.0, 20.0]
m = 1.0
c = 2.0

plt.figure(figsize=(10, 6))

for k_value in spring_values:
    def spring_system(time, y):
        x = y[0]
        v = y[1]

        dxdt = v
        dvdt = -(c / m) * v - (k_value / m) * x

        return [dxdt, dvdt]

    sol_spring = solve_ivp(spring_system, [0, 10], [x0, v0], t_eval=t)
    plt.plot(sol_spring.t, sol_spring.y[0], label=f"k = {k_value}")

plt.title("Effect of Spring Constant on Free Response")
plt.xlabel("Time")
plt.ylabel("Position")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("results/spring_effect.png", dpi=300)
plt.show()

# Part 5: Velocity response
plt.figure(figsize=(10, 6))
plt.plot(sol_forced.t, sol_forced.y[1], label="Velocity response")

plt.title("Velocity Response of Mass-Spring-Damper System")
plt.xlabel("Time")
plt.ylabel("Velocity")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("results/velocity_response.png", dpi=300)
plt.show()

# Part 6: Overshoot and settling time for underdamped case
x_under = underdamped_solution.y[0]
t_under = underdamped_solution.t

peak_displacement = np.max(np.abs(x_under))

tolerance = 0.02 * abs(x0)

settling_time = None
for i in range(len(x_under)):
    if np.all(np.abs(x_under[i:]) <= tolerance):
        settling_time = t_under[i]
        break

print("Underdamped case metrics")
print(f"Peak displacement: {peak_displacement:.4f}")
print(f"Settling time (2% band): {settling_time:.4f} s")

plt.figure(figsize=(10, 6))
plt.plot(t_under, x_under, label="Underdamped response")
plt.axhline(tolerance, color="red", linestyle="--", label="2% band")
plt.axhline(-tolerance, color="red", linestyle="--")

if settling_time is not None:
    plt.axvline(settling_time, color="green", linestyle="--", label=f"Settling time = {settling_time:.2f}s")

plt.title("Underdamped Response with Settling Time")
plt.xlabel("Time")
plt.ylabel("Position")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("results/underdamped_metrics.png", dpi=300)
plt.show()
