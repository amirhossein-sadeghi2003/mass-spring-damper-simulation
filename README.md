# Mass-Spring-Damper Simulation

This project simulates the free response of a mass-spring-damper system and compares three standard damping cases:

- underdamped
- critically damped
- overdamped

## Description

A mass-spring-damper system is a common second-order dynamic system in physics and engineering.

The governing equation is:

m x'' + c x' + k x = 0

where:

- `m` is the mass
- `c` is the damping coefficient
- `k` is the spring constant
- `x` is the displacement

The purpose of this project is to study how the damping coefficient changes the system response over time.

## Goal

The main goals of this project are:

- model a simple dynamic system
- simulate its free response
- compare standard damping behaviors
- understand how damping affects oscillation and settling

## Parameters

The simulation uses:

- `m = 1.0`
- `k = 10.0`

Initial conditions:

- `x0 = 1.0`
- `v0 = 0.0`

The critical damping value is computed as:

c_critical = 2 * sqrt(m * k)

Based on this, the following cases are compared:

- `Underdamped`: `c = 2.0`
- `Critically damped`: `c = 2 * sqrt(m * k)`
- `Overdamped`: `c = 10.0`

## Result

The simulation shows the difference between three damping cases:

- the underdamped case oscillates before settling
- the critically damped case returns to equilibrium quickly without oscillating
- the overdamped case returns more slowly without oscillation

This comparison helps show the effect of damping on the motion of a second-order system.

## Output

Saved figures:

- `results/damping_comparison.png`
- `results/damping_cases.png`

## Run

From the project root:

```bash
python3 src/main.py
