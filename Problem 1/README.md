# Problem 1: Water Jug Problem

## 1. Problem Statement

The Water Jug Problem is a classic state-space search problem in Artificial Intelligence. You are given two jugs of capacities $X$ and $Y$ litres, where $X > 0$ and $Y > 0$. Neither jug has any measuring markings. There is an unlimited supply of water available from a tap and a drain to empty the jugs.

The objective is to determine a sequence of allowable operations to measure exactly $Z$ litres of water into either of the two jugs.

### Allowed Operations:
1. **Fill Jug 1 completely** with water.
2. **Fill Jug 2 completely** with water.
3. **Empty Jug 1 completely** into the drain.
4. **Empty Jug 2 completely** into the drain.
5. **Pour water from Jug 1 into Jug 2** until Jug 1 is empty or Jug 2 becomes completely full.
6. **Pour water from Jug 2 into Jug 1** until Jug 2 is empty or Jug 1 becomes completely full.

---

## 2. Objective

The Python program aims to:
- Accept user inputs for jug capacities ($X, Y$) and target volume ($Z$).
- Validate inputs and mathematically determine whether the target is achievable.
- Model the problem as a state-space search graph.
- Implement **Breadth-First Search (BFS)** to find the shortest (optimal) sequence of steps to measure $Z$ litres.
- Avoid cycles by maintaining a `visited` set of states.
- Output each step with its step number, a human-readable description of the operation, and the water level in both jugs `(jug1, jug2)`.
- Clearly confirm when the goal state is reached.

---

## 3. Algorithm Used: Breadth-First Search (BFS)

### Why BFS?
- **Completeness**: If a valid solution exists, BFS will always find it.
- **Optimality**: Since each action costs 1 step (uniform edge weights), BFS guarantees finding the solution with the minimum number of operations.
- **Cycle Prevention**: Exploring states in levels while tracking already-visited states prevents infinite loops (such as repeatedly filling and emptying the same jug).

### Mathematical Solvability (Bezout's Identity):
Before initiating the graph search, the program performs a mathematical check:
1. **Capacity Limit**: Target $Z \le \max(X, Y)$ because neither jug can hold more water than its maximum capacity.
2. **Divisibility Condition**: By **Bezout's Identity**, any amount of water formed by pouring, filling, and emptying operations can be represented as an integer linear combination:
   $$a \cdot X + b \cdot Y = Z$$
   Therefore, $Z$ must be an integer multiple of the Greatest Common Divisor ($\gcd(X, Y)$):
   $$Z \pmod{\gcd(X, Y)} = 0$$

If either condition is violated, the program stops immediately and informs the user that no solution exists.

---

## 4. Approach and Implementation

### State Representation
Each state is represented as a tuple of two integers:
$$\text{State} = (\text{jug1\_amount}, \text{jug2\_amount})$$
- Initial State: $(0, 0)$
- Goal State: Any state $(j_1, j_2)$ such that $j_1 = Z$ or $j_2 = Z$.

### Transition Rules
From state $(j_1, j_2)$:
| Operation | Precondition | Next State |
| :--- | :--- | :--- |
| **Fill Jug 1** | $j_1 < X$ | $(X, j_2)$ |
| **Fill Jug 2** | $j_2 < Y$ | $(j_1, Y)$ |
| **Empty Jug 1** | $j_1 > 0$ | $(0, j_2)$ |
| **Empty Jug 2** | $j_2 > 0$ | $(j_1, 0)$ |
| **Pour 1 $\to$ 2** | $j_1 > 0 \land j_2 < Y$ | Let $p = \min(j_1, Y - j_2) \implies (j_1 - p, j_2 + p)$ |
| **Pour 2 $\to$ 1** | $j_2 > 0 \land j_1 < X$ | Let $p = \min(j_2, X - j_1) \implies (j_1 + p, j_2 - p)$ |

### Main Functions
1. `is_solvable(cap1, cap2, target)`: Verifies capacity bounds and $\gcd$ divisibility.
2. `solve_water_jug_bfs(cap1, cap2, target)`: Uses a `collections.deque` queue to explore states breadth-first. Stores current state and the accumulated path of actions.
3. `print_solution(cap1, cap2, target, solution)`: Formats and displays the step-by-step path cleanly in a structured table.
4. `get_user_inputs()`: Safely reads user inputs from interactive prompts or command-line arguments.

---

## 5. How to Run

Navigate to the `Problem 1` directory and execute:

### Interactive Mode:
```bash
python water_jug.py
```
You will be prompted to enter Jug 1 capacity, Jug 2 capacity, and the target volume.

