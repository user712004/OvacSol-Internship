"""
Linear Regression Module

This module implements simple linear regression
from scratch using gradient descent.
"""

import numpy as np
import matplotlib.pyplot as plt


def predict(x, weight, bias):
    """Generate predictions using y = wx + b."""
    return weight * x + bias


def calculate_cost(x, y, weight, bias):
    """Calculate the mean squared error cost."""
    predictions = predict(x, weight, bias)
    errors = predictions - y

    return np.mean(errors ** 2)


def train_linear_regression(
    x,
    y,
    learning_rate=0.001,
    iterations=5000
):
    """Train a linear regression model using gradient descent."""
    weight = 0.0
    bias = 0.0

    number_of_samples = len(x)

    for _ in range(iterations):
        predictions = predict(x, weight, bias)
        errors = predictions - y

        weight_gradient = (
            2 / number_of_samples
        ) * np.sum(x * errors)

        bias_gradient = (
            2 / number_of_samples
        ) * np.sum(errors)

        weight -= learning_rate * weight_gradient
        bias -= learning_rate * bias_gradient

    return weight, bias


def plot_regression(x, y, weight, bias, filename):
    """Create and save the regression plot."""
    predictions = predict(x, weight, bias)

    plt.figure(figsize=(8, 5))

    plt.scatter(
        x,
        y,
        label="Actual Data"
    )

    plt.plot(
        x,
        predictions,
        label="Regression Line"
    )

    plt.xlabel("Study Hours")
    plt.ylabel("Exam Marks")
    plt.title("Linear Regression from Scratch")
    plt.legend()
    plt.grid(True)

    plt.savefig(filename)
    plt.close()