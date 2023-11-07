# -*- coding: utf-8 -*-
"""Exercise 3.

Least Square
"""

import numpy as np


def least_squares(y, tx):
    """calculate the least squares."""
    # ***************************************************
    # INSERT YOUR CODE HERE
    # least squares: TODO
    # returns mse, and optimal weights
    a = tx.T @ tx
    b = tx.T @ y
    return np.linalg.solve(a, b)
    # ***************************************************
    raise NotImplementedError
