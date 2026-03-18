"""
test_sam.py
A reproduction script for the 2-state 'Sam's Weekend' MDP.
This script verifies the value_iteration solver against a known benchmark.
"""

from value_iteration.solver import value_iteration

def run_sam_example():
    # 1. Define the State Space
    S = {"healthy", "sick"}

    # 2. Define the Transitions and Rewards
    # Format: transitions[state][action] = [(probability, next_state, reward), ...]
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

    # 3. Run the Asynchronous Value Iteration
    # We use gamma=0.9 as specified in the benchmark
    V, policy = value_iteration(S, transitions, gamma=0.9)

    print("-" * 30)
    print("REPRODUCTION RESULTS")
    print("-" * 30)

    # 4. Display the Optimal Policy (The "Decision")
    print("\n[Optimal Policy]")
    for s in sorted(S):
        print(f"If {s}, then Sam should {policy[s].upper()}.")

    # 5. Display the Value Function (The "Numerical Validation")
    print("\n[Converged Values (V*)]")
    for s in sorted(S):
        print(f"V({s}): {V[s]:.2f}")
    
    print("-" * 30)

if __name__ == "__main__":
    run_sam_example()
