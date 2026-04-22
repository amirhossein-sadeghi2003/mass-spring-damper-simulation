# Mass-Spring-Damper Simulation

This project simulates the behavior of a mass-spring-damper system in different scenarios.

## Description

A mass-spring-damper system is a standard second-order dynamic system in physics and engineering.

The governing equation is:

m x'' + c x' + k x = F(t)

where:

- `m` is the mass
- `c` is the damping coefficient
- `k` is the spring constant
- `x` is the displacement
- `F(t)` is the external force input

This project studies how damping, external force, and mass affect the system response.

## Goals

The goals of this project are:

- model a simple dynamic system
- simulate free response
- compare standard damping cases
- simulate forced response
- analyze the effect of mass on system behavior
- understand how system parameters affect motion

## Parameters

Base parameters:

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

### 1. Free Response

The free response compares three damping cases:

- `Underdamped`: `c = 2.0`
- `Critically damped`: `c = 2 * sqrt(m * k)`
- `Overdamped`: `c = 10.0`

### 2. Forced Response

The forced response uses:

- `c = 2.0`
- `F(t) = sin(2t)`

### 3. Effect of Mass

The mass comparison uses:

- `m = 0.5`
- `m = 1.0`
- `m = 2.0`

while keeping `c = 2.0` and `k = 10.0` fixed.

## Results

### Free Response

The free response shows the difference between underdamped, critically damped, and overdamped behavior.

### Forced Response

The forced response shows how the system reacts to a sinusoidal external force.

### Mass Effect

The mass comparison shows that changing the mass changes the speed and oscillation behavior of the system. Lower mass gives a faster response, while higher mass makes the system slower.

## Output

Saved figures:

- `results/damping_comparison.png`
- `results/damping_cases.png`
- `results/forced_response.png`
- `results/mass_effect.png`

## Run

From the project root:

```bash
python3 src/main.py
