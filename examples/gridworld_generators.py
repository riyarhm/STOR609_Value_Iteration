def get_assessment_grid_world():
    """
    Generates the specific Grid World MDP required.
    
    Returns:
    --------
    states : list
    transitions : dict
    terminal_states : list
    """
    # Define all possible states
    states = ['TL', 'TR', 'BL', 'BR']
    
    # State BR is explicitly defined as terminal
    terminal_states = ['BR']
    
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
