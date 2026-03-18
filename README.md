# `value_iteration`

- [Description](#description)
- [Installation](#installation)
- [Example](#example)
  - [Simple 2-state MDP example](#simple-2-mdp-example)
  - [2x2 Gridworld example](#gridworld-example)
- [Pseudocode](#pseudocode)
- [License](#license)
- [GitHub Repository](#github-repository)
- [Contributors](#contributors)
- [References](#references)

## **Description**

The `value_iteration` python package provides an implementation of the value iteration algorithm. This algorithm is a well-known solution method for finding the optimal policy of a Markov Decision Process (MDP). 

For a range of problems that can be modelled as MDPs, the value iteration algorithm finds the optimal policy by maximising a value function iteratively. 

To learn more about MDPs and the value iteration algorithm, the user can refer to Sections [9.5](https://artint.info/2e/html2e/ArtInt2e.Ch9.S5.html) and [9.5.1](https://artint.info/2e/html2e/ArtInt2e.Ch9.S5.SS1.html) of [Artificial Intelligence: Foundations and Computational Agents 2nd edition](https://artint.info/2e/html2e/ArtInt2e.html).

**Key Features**
- Implements the asynchronous (Gauss-Seidel) value iteration function, which often converges faster than the standard synchronous version.
- Includes an interactive example of the Assessment 2x2 Gridworld problem solved and visualised using `seaborn`.
- Designed with a modular structure, decoupling environment transition dynamics from the solver engine to allow for high reusability.


## **Installation**

This python package can be installed from GitHub with pip.
#### installing from github with pip
``` python
python -m pip install "git+https://github.com/riyarhm/STOR609_Value_Iteration"
```

## **Example**

### Simple 2-state MDP example
This example is taken from [Example 9.27](https://artint.info/2e/html2e/ArtInt2e.Ch9.S5.html#Ch9.Thmciexamplered27) from [Artificial Intelligence: Foundations and Computational Agents 2nd edition](https://artint.info/2e/html2e/ArtInt2e.html). 

Suppose Sam wanted to make an informed decision about whether to party or relax over the weekend. Sam prefers to party, but is worried about getting sick. Such a problem can be modeled as an MDP with two states, *healthy* and *sick*, and two actions, *relax* and *party*. Thus, the set of states is 
$$S = \{\textit{healthy}, \textit{sick} \}$$.

Based on experience, Sam estimates that $P(s' \vert s, a)$ is given by:

| S   | A  | Probability of $s' =$ _healthy_   |
|----|----|---------------------------------------------|
| healthy  | relax   | 0.95  |
| healthy  | party   | 0.7  |
| sick  | relax   | 0.5  |
| sick  | party   | 0.1  |

Sam estimates his immediate rewards to be:

| S   | A  | Reward   |
|----|----|---------------------------------------------|
| healthy  | relax   | 7  |
| healthy  | party   | 10  |
| sick  | relax   | 0  |
| sick  | party   | 2  |

**The problem is to determine what Sam should do each weekend.**

```python
from value_iteration import value_iteration

# 1. Define the environment dynamics
S = {"healthy", "sick"}
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

# 2. Implement the value iteration algorithm
V, policy = value_iteration(S, transitions, gamma=0.9)

# 3. Display results
for s in S:
    print(f"If {s}, then Sam should {policy[s]}.")
```

###  2x2 Gridworld example
To see a more detailed application of how this package solves and visualises the stochastic 2x2 Grid World for Assessment , see the Jupyter Notebook in the [examples/grid_world.ipynb](examples/grid_world.ipynb).


## **Algorithm and Pseudocode**
For a detailed look at the algorithm's pseudocode and a direct architectural comparison to Figure 9.16 in Poole and Mackworth, please see the PSEUDOCODE.md file in this repository.


## **License**
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License.

## **Github Repository**
Source files for the package can be found at [https://github.com/riyarhm/STOR609_Value_Iteration/tree/main/value_iteration](https://github.com/riyarhm/STOR609_Value_Iteration/tree/main/value_iteration).

## **Contributors**
- Riya Raheem [email](mailto:riyaraheemkp@gmail.com) (**Author**)
  (**Maintainer**) (**Creator**) (**Translator**)
  
## **References**

Poole, D. L., & Mackworth, A. K. (2017). *Artificial Intelligence: Foundations of Computational Agents* (2nd ed.). Cambridge University Press.


   
   
