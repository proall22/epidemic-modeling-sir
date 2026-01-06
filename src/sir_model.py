"""
SIR epidemic model implementation.

This module defines the classical SIR model used to simulate
the spread of infectious diseases using ordinary differential equations.
"""

def sir_model(y, t, beta, gamma):
    """
    Computes the derivatives for the SIR model.

    Parameters
    ----------
    y : list or tuple
        Current state [S, I, R]
    t : float
        Time variable (not explicitly used, included for compatibility)
    beta : float
        Infection rate
    gamma : float
        Recovery rate

    Returns
    -------
    list
        Derivatives [dS/dt, dI/dt, dR/dt]
    """
    S, I, R = y

    dSdt = -beta * S * I
    dIdt = beta * S * I - gamma * I
    dRdt = gamma * I

    return [dSdt, dIdt, dRdt]
