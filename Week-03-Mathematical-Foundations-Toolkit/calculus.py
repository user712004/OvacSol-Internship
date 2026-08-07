"""
Calculus Module

This module provides numerical derivative estimation
and gradient descent.
"""


def numerical_derivative(function, x, h=1e-5):
    """Estimate the derivative using finite differences."""
    return (function(x + h) - function(x - h)) / (2 * h)


def gradient_descent(function, derivative, initial_x,
                     learning_rate=0.1, iterations=20):
    """Use gradient descent to find a minimum."""
    x = initial_x
    history = [x]

    for _ in range(iterations):
        gradient = derivative(x)
        x = x - learning_rate * gradient
        history.append(x)

    return x, history