# Problem 2: Missionaries and Cannibals Problem

## 1. Problem Statement

The Missionaries and Cannibals problem is a renowned river-crossing problem in Artificial Intelligence used to study state-space representation, constraint satisfaction, and uninformed search algorithms.

### Setting:
- Three missionaries and three cannibals are on the **Left bank** (starting bank) of a river.
- They must all cross to the **Right bank** (destination bank) using a small boat.
- The boat can carry a maximum of **two people** at a time and requires at least **one person** on board to row it.

### Core Constraint (Safety Rule):
At no point on either riverbank may the **cannibals outnumber the missionaries** if there is at least one missionary present on that bank:
- If missionaries are present on a bank ($M > 0$), we must have $M \ge C$.
- If there are zero missionaries on a bank ($M = 0$), any number of cannibals can be safely present there without endangering anyone.

The puzzle is solved when all three missionaries and all three cannibals are safely on the Right bank.

---

## 2. Objective

The Python program aims to:
- Formulate the problem as a formal state-space search problem.
- Model valid state transitions corresponding to legal boat crossings.
- Implement **Breadth-First Search (BFS)** to find the shortest (optimal) sequence of safe crossings.
- Ensure all intermediate states strictly adhere to safety constraints.
- Display each step clearly with step numbers, the number of passengers crossing, the direction of the boat, and the count of missionaries and cannibals on both banks.
- Confirm successful completion once the goal state is reached.

---

## 3. Algorithm Used: Breadth-First Search (BFS)

### Why BFS for River-Crossing Problems?
1. **Shortest Path Guarantee**: Because every boat crossing has an equal cost of 1 unit, BFS is guaranteed to discover the optimal solution requiring the minimum number of crossings.
2. **Cycle Prevention**: The state space contains cycles (e.g., sending people across and immediately bringing them right back). Maintaining a `visited` set ensures the search never explores the same state twice.
3. **Avoids Deep Traps**: Unlike Depth-First Search (DFS), BFS will not plunge down an infinite branch or get trapped in repetitive cycles.

---

## 4. Approach and Implementation

### State Representation
A state is represented as a 3-tuple:
$$\text{State} = (M_{\text{left}}, C_{\text{left}}, \text{Boat})$$
- $M_{\text{left}} \in \{0, 1, 2, 3\}$: Number of missionaries on the Left bank.
- $C_{\text{left}} \in \{0, 1, 2, 3\}$: Number of cannibals on the Left bank.
- $\text{Boat} \in \{\text{'Left'}, \text{'Right'}\}$: Current location of the boat.

The population on the Right bank is derived directly from the invariant:
$$M_{\text{right}} = 3 - M_{\text{left}}$$
$$C_{\text{right}} = 3 - C_{\text{left}}$$

### Initial and Goal States
- **Initial State**: $(3, 3, \text{'Left'})$ — Everyone and the boat are on the starting bank.
- **Goal State**: $(0, 0, \text{'Right'})$ — Everyone and the boat have crossed to the destination bank.

### Legal Boat Moves
The boat can carry 1 or 2 passengers. The allowable passenger combinations $(m, c)$ are:
1. $(0, 2)$ — 2 Cannibals
2. $(0, 1)$ — 1 Cannibal
3. $(1, 1)$ — 1 Missionary and 1 Cannibal
4. $(2, 0)$ — 2 Missionaries
5. $(1, 0)$ — 1 Missionary

### State Validity Function (`is_safe`)
A state $(M_{\text{left}}, C_{\text{left}})$ is considered valid if and only if:
1. **Capacity Boundaries**:
   $$0 \le M_{\text{left}} \le 3 \quad \text{and} \quad 0 \le C_{\text{left}} \le 3$$
2. **Left Bank Safety**:
   $$\text{If } M_{\text{left}} > 0 \implies M_{\text{left}} \ge C_{\text{left}}$$
3. **Right Bank Safety**:
   $$\text{If } (3 - M_{\text{left}}) > 0 \implies (3 - M_{\text{left}}) \ge (3 - C_{\text{left}})$$

