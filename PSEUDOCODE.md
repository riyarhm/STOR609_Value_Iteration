# Algorithm & Pseudocode Comparison

This document outlines the core Value Iteration algorithm used in this package and contrasts it with the theoretical foundation provided in *Artificial Intelligence: Foundations and Computational Agents* (Poole and Mackworth).

## 1. Original Textbook Pseudocode (Figure 9.16)
The standard synchronous Value Iteration algorithm as defined by Poole and Mackworth follows this structure:

```text
procedure Value_iteration_original(S, A, P, R, gamma, theta):
    Initialize V_k[s] = 0 for all s in S
    Initialize V_k_minus_1[s] = 0 for all s in S
    
    // Value Update Loop
    repeat:
        delta = 0
        for each state s in S:
            V_k[s] = max_a (R(s,a) + gamma * sum over s' of P(s'|s,a) * V_k_minus_1[s'])
            delta = max(delta, |V_k[s] - V_k_minus_1[s]|)
            
        V_k_minus_1 = V_k
    until delta < theta
    
    // Policy Extraction Loop
    Initialize policy[s] = None for all s in S
    for each state s in S:
        policy[s] = argmax_a (R(s,a) + gamma * sum over s' of P(s'|s,a) * V_k[s'])
        
    return V_k, policy
```
    
## 1. Custom Implementation Pseudocode

The optimized algorithm implemented in `value_iteration/solver.py` operates as follows:

```text
procedure Value_iteration_custom(S, A, P, R, terminal_states, gamma, theta):
    Initialize V[s] = 0 for all s in S
    Initialize policy[s] = None for all s in S
    
    repeat:
        delta = 0
        for each state s in S:
            if s is in terminal_states: 
                continue
            
            v_old = V[s]
            for each action a available in s:
                Q[s,a] = sum over s' of P(s'|s,a) * (R(s',s,a) + gamma * V[s'])
            
            V[s] = max_a Q[s,a]
            policy[s] = argmax_a Q[s,a]
            
            delta = max(delta, |v_old - V[s]|)
            
    until delta < theta
    return V, policy
```

## Architectural Differences

This implementation makes three deliberate architectural differences from the textbook's pseudocode to improve computational efficiency and handle the specific requirements of the Assessment Grid World:

* **Asynchronous (In-Place) Updates:** Figure 9.16 utilizes a synchronous approach, requiring two distinct arrays ($V_k$ and $V_{k-1}$) to update state values strictly based on the prior iteration. This package utilizes asynchronous (Gauss-Seidel) value iteration, updating a single dictionary in-place. This allows the algorithm to immediately utilize the most recently updated state values, often resulting in faster convergence.
* **Reward Function Structure:** The textbook specifies the reward strictly as $R(s,a)$, placing it outside the transition probability summation. This package accommodates environments where the reward depends on the resulting state by calculating expected rewards as $R(s',s,a)$ inside the summation loop. This is explicitly required to model the boundary and target constraints of the Assessment environment.
* **On-the-Fly Policy Extraction:** Figure 9.16 computes the optimal policy $\pi$ in a completely isolated loop after the value function has fully converged. To improve computational efficiency, this implementation extracts and stores the argmax policy simultaneously during the value update loop, preventing the need to iterate through the entire state-action space a second time.