### Command-Line Arguments Mode:
You can also supply the values directly as arguments:
```bash
python water_jug.py 4 3 2
```
Syntax: `python water_jug.py <cap1> <cap2> <target>`

---

## 6. Sample Input

```text
Jug 1 Capacity: 4
Jug 2 Capacity: 3
Target Volume: 2
```

---

## 7. Sample Output

```text
Checking solvability for Jug 1 = 4L, Jug 2 = 3L, Target = 2L...
Problem is mathematically solvable! Searching for optimal path using BFS...

======================================================================
                    WATER JUG PROBLEM SOLUTION
======================================================================
Configuration : Jug 1 Capacity = 4L | Jug 2 Capacity = 3L
Target Volume : 2L
----------------------------------------------------------------------
Step   | Action Performed                           | Jug 1   | Jug 2  
----------------------------------------------------------------------
0      | Initial State (Both jugs empty)            | 0    L | 0    L
1      | Fill Jug 2 completely to 3L                | 0    L | 3    L
2      | Pour 3L from Jug 2 into Jug 1              | 3    L | 0    L
3      | Fill Jug 2 completely to 3L                | 3    L | 3    L
4      | Pour 1L from Jug 2 into Jug 1              | 4    L | 2    L
----------------------------------------------------------------------
SUCCESS: Target 2L reached in Jug 2 at Step 4!
======================================================================
```

### Unsolvable Example Output (`cap1 = 6, cap2 = 4, target = 3`):
```text
Checking solvability for Jug 1 = 6L, Jug 2 = 4L, Target = 3L...

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
CANNOT BE SOLVED:
Reason: Target (3L) is not a multiple of GCD(6, 4) = 2. By Bezout's identity, no solution exists.
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
```

---

## 8. Code Explanation

- **`deque` for BFS Queue**: Standard Python lists have $O(n)$ time complexity for popping from the front (`pop(0)`). Using `collections.deque` allows $O(1)$ amortized `popleft()` operations, making state exploration efficient.
- **Visited Set**: The `visited` hash set stores tuples `(j1, j2)`. Hash table lookups take $O(1)$ time on average. Any state generated that is already in `visited` is skipped immediately, preventing cycles and infinite loops.
- **Path Storage**: Each queue item holds `(current_state, path)`. When the target condition is met, the path contains the exact sequence of actions taken from the start, preserving full step-by-step history without requiring backtracking or separate parent pointers.
- **Pour Calculation**: `min(j1, cap2 - j2)` calculates the exact amount of water that can be transferred. This cleanly covers both scenarios: either the source jug empties completely or the destination jug fills to capacity.

---

## 9. Time and Space Complexity

- **State Space Size**: The maximum number of distinct configurations of the two jugs is $(X + 1) \times (Y + 1)$, where $X$ is the capacity of Jug 1 and $Y$ is the capacity of Jug 2.
- **Time Complexity**: $\mathcal{O}(X \times Y)$
  In the worst case, BFS visits every reachable state once. For each state, 6 constant-time transitions are evaluated.
- **Space Complexity**: $\mathcal{O}(X \times Y)$
  The `visited` set and the BFS queue can store at most $(X + 1) \times (Y + 1)$ states in memory.

---

## 10. Viva Preparation

### Q1: Why do we use BFS instead of DFS for the Water Jug problem?
**Answer**: BFS explores the state space level-by-level, ensuring that the first time a goal state is discovered, it is reached in the **minimum number of steps** (shortest path). In contrast, DFS might dive deep into long, non-optimal cycles and requires a depth limit to avoid infinite recursion.

### Q2: What is the mathematical condition for a Water Jug problem to have a solution?
**Answer**: According to Bezout's Identity, a target $Z$ can be measured if and only if:
1. $Z \le \max(X, Y)$ (the target does not exceed the largest jug's capacity).
2. $Z \pmod{\gcd(X, Y)} = 0$ ($Z$ is an exact integer multiple of the greatest common divisor of the capacities).

### Q3: How do we prevent infinite loops during state exploration?
**Answer**: We maintain a `visited` set containing all explored states `(j1, j2)`. Before pushing any newly generated state into the queue, we check whether it already exists in `visited`. If so, it is discarded.

### Q4: What is the state representation used here?
**Answer**: An ordered pair/tuple `(jug1_amount, jug2_amount)`, representing the current quantity of water in Jug 1 and Jug 2 respectively.

### Q5: How many operations can be performed from any given state?
**Answer**: There are at most 6 operations:
1. Fill Jug 1
2. Fill Jug 2
3. Empty Jug 1
4. Empty Jug 2
5. Pour Jug 1 into Jug 2
6. Pour Jug 2 into Jug 1
