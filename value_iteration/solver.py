def value_iteration(states, transitions, terminal_states=None, gamma=0.9, theta=1e-6):
    """
    Implements the value iteration algorithm for Markov Decision Processes.

    Parameters:
    -----------
    states : list
        A list of all possible states in the MDP.
    transitions : dict
        A nested dictionary representing P(s'|s,a) and R(s'|s,a).
        Format: transitions[state][action] = [(probability, next_state, reward), ...]
    terminal_states : list, optional
        A list of terminal states where the episode ends. Default is an empty list.
    gamma : float, optional
        The discount factor [0, 1]. Default is 0.9.
    theta : float, optional
        A small threshold for determining convergence. Default is 1e-6.

    Returns:
    --------
    V : dict
        The optimal value function, mapping states to values.
    policy : dict
        The optimal policy, mapping states to the best action.
    """
    if terminal_states is None:
        terminal_states = []

    # Initialize the value function to zero for all states
    V = {s: 0.0 for s in states}
    policy = {s: None for s in states}

    while True:
        delta = 0.0
        
        for s in states:
            if s in terminal_states:
                continue  # Terminal states have a value of 0 and no actions
                
            v = V[s]
            action_values = {}
            
            # Calculate the expected value for each possible action
            for a, outcomes in transitions.get(s, {}).items():
                expected_value = 0.0
                for prob, next_s, reward in outcomes:
                    expected_value += prob * (reward + gamma * V[next_s])
                action_values[a] = expected_value
                
            # Greedily update the value function and policy
            if action_values:
                best_action = max(action_values, key=action_values.get)
                V[s] = action_values[best_action]
                policy[s] = best_action
                
            delta = max(delta, abs(v - V[s]))
            
        # Check for convergence
        if delta < theta:
            break
            
    return V, policy
