"""
Value Iteration Solver Package

This package provides a robust, reusable implementation of the Value Iteration 
algorithm for solving discrete Markov Decision Processes (MDPs). 

It is designed to mathematically evaluate stochastic environments by 
calculating the optimal value function (V) and extracting the optimal 
policy (π*) that maximizes cumulative discounted rewards.
"""

__author__ = "Riya Raheem"
__version__ = "1.0.0"

# Expose the core functions to the user at the package level
from .solver import value_iteration
from .utilities import print_results

# Define exactly what gets imported when a user runs `from value_iteration import *`
__all__ = ['value_iteration', 'print_results']
