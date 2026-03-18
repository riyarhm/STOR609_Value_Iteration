def get_assessment_grid_world():
    """
    Generates the specific 2x2 Grid World MDP required for Assessment.
    
    This function declaratively defines the state space, terminal states, 
    and the stochastic transition dynamics (which intrinsically include 
    the expected rewards) for the assessment's specific problem. By separating 
    this data generation from the mathematical solver, the codebase remains 
    modular and reusable.

    Returns:
    --------
    states : list of str
        The complete state space representing the 2x2 grid: ['TL', 'TR', 'BL', 'BR'].
    transitions : dict
        A nested dictionary representing the transition probabilities P(s'|s,a) 
        and expected rewards R(s',s,a). 
        Format: transitions[current_state][action] = [(probability, next_state, reward), ...]
    terminal_states : list of str
        States that safely terminate the MDP episode (values remain 0).
    """
    # Define all possible states
    states = ['TL', 'TR', 'BL', 'BR']
    
    # Define Terminal state
    # State BR is explicitly defined as terminal
    terminal_states = ['BR']
    
    # Define Transition dynamics and rewards
    # Transitions map: state -> action -> list of (probability, next_state, reward)
    transitions = {
        'TL': {
            'R': [(0.9, 'TR', -1.0), (0.1, 'BL', -2.0)],
            'D': [(0.9, 'BL', -2.0), (0.1, 'TR', -1.0)]
        },
        'TR': {
            'L': [(0.9, 'TL', -3/2), (0.1, 'BR', 10.0)],
            'D': [(0.8, 'BR', 15.0), (0.2, 'TL', -1.0)]
        },
        'BL': {
            'R': [(0.9, 'BR', 20.0), (0.1, 'TL', -5/2)],
            'U': [(0.8, 'TL', -1/2), (0.2, 'BR', 5.0)]
        },
        'BR': {}  # Terminal state has no outgoing actions
    }
    
    return states, transitions, terminal_states
