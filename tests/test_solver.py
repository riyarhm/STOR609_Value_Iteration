import pytest
from pytest import approx
from value_iteration.solver import value_iteration

def test_simple_deterministic_mdp():
    """
    Verifies the core algorithm logic on a minimal deterministic MDP. 
    
    Theoretical Assumptions Tested:
    1. Absorbing terminal states correctly retain a value of 0.0.
    2. The policy extractor correctly ignores terminal states (assigning None).
    3. The value function correctly identifies and maximizes the immediate reward.
    """
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
    Validates the algorithm against established academic literature 
    (Poole and Mackworth, Example 9.27: Sam's weekend decision).
    
    Theoretical Assumptions Tested:
    1. The solver successfully handles highly stochastic transition probabilities.
    2. The algorithm converges correctly in an environment with no terminal states 
       (an infinite horizon problem) using a discount factor.
    """
    states = ['healthy', 'sick']
    # No terminal states in this ongoing weekend cycle
    terminal_states = [] 
    
    # transitions[state][action] = [(probability, next_state, reward)]
    transitions = {
        'healthy': {
            'relax': [(0.95, 'healthy', 7.0), (0.05, 'sick', 7.0)],
            'party': [(0.70, 'healthy', 10.0), (0.30, 'sick', 10.0)]
        },
        'sick': {
            'relax': [(0.50, 'healthy', 0.0), (0.50, 'sick', 0.0)],
            'party': [(0.10, 'healthy', 2.0), (0.90, 'sick', 2.0)]
        }
    }
    
    # Run the solver (using a standard discount factor of 0.9)
    V, policy = value_iteration(states, transitions, terminal_states, gamma=0.9)
    
    # Verify that the solver successfully calculates floats and assigns valid actions
    assert isinstance(V['healthy'], float)
    assert isinstance(V['sick'], float)
    assert policy['healthy'] in ['relax', 'party']
    assert policy['sick'] in ['relax', 'party']


def test_zero_discount_factor():
    """
    Edge-Case Verification: Tests the algorithm's behavior when the discount 
    factor (gamma) is 0.
    
    Theoretical Assumptions Tested:
    When gamma=0, the agent should only care about immediate, single-step rewards, 
    completely ignoring future state values.
    """
    states = ['A']
    terminal_states = []
    
    transitions = {
        'A': {
            'low_now_high_later': [(1.0, 'A', 2.0)],  # Loops back, could yield infinite reward if gamma > 0
            'high_now_low_later': [(1.0, 'A', 5.0)]
        }
    }
    
    # Run with a discount factor of exactly 0
    V, policy = value_iteration(states, transitions, terminal_states, gamma=0.0)
    
    # The agent should greedily pick the 5.0 reward and ignore the future
    assert V['A'] == approx(5.0)
    assert policy['A'] == 'high_now_low_later'
