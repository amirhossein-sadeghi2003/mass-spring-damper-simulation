# Mass-Spring-Damper Simulation

This project simulates the behavior of a mass-spring-damper system in different scenarios to better understand the dynamics of a second-order system.

## Description

A mass-spring-damper system is a standard model in physics, dynamics, and control engineering.

The governing equation is:

m x'' + c x' + k x = F(t)

where:

- `m` is the mass
- `c` is the damping coefficient
- `k` is the spring constant
- `x` is the displacement
- `F(t)` is the external force input

This project studies how different system parameters affect the response of the system over time.

## Goals

The goals of this project are:

- model a simple dynamic system
- simulate free response
- compare standard damping cases
- simulate forced response
- analyze the effect of mass
- analyze the effect of spring constant
- visualize velocity response
- compute simple response metrics
- improve understanding of second-order system behavior

## Base Parameters

The main simulation uses:

- `m = 1.0`
- `k = 10.0`

Initial conditions for free response:

- `x0 = 1.0`
- `v0 = 0.0`

Initial conditions for forced response:

- `x0 = 0.0`
- `v0 = 0.0`

The critical damping value is:

c_critical = 2 * sqrt(m * k)

## Simulations

### 1. Free Response and Damping Cases

The free response compares three damping cases:

- `Underdamped`: `c = 2.0`
- `Critically damped`: `c = 2 * sqrt(m * k)`
- `Overdamped`: `c = 10.0`

This part shows how damping changes oscillation and settling behavior.

### 2. Forced Response

The forced response uses:

- `c = 2.0`
- `F(t) = sin(2t)`

This part shows how the system reacts to an external sinusoidal force.

### 3. Effect of Mass

The mass comparison uses:

- `m = 0.5`
- `m = 1.0`
- `m = 2.0`

while keeping `c = 2.0` and `k = 10.0` fixed.

This part shows that lower mass leads to faster motion, while higher mass makes the response slower.

### 4. Effect of Spring Constant

The spring comparison uses:

- `k = 5.0`
- `k = 10.0`
- `k = 20.0`

while keeping `m = 1.0` and `c = 2.0` fixed.

This part shows that a larger spring constant makes the system stiffer and increases the oscillation frequency.

### 5. Velocity Response

The velocity response is plotted for the forced-response case.

This helps show how the speed of the system changes over time, not only its position.

### 6. Response Metrics

For the underdamped free-response case, the project also computes:

- peak displacement
- settling time using a 2% tolerance band

These metrics help describe the transient behavior of the system in a more control-oriented way.

## Results

This project shows several important behaviors of a second-order dynamic system:

- damping changes oscillation and settling behavior
- external force changes the response shape
- mass affects the speed of the response
- spring stiffness affects oscillation frequency
- velocity gives additional information about system motion
- response metrics help quantify transient behavior

## Output

Saved figures:

- `results/damping_comparison.png`
- `results/damping_cases.png`
- `results/forced_response.png`
- `results/mass_effect.png`
- `results/spring_effect.png`
- `results/velocity_response.png`
- `results/underdamped_metrics.png`

## Run

From the project root:

```bash
python3 src/main.py
