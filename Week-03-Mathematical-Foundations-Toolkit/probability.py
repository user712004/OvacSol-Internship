"""
Probability Module

This module simulates dice rolls, compares experimental
and theoretical probabilities, and creates a visualization.
"""

import numpy as np
import matplotlib.pyplot as plt


def simulate_dice_rolls(number_of_rolls=1000):
    """Simulate rolling a six-sided die."""
    return np.random.randint(1, 7, size=number_of_rolls)


def experimental_probabilities(rolls):
    """Calculate experimental probability for each outcome."""
    probabilities = {}

    for outcome in range(1, 7):
        count = np.sum(rolls == outcome)
        probabilities[outcome] = count / len(rolls)

    return probabilities


def theoretical_probability():
    """Return the theoretical probability for each outcome."""
    return {outcome: 1 / 6 for outcome in range(1, 7)}


def plot_probability_comparison(
    experimental,
    theoretical,
    filename
):
    """Create and save an experimental vs theoretical chart."""

    outcomes = list(experimental.keys())

    experimental_values = [
        experimental[outcome]
        for outcome in outcomes
    ]

    theoretical_values = [
        theoretical[outcome]
        for outcome in outcomes
    ]

    x = np.arange(len(outcomes))
    width = 0.35

    plt.style.use("dark_background")

    fig, ax = plt.subplots(
        figsize=(10, 6),
        dpi=160
    )

    fig.patch.set_facecolor("#0B1020")
    ax.set_facecolor("#111827")

    ax.bar(
        x - width / 2,
        experimental_values,
        width,
        label="Experimental Probability"
    )

    ax.bar(
        x + width / 2,
        theoretical_values,
        width,
        label="Theoretical Probability"
    )

    ax.set_title(
        "Dice Probability: Experimental vs Theoretical",
        fontsize=17,
        fontweight="bold",
        pad=18
    )

    ax.set_xlabel(
        "Dice Outcome",
        fontsize=11,
        labelpad=10
    )

    ax.set_ylabel(
        "Probability",
        fontsize=11,
        labelpad=10
    )

    ax.set_xticks(x)
    ax.set_xticklabels(outcomes)

    ax.grid(
        axis="y",
        linestyle="--",
        linewidth=0.6,
        alpha=0.18
    )

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    ax.legend(
        frameon=True,
        framealpha=0.85
    )

    fig.tight_layout()

    plt.savefig(
        filename,
        dpi=200,
        bbox_inches="tight",
        facecolor=fig.get_facecolor()
    )

    plt.close(fig)