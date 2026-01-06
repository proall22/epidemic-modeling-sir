# Mathematical Modeling of Epidemics Using the SIR Model

## Overview

This project investigates the spread of infectious diseases using the classical

SIR (Susceptible–Infected–Recovered) mathematical model. The goal is to demonstrate

how differential equations and numerical methods can be used to analyze epidemic

dynamics and assess the impact of public health interventions.

---


## Problem Statement

Understanding how diseases spread is essential for effective public health planning.

This project addresses the following questions:

- How does an infectious disease evolve over time?

- How do infection and recovery rates influence epidemic peaks?

- How effective are interventions such as lockdowns?


## Methodology

- Formulation of the SIR model as a system of ordinary differential equations

- Numerical solution using SciPy’s ODE solvers

- Scenario-based simulations to analyze intervention strategies

- Visualization and interpretation of results



## Project Structure

```

epidemic-modeling-sir/

├── notebooks/

│ └── SIR\_Model\_Simulation.ipynb

├── src/

│ └── sir\_model.py

├── figures/

├── requirements.txt

├── README.md

```

## Tools and Technologies

- Python

- NumPy

- SciPy

- Matplotlib

- Google Colab



## Results Summary

The simulations show that reducing the infection rate significantly lowers

the peak number of infected individuals and slows disease spread. These results

highlight the value of mathematical modeling in guiding real-world policy decisions.



## Limitations

- Assumes homogeneous mixing of the population

- No demographic or spatial structure

- Permanent immunity after recovery



## Future Work

- Extension to SEIR and vaccination models

- Parameter estimation using real epidemiological data

- Incorporation of stochastic effects



## Author

Misgana(proall22)

Software Engineering Graduate  