---

## 5. How to Run

Navigate to the `Problem 2` directory and execute:

```bash
python missionaries_cannibals.py
```

No external dependencies are required. The script runs using standard Python 3.

---

## 6. Sample Input

This is a deterministic puzzle with fixed initial parameters (3 Missionaries, 3 Cannibals, Boat Capacity = 2). The program executes autonomously without needing external configuration input.

---

## 7. Sample Output

```text
Solving the Missionaries and Cannibals Problem using BFS...

==============================================================================
           MISSIONARIES AND CANNIBALS PROBLEM - OPTIMAL SOLUTION (BFS)
==============================================================================
Problem Setup : 3 Missionaries, 3 Cannibals, Boat Capacity = 2
Safety Rule   : Cannibals must never outnumber Missionaries on either bank!
==============================================================================

Step 0: Initial State
------------------------------------------------------------------------------
  Left Bank  : 3 Missionaries , 3 Cannibals    [BOAT]
  ~~~~~~~~~~~ [       R I V E R       ] ~~~~~~~~~~~
  Right Bank : 0 Missionaries , 0 Cannibals          

Step 1: Move 2 Cannibals (Left -> Right)
------------------------------------------------------------------------------
  Left Bank  : 3 Missionaries , 1 Cannibal           
  ~~~~~~~~~~~ [       R I V E R       ] ~~~~~~~~~~~
  Right Bank : 0 Missionaries , 2 Cannibals    [BOAT]

Step 2: Move 1 Cannibal (Right -> Left)
------------------------------------------------------------------------------
  Left Bank  : 3 Missionaries , 2 Cannibals    [BOAT]
  ~~~~~~~~~~~ [       R I V E R       ] ~~~~~~~~~~~
  Right Bank : 0 Missionaries , 1 Cannibal           

Step 3: Move 2 Cannibals (Left -> Right)
------------------------------------------------------------------------------
  Left Bank  : 3 Missionaries , 0 Cannibals          
  ~~~~~~~~~~~ [       R I V E R       ] ~~~~~~~~~~~
  Right Bank : 0 Missionaries , 3 Cannibals    [BOAT]

Step 4: Move 1 Cannibal (Right -> Left)
------------------------------------------------------------------------------
  Left Bank  : 3 Missionaries , 1 Cannibal     [BOAT]
  ~~~~~~~~~~~ [       R I V E R       ] ~~~~~~~~~~~
  Right Bank : 0 Missionaries , 2 Cannibals          

Step 5: Move 2 Missionaries (Left -> Right)
------------------------------------------------------------------------------
  Left Bank  : 1 Missionary   , 1 Cannibal           
  ~~~~~~~~~~~ [       R I V E R       ] ~~~~~~~~~~~
  Right Bank : 2 Missionaries , 2 Cannibals    [BOAT]

Step 6: Move 1 Missionary and 1 Cannibal (Right -> Left)
------------------------------------------------------------------------------
  Left Bank  : 2 Missionaries , 2 Cannibals    [BOAT]
  ~~~~~~~~~~~ [       R I V E R       ] ~~~~~~~~~~~
  Right Bank : 1 Missionary   , 1 Cannibal           

Step 7: Move 2 Missionaries (Left -> Right)
------------------------------------------------------------------------------
  Left Bank  : 0 Missionaries , 2 Cannibals          
  ~~~~~~~~~~~ [       R I V E R       ] ~~~~~~~~~~~
  Right Bank : 3 Missionaries , 1 Cannibal     [BOAT]

Step 8: Move 1 Cannibal (Right -> Left)
------------------------------------------------------------------------------
  Left Bank  : 0 Missionaries , 3 Cannibals    [BOAT]
  ~~~~~~~~~~~ [       R I V E R       ] ~~~~~~~~~~~
  Right Bank : 3 Missionaries , 0 Cannibals          

Step 9: Move 2 Cannibals (Left -> Right)
------------------------------------------------------------------------------
  Left Bank  : 0 Missionaries , 1 Cannibal           
  ~~~~~~~~~~~ [       R I V E R       ] ~~~~~~~~~~~
  Right Bank : 3 Missionaries , 2 Cannibals    [BOAT]

Step 10: Move 1 Cannibal (Right -> Left)
------------------------------------------------------------------------------
  Left Bank  : 0 Missionaries , 2 Cannibals    [BOAT]
  ~~~~~~~~~~~ [       R I V E R       ] ~~~~~~~~~~~
  Right Bank : 3 Missionaries , 1 Cannibal           

Step 11: Move 2 Cannibals (Left -> Right)
------------------------------------------------------------------------------
  Left Bank  : 0 Missionaries , 0 Cannibals          
  ~~~~~~~~~~~ [       R I V E R       ] ~~~~~~~~~~~
  Right Bank : 3 Missionaries , 3 Cannibals    [BOAT]

==============================================================================
SUCCESS: All 3 Missionaries and 3 Cannibals crossed the river safely in 11 moves!
==============================================================================
```

