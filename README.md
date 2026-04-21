# Mass-Spring-Damper Simulation

This project simulates the behavior of a mass-spring-damper system in two cases:

- free response
- forced response

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

This project studies how damping changes the system response, and how the system behaves when an external sinusoidal force is applied.

## Goals

The goals of this project are:

- model a simple dynamic system
- simulate free response
- compare standard damping cases
- simulate forced response
- understand how damping and input force affect the motion

## Parameters

The simulation uses:

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

The free response compares:

- `Underdamped`: `c = 2.0`
- `Critically damped`: `c = 2 * sqrt(m * k)`
- `Overdamped`: `c = 10.0`

The forced response uses:

- `c = 2.0`
- `F(t) = sin(2t)`

## Results

### Free Response

The free response compares three damping cases:

- the underdamped case oscillates before settling
- the critically damped case returns quickly without oscillation
- the overdamped case returns more slowly without oscillation

### Forced Response

The forced response shows how the system reacts to a sinusoidal input force.

The output displacement does not exactly match the input force because the system dynamics depend on mass, damping, and spring stiffness.

## Output

Saved figures:

- `results/damping_comparison.png`
- `results/damping_cases.png`
- `results/forced_response.png`

## Run

From the project root:

```bash
python3 src/main.py
