# Nature Inspired Computing for Gaming: the Flappy Bird Game

## Game Overview
The project itself is a copy of the Flappy Bird game with the integrated Genetic Programming algorithm. 
The game itself learns how to play and tries to maximize the lifetime of a bird.

The game classes adhere to a hierarchical structure, following the principles of OOP and respecting the principle of single responsibility.

*The game is written in Python using Pygame.*

### Physics Logic Overview

Obstacles move horizontally with the constant velocity. Birds move with the constant velocity vertically, however, at the time of the jump they get the falling acceleration.

### Genetic Programming Cycle (1 Generation)

Population Size: 100 birds
Elitism: Top 5 individuals from the current population are preserved in the next generation without changes.
New Individual Generation (for the remaining 95):
#### 1. Selection (Tournament Method):
Randomly select 30 individuals from the population.
The 2 with the highest fitness are selected as parents.
#### 2. Crossover:
With probability 0.95: crossover is performed.

With probability 0.05: one of the parents is copied directly.

How crossover works:
1) Random subtrees (nodes) are selected from both parents.
2) One parent’s subtree is replaced with the selected subtree from the other.
3) The modified tree becomes the child.

#### 3. Mutation:
With probability 0.2: mutation is applied.
How mutation works:
1) A random node in the decision tree is selected.
2) It is replaced with a newly generated random subtree.

#### 4. Tree Depth Constraint:
If the resulting tree has depth > 10, it is rejected and a new child is generated.

#### Fitness Evaluation
Fitness is computed during the bird’s lifetime based on:

* **Survival Bonus:**
Each update() cycle alive grants +1 to the bird’s fitness.

* **Precision Bonus (Pipe Centering):**
fitness += 100 / (abs(GapCenterPosition - BirdPosition) + 3)
This rewards the bird for staying close to the vertical center of the pipe gap.

* **Penalty for Flying Too High/Low:**
If a bird flies too close to the top or bottom edge of the game screen, its fitness will decrease.

* **Decision Making (Tree)**
Each bird is assigned a decision tree.
This tree is recursively evaluated every frame (update()), converting the tree into a boolean value (True/False).
If the result is True, the bird jumps. Otherwise, it falls.

---

##  Launch Locally

To run launch the main.py file.

*Pygame should be installed.*
