# Mass-Spring-Damper Simulation

This project simulates the response of a mass-spring-damper system for different damping values.

## Description

A mass-spring-damper system is a simple dynamic system that is widely used in physics and engineering.  
The goal of this project is to study how damping affects the motion of the system over time.

The governing equation is:

m x'' + c x' + k x = 0

where:

- `m` is the mass
- `c` is the damping coefficient
- `k` is the spring constant
- `x` is the displacement

## Goal

The main goal of this project is to:

- model a simple dynamic system
- simulate its motion
- compare the response for different damping values
- understand how damping changes the system behavior

## Parameters

The simulation uses:

- `m = 1.0`
- `k = 10.0`
- `c = [0.5, 2.0, 5.0]`

Initial conditions:

- `x0 = 1.0`
- `v0 = 0.0`

## Result

The plot below shows the displacement of the system over time for three different damping values.

- for smaller damping, the system oscillates more
- for larger damping, the system settles faster
- increasing damping reduces the oscillations

## Output

Saved figure:

`results/damping_comparison.png`

## Run

From the project root:

```bash
python3 src/main.py
