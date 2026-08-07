"""
Mathematical Foundations Toolkit for AI

Week 3 Internship Project
OvacSol Pvt. Ltd.
"""

import numpy as np

from vectors import (
    add_vectors,
    subtract_vectors,
    scalar_multiply,
    dot_product,
    magnitude,
)

from matrices import (
    add_matrices,
    subtract_matrices,
    multiply_matrices,
    transpose_matrix,
    determinant,
    inverse_matrix,
)

from calculus import (
    numerical_derivative,
    gradient_descent,
)

from probability import (
    simulate_dice_rolls,
    experimental_probabilities,
    theoretical_probability,
)

from statistics import (
    calculate_mean,
    calculate_median,
    calculate_mode,
    calculate_variance,
    calculate_standard_deviation,
    calculate_range,
)

from linear_regression import (
    train_linear_regression,
    calculate_cost,
    plot_regression,
)


def vector_demo():
    """Demonstrate vector operations."""
    print("\n========== VECTOR OPERATIONS ==========")

    vector_a = np.array([85, 90])
    vector_b = np.array([78, 88])

    print("Vector A:", vector_a)
    print("Vector B:", vector_b)
    print("Addition:", add_vectors(vector_a, vector_b))
    print("Subtraction:", subtract_vectors(vector_a, vector_b))
    print("Scalar Multiplication:", scalar_multiply(vector_a, 2))
    print("Dot Product:", dot_product(vector_a, vector_b))
    print("Magnitude of A:", magnitude(vector_a))


def matrix_demo():
    """Demonstrate matrix operations."""
    print("\n========== MATRIX OPERATIONS ==========")

    matrix_a = np.array([
        [2, 1],
        [1, 3]
    ], dtype=float)

    matrix_b = np.array([
        [4, 2],
        [3, 5]
    ], dtype=float)

    print("Matrix A:\n", matrix_a)
    print("\nMatrix B:\n", matrix_b)

    print("\nAddition:\n", add_matrices(matrix_a, matrix_b))
    print("\nSubtraction:\n", subtract_matrices(matrix_a, matrix_b))
    print("\nMultiplication:\n", multiply_matrices(matrix_a, matrix_b))
    print("\nTranspose of A:\n", transpose_matrix(matrix_a))
    print("\nDeterminant of A:", determinant(matrix_a))
    print("\nInverse of A:\n", inverse_matrix(matrix_a))


def linear_algebra_demo():
    """Demonstrate solving a system of linear equations."""
    print("\n========== LINEAR ALGEBRA ==========")

    matrix_a = np.array([
        [2, 1],
        [1, 3]
    ], dtype=float)

    vector_b = np.array([8, 13], dtype=float)

    solution = np.linalg.solve(matrix_a, vector_b)

    print("System:")
    print("2x + y = 8")
    print("x + 3y = 13")

    print("\nSolution [x, y]:", solution)

    print(
        "\nVerification:",
        np.matmul(matrix_a, solution)
    )


def calculus_demo():
    """Demonstrate numerical differentiation and gradient descent."""
    print("\n========== CALCULUS ==========")

    def function(x):
        return x ** 2 + 3 * x + 2

    def derivative(x):
        return 2 * x + 3

    starting_point = 5

    numerical = numerical_derivative(
        function,
        starting_point
    )

    minimum, history = gradient_descent(
        function,
        derivative,
        starting_point,
        learning_rate=0.1,
        iterations=20
    )

    print("Function: f(x) = x² + 3x + 2")
    print("Numerical derivative at x = 5:", numerical)
    print("Estimated minimum:", minimum)
    print("Minimum function value:", function(minimum))
    print("Iterations:", len(history) - 1)


def probability_demo():
    """Demonstrate experimental and theoretical probability."""
    print("\n========== PROBABILITY ==========")

    rolls = simulate_dice_rolls(1000)

    experimental = experimental_probabilities(rolls)
    theoretical = theoretical_probability()

    print("Total dice rolls:", len(rolls))

    print("\nOutcome | Experimental | Theoretical")
    print("-------------------------------------")

    for outcome in range(1, 7):
        print(
            f"   {outcome}    |"
            f"    {experimental[outcome]:.3f}    |"
            f"    {theoretical[outcome]:.3f}"
        )


def statistics_demo():
    """Demonstrate descriptive statistics."""
    print("\n========== STATISTICS ==========")

    marks = np.array([
        78, 85, 90, 72, 88,
        95, 85, 82, 91, 76,
        85, 89, 93, 80, 87
    ])

    print("Student Marks:", marks)
    print("Mean:", calculate_mean(marks))
    print("Median:", calculate_median(marks))
    print("Mode:", calculate_mode(marks))
    print("Variance:", calculate_variance(marks))
    print(
        "Standard Deviation:",
        calculate_standard_deviation(marks)
    )
    print("Range:", calculate_range(marks))


def linear_regression_demo():
    """Train and visualize a linear regression model."""
    print("\n========== LINEAR REGRESSION ==========")

    study_hours = np.array([
        1, 2, 3, 4, 5,
        6, 7, 8, 9, 10
    ], dtype=float)

    exam_marks = np.array([
        35, 42, 50, 55, 62,
        68, 74, 81, 88, 94
    ], dtype=float)

    weight, bias = train_linear_regression(
        study_hours,
        exam_marks,
        learning_rate=0.001,
        iterations=5000
    )

    cost = calculate_cost(
        study_hours,
        exam_marks,
        weight,
        bias
    )

    print("Study Hours:", study_hours)
    print("Exam Marks:", exam_marks)
    print("\nLearned Weight:", weight)
    print("Learned Bias:", bias)
    print("Final Cost:", cost)

    plot_regression(
        study_hours,
        exam_marks,
        weight,
        bias,
        "charts/regression_plot.png"
    )

    print("\nRegression chart saved:")
    print("charts/regression_plot.png")


def main():
    """Run the complete Mathematical Foundations Toolkit."""

    print("==============================================")
    print("   MATHEMATICAL FOUNDATIONS TOOLKIT FOR AI")
    print("              WEEK 3 PROJECT")
    print("             OvacSol Pvt. Ltd.")
    print("==============================================")

    vector_demo()
    matrix_demo()
    linear_algebra_demo()
    calculus_demo()
    probability_demo()
    statistics_demo()
    linear_regression_demo()

    print("\n==============================================")
    print("       PROJECT EXECUTED SUCCESSFULLY")
    print("==============================================")


if __name__ == "__main__":
    main()