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
- Asynchronous Solver: Implements a Gauss-Seidel update rule that speeds up convergence by using the most recently calculated values within a single iteration.
- Environment-Agnostic Design: The solver does not depend on a specific grid or problem shape. It accepts any MDP defined by a standard transition and reward dictionary.
- Verification Suite: Includes built-in unit tests (`pytest`) and visualization tools in the 2x2 Gridworld problem (`seaborn` heatmaps) to verify the accuracy and stability of the calculated optimal policy.
- Extensible Architecture: Designed so that new reward structures or transition dynamics can be plugged in without modifying the core algorithm.


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

The detailed code of this is given in [examples/sam_example.py](examples/sam_example.py).

After running the code above with a discount factor of γ=0.9, the solver produces the following optimal policy:
If healthy, then Sam should party.
If sick, then Sam should relax.

###  2x2 Gridworld example
To see a more detailed application of how this package solves and visualises the stochastic 2x2 Grid World for Assessment , see the Jupyter Notebook in the [examples/grid_world.ipynb](examples/grid_world.ipynb).


## **Algorithm and Pseudocode**
For a detailed look at the algorithm's pseudocode and a direct architectural comparison to Figure 9.16 in Poole and Mackworth, please see the [PSEUDOCODE.md](PSEUDOCODE.md) file in this repository.


## **License**
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/gpl-3.0.txt>.

## **Github Repository**
Source files for the package can be found at [https://github.com/riyarhm/STOR609_Value_Iteration/tree/main/value_iteration](https://github.com/riyarhm/STOR609_Value_Iteration/tree/main/value_iteration).

## **Contributors**
- Riya Raheem [email](mailto:riyaraheemkp@gmail.com) (**Author**)
  (**Maintainer**) (**Creator**) (**Translator**)
  
## **References**

Poole, D. L., & Mackworth, A. K. (2017). *Artificial Intelligence: Foundations of Computational Agents* (2nd ed.). Cambridge University Press.


   
   
