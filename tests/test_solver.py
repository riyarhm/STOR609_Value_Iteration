import pytest
from pytest import approx
from value_iteration.solver import value_iteration

def test_simple_deterministic_mdp():
    """A simple deterministic test to ensure basic logic works."""
    # 1. Define the simple MDP
    states = ['A', 'B']
    terminal_states = ['B']
    
    # transitions[state][action] = [(probability, next_state, reward)]
    transitions = {
        'A': {
            'move_to_B': [(1.0, 'B', 10.0)],
            'stay_at_A': [(1.0, 'A', -1.0)]
        },
        'B': {} # Terminal state has no actions
    }
    
    # 2. Run the solver
    V, policy = value_iteration(states, transitions, terminal_states, gamma=0.9)
    
    # 3. Assert the expected mathematical outcomes
    assert V['A'] == approx(10.0)
    assert V['B'] == approx(0.0)
    
    # 4. Assert the expected optimal policy
    assert policy['A'] == 'move_to_B'
    assert policy['B'] is None


def test_example_9_27():
    """
    Test based on Example 9.27 (Sam's weekend decision) from 
    Artificial Intelligence: Foundations and Computational Agents.
    """
    states = ['healthy', 'sick']
    # No terminal states in this ongoing weekend cycle
    terminal_states = [] 
    
    # transitions[state][action] = [(probability, next_state, reward)]
    transitions = {
        'healthy': {
            'relax': [
                (0.95, 'healthy', 7.0), 
                (0.05, 'sick', 7.0)
            ],
            'party': [
                (0.70, 'healthy', 10.0), 
                (0.30, 'sick', 10.0)
            ]
        },
        'sick': {
            'relax': [
                (0.50, 'healthy', 0.0), 
                (0.50, 'sick', 0.0)
            ],
            'party': [
                (0.10, 'healthy', 2.0), 
                (0.90, 'sick', 2.0)
            ]
        }
    }
    
    # Run the solver (using a standard discount factor of 0.9)
    V, policy = value_iteration(states, transitions, terminal_states, gamma=0.9)
    
    # Print the results so you can compare them to your hand calculations
    print("\nConverged Values for Example 9.27:", V)
    print("Optimal Policy for Example 9.27:", policy)
    
    # Verify that the solver successfully calculates floats and assigns valid actions
    assert isinstance(V['healthy'], float)
    assert isinstance(V['sick'], float)
    assert policy['healthy'] in ['relax', 'party']
    assert policy['sick'] in ['relax', 'party']
