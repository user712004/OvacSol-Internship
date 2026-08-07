"""
Statistics Module

This module provides basic descriptive statistics
using NumPy.
"""

import numpy as np


def calculate_mean(data):
    """Return the mean of the dataset."""
    return np.mean(data)


def calculate_median(data):
    """Return the median of the dataset."""
    return np.median(data)


def calculate_mode(data):
    """Return the mode of the dataset."""
    values, counts = np.unique(data, return_counts=True)
    return values[np.argmax(counts)]


def calculate_variance(data):
    """Return the variance of the dataset."""
    return np.var(data)


def calculate_standard_deviation(data):
    """Return the standard deviation of the dataset."""
    return np.std(data)


def calculate_range(data):
    """Return the range of the dataset."""
    return np.max(data) - np.min(data)