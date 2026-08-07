"""
Matrix Operations Module

This module provides basic matrix operations
using NumPy.
"""

import numpy as np


def add_matrices(matrix_a, matrix_b):
    """Return the sum of two matrices."""
    return np.add(matrix_a, matrix_b)


def subtract_matrices(matrix_a, matrix_b):
    """Return the difference between two matrices."""
    return np.subtract(matrix_a, matrix_b)


def multiply_matrices(matrix_a, matrix_b):
    """Return the matrix product."""
    return np.matmul(matrix_a, matrix_b)


def transpose_matrix(matrix):
    """Return the transpose of a matrix."""
    return np.transpose(matrix)


def determinant(matrix):
    """Return the determinant of a matrix."""
    return np.linalg.det(matrix)


def inverse_matrix(matrix):
    """Return the inverse of a matrix."""
    return np.linalg.inv(matrix)


def identity_matrix(size):
    """Return an identity matrix."""
    return np.eye(size)


def zero_matrix(rows, columns):
    """Return a zero matrix."""
    return np.zeros((rows, columns))