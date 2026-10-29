# Artificial Intelligence Lab — Lab Test 1

**Course**: Artificial Intelligence Laboratory  
**Assignment**: Lab Test 1 Implementation & Viva Documentation  
**Language**: Python 3 (Standard Library)

---

## 1. Assignment Overview & Objectives

The primary objective of this laboratory assignment is to design, implement, and analyze classical Artificial Intelligence search and constraint satisfaction algorithms for three foundational problems:

1. **Problem 1: Water Jug Problem** — State-space search using Breadth-First Search (BFS) to find the shortest sequence of jug operations to measure a specified target volume, with Bezout's identity solvability validation.
2. **Problem 2: Missionaries and Cannibals Problem** — State-space search using Breadth-First Search (BFS) to safely navigate 3 missionaries and 3 cannibals across a river using a 2-person boat without violating safety constraints.
3. **Problem 3: Basic Sudoku Solver (9×9)** — Constraint Satisfaction Problem (CSP) solver using recursive Backtracking to solve standard 9×9 grids while upholding row, column, and 3×3 subgrid uniqueness rules.

Each solution is implemented with an emphasis on code readability, clear variable and state naming, error handling, and beginner-friendly logic suitable for practical lab evaluation and viva examination.

---

## 2. Directory Structure

The repository follows the exact required folder layout:

```text
Lab 1/
├── README.md                           # Main laboratory overview and execution guide
├── Problem 1/
│   ├── water_jug.py                   # Python implementation of Water Jug Problem (BFS)
│   └── README.md                      # Problem 1 documentation, algorithm, and viva prep
├── Problem 2/
│   ├── missionaries_cannibals.py      # Python implementation of Missionaries & Cannibals (BFS)
│   └── README.md                      # Problem 2 documentation, algorithm, and viva prep
└── Problem 3/
    ├── sudoku_solver.py               # Python implementation of 9x9 Sudoku Solver (Backtracking)
    └── README.md                      # Problem 3 documentation, algorithm, and viva prep
```

---

## 3. Prerequisites & Environment Setup

- **Python Version**: Python 3.8 or higher (tested with Python 3.10+).
- **External Dependencies**: **None**. All implementations rely strictly on Python's built-in standard library (`collections.deque`, `math`, `sys`, `typing`).
- **Platform**: Operating System independent (Windows, macOS, Linux).

---

## 4. Problem Summaries & Algorithms Used

| Problem | AI Paradigm | Primary Algorithm | State Representation |
| :--- | :--- | :--- | :--- |
| **1. Water Jug** | Uninformed Search | Breadth-First Search (BFS) | `(jug1_litres, jug2_litres)` |
| **2. Missionaries & Cannibals** | Uninformed Search | Breadth-First Search (BFS) | `(m_left, c_left, boat_pos)` |
| **3. Sudoku Solver (9×9)** | Constraint Satisfaction | Recursive Backtracking (DFS) | 2D list `grid[9][9]` |

### Algorithm Highlights:
- **Breadth-First Search (BFS)**:
  - Explores states level-by-level using a FIFO queue (`collections.deque`).
  - Guarantees the **shortest / optimal** path when all transitions have equal cost (1 step per action).
  - Maintains a `visited` set to detect repeated states and avoid cycles.
  - Used in Problem 1 and Problem 2.
- **Recursive Backtracking**:
  - Explores assignments depth-first.
  - Tentatively assigns a candidate digit ($1$–$9$) to an empty cell, checks local consistency (`is_valid`), and recurses.
  - If a dead end is encountered, it **undoes** the assignment (resets cell to `0`) and backtracks to try the next candidate.
  - Modifies the grid in-place to achieve $O(M)$ auxiliary stack space.
  - Used in Problem 3.

---

## 5. Instructions for Running Each Program

All commands can be executed from the terminal or command prompt.

### Problem 1: Water Jug Problem
Navigate to `Lab 1/Problem 1/` and run:
```bash
# Interactive mode (prompts for Jug 1, Jug 2 capacities and target):
python water_jug.py

# Or pass parameters via command line:
python water_jug.py 4 3 2
```

### Problem 2: Missionaries and Cannibals Problem
Navigate to `Lab 1/Problem 2/` and run:
```bash
python missionaries_cannibals.py
```

### Problem 3: Basic Sudoku Solver (9×9)
Navigate to `Lab 1/Problem 3/` and run:
```bash
# Interactive mode (menu to choose sample, custom input, or unsolvable test):
python sudoku_solver.py

# Or directly run sample / unsolvable puzzles via flags:
python sudoku_solver.py --sample
python sudoku_solver.py --unsolvable
```

---

## 6. User Inputs and Expected Outputs Summary

### Problem 1 (Water Jug):
- **Inputs**: Capacities of Jug 1, Jug 2, and Target amount (positive integers).
- **Validation**: Checks that capacities $> 0$, target $\le \max(\text{cap}_1, \text{cap}_2)$, and target is divisible by $\gcd(\text{cap}_1, \text{cap}_2)$ (Bezout's identity).
- **Output**: Step 0 initial state, followed by each numbered operation with clear action descriptions, water levels in both jugs, and final success confirmation.

### Problem 2 (Missionaries & Cannibals):
- **Inputs**: Autonomous problem formulation (3 Missionaries, 3 Cannibals, Boat Capacity 2).
- **Validation**: Strict boundary checks and safety checks ensuring cannibals never outnumber missionaries on either bank when missionaries are present.
- **Output**: River visualization showing Step 0 through Step 11, passengers on each crossing, boat direction, and headcount on both riverbanks.

### Problem 3 (Sudoku Solver):
- **Inputs**: 9 rows of 9 numbers ($0$ for empty cells), supporting space-separated, comma-separated, or consecutive 9-digit format, as well as one-press default sample loading.
- **Validation**: Grid dimensions ($9 \times 9$), integer range ($0$–$9$), and detection of conflicting initial clues.
- **Output**: Formatted initial board with $3 \times 3$ grid lines, followed by the solved board or a clear notification if the board is unsolvable.

---

## 7. Individual Problem Documentation

For detailed step-by-step algorithms, complexity analyses, verified terminal outputs, and viva preparation questions with answers, please consult the respective folder READMEs:
- [Problem 1 README](Problem%201/README.md)
- [Problem 2 README](Problem%202/README.md)
- [Problem 3 README](Problem%203/README.md)
