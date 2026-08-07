"""
Vector Operations Module

This module provides basic vector operations
using NumPy.
"""

import numpy as np


def add_vectors(vector_a, vector_b):
    """Return the sum of two vectors."""
    return np.add(vector_a, vector_b)


def subtract_vectors(vector_a, vector_b):
    """Return the difference between two vectors."""
    return np.subtract(vector_a, vector_b)


def scalar_multiply(vector, scalar):
    """Multiply a vector by a scalar."""
    return np.multiply(vector, scalar)


def dot_product(vector_a, vector_b):
    """Return the dot product of two vectors."""
    return np.dot(vector_a, vector_b)


def magnitude(vector):
    """Return the magnitude of a vector."""
    return np.linalg.norm(vector)