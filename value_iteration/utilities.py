def print_results(V, policy):
    """
    A utility function to neatly print the value function and policy.
    
    Parameters:
    -----------
    V : dict
        The optimal value function.
    policy : dict
        The optimal policy mapping states to actions.
    """
    print("--- Optimal Value Function ---")
    for state, value in V.items():
        print(f"State {state}: {value:.4f}")
        
    print("\n--- Optimal Policy ---")
    for state, action in policy.items():
        if action is None:
            print(f"State {state}: Terminal (No Action)")
        else:
            print(f"State {state}: Take action '{action}'")