---

## 8. Code Explanation

- **`is_safe(m_left, c_left)`**: Checks whether any constraints are broken. Notice that `m_right` and `c_right` are calculated dynamically. The rule `if m > 0 and c > m: return False` is checked independently for both the Left bank and the Right bank.
- **Direction Handling**: When `boat == 'Left'`, people subtract from the Left bank. When `boat == 'Right'`, people return to the Left bank, so people add to the Left bank.
- **`visited` Hash Set**: We store tuples `(m_left, c_left, boat)`. If this configuration has already been explored at an earlier step or equal depth, it is skipped. This prevents cycles such as the boat moving back and forth without progress.
- **`collections.deque`**: Provides an efficient queue where popping the next shallowest state from the front runs in $O(1)$ time.

---

## 9. Time and Space Complexity

- **Total State Space**:
  - $M_{\text{left}} \in \{0, 1, 2, 3\}$ (4 possibilities)
  - $C_{\text{left}} \in \{0, 1, 2, 3\}$ (4 possibilities)
  - $\text{Boat} \in \{\text{'Left'}, \text{'Right'}\}$ (2 possibilities)
  - Total possible states = $4 \times 4 \times 2 = 32$ states.
- **Valid States**: Out of 32 possible states, only **16 states** are safe and valid.
- **Time Complexity**: $\mathcal{O}(V + E)$ where $V \le 16$ and each state has at most 5 outward transitions. Thus, the search explores the entire graph in milliseconds: $\mathcal{O}(1)$ practically.
- **Space Complexity**: $\mathcal{O}(V)$ for storing visited states and the BFS queue ($\le 32$ states), which is $\mathcal{O}(1)$ constant memory.

---

## 10. Viva Preparation

### Q1: What makes a state unsafe in this problem?
**Answer**: A state is unsafe if missionaries are outnumbered by cannibals on either the Left bank or the Right bank, provided there is at least one missionary on that bank. If a bank has 0 missionaries, it is considered safe regardless of how many cannibals are present.

### Q2: Why is the boat position necessary in the state tuple?
**Answer**: The boat position determines which direction people can move (Left to Right or Right to Left). Without including the boat in the state, the system cannot distinguish between having 3 missionaries on a bank with the boat versus without the boat.

### Q3: What is the minimum number of river crossings required to solve this problem?
**Answer**: Exactly **11 crossings** (or steps). BFS is mathematically guaranteed to find this minimum length path.

### Q4: Can 3 missionaries and 3 cannibals cross safely if the boat capacity is 1?
**Answer**: No. If the boat capacity is 1, nobody can return with the boat without stranding or outnumbering missionaries, making the problem unsolvable.

### Q5: What is the critical move in this puzzle?
**Answer**: At Step 5 and Step 7, two missionaries cross together, and at Step 6, one missionary and one cannibal return. This clever transition allows missionaries to transition across without ever leaving fewer missionaries than cannibals on either bank.
