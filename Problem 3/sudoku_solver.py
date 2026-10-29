"""
Problem 3: Basic Sudoku Solver (9x9)
Artificial Intelligence Lab - Lab Test 1

Description:
Solves a 9x9 Sudoku puzzle using recursive Backtracking.
Checks row, column, and 3x3 subgrid constraints to find a valid assignment
without altering any of the initial clues.
"""

import sys
from typing import Optional, List, Tuple


# A classic solvable sample Sudoku puzzle
SAMPLE_PUZZLE = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

# A known unsolvable puzzle (initial configuration is valid, but no complete solution exists)
UNSOLVABLE_PUZZLE = [
    [5, 1, 6, 8, 4, 9, 7, 3, 2],
    [3, 0, 7, 6, 0, 5, 0, 0, 0],
    [8, 0, 9, 7, 0, 0, 0, 6, 5],
    [1, 3, 5, 0, 6, 0, 9, 0, 7],
    [4, 7, 2, 5, 9, 1, 0, 0, 6],
    [9, 6, 8, 3, 7, 0, 0, 5, 0],
    [2, 5, 3, 1, 8, 6, 0, 7, 4],
    [6, 8, 4, 2, 0, 7, 5, 0, 0],
    [7, 9, 1, 0, 5, 0, 6, 0, 8],
]


def print_grid(grid: List[List[int]]) -> None:
    """
    Prints the 9x9 Sudoku grid with clear subgrid borders.
    Empty cells (0) are displayed as dots ('.') for improved readability.
    """
    horizontal_border = "+-------+-------+-------+"
    print(horizontal_border)
    for r in range(9):
        row_str = "| "
        for c in range(9):
            val = str(grid[r][c]) if grid[r][c] != 0 else "."
            row_str += val + " "
            if (c + 1) % 3 == 0:
                row_str += "| "
        print(row_str)
        if (r + 1) % 3 == 0:
            print(horizontal_border)


def find_empty_cell(grid: List[List[int]]) -> Optional[Tuple[int, int]]:
    """
    Finds an unassigned empty cell (denoted by 0) in the grid.
    Returns (row, col) tuple if found, or None if all cells are filled.
    """
    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0:
                return (r, c)
    return None


def is_valid(grid: List[List[int]], row: int, col: int, num: int) -> bool:
    """
    Checks if placing 'num' at grid[row][col] satisfies all 3 Sudoku constraints:
    1. Row constraint: 'num' must not appear elsewhere in the same row.
    2. Column constraint: 'num' must not appear elsewhere in the same column.
    3. 3x3 Subgrid constraint: 'num' must not appear in the 3x3 box containing (row, col).
    """
    # 1. Check Row
    for c in range(9):
        if c != col and grid[row][c] == num:
            return False

    # 2. Check Column
    for r in range(9):
        if r != row and grid[r][col] == num:
            return False

    # 3. Check 3x3 Subgrid
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if (r != row or c != col) and grid[r][c] == num:
                return False

    return True


def validate_initial_grid(grid: List[List[int]]) -> Tuple[bool, str]:
    """
    Validates that the initial grid:
    1. Has exactly 9 rows.
    2. Each row has exactly 9 columns.
    3. All elements are integers between 0 and 9.
    4. Initial non-zero clues do not violate row, column, or subgrid constraints.
    """
    if len(grid) != 9:
        return False, f"Grid must have exactly 9 rows, but got {len(grid)} rows."

    for r_idx, row in enumerate(grid):
        if len(row) != 9:
            return False, f"Row {r_idx + 1} must have exactly 9 cells, but got {len(row)}."
        for c_idx, val in enumerate(row):
            if not isinstance(val, int) or val < 0 or val > 9:
                return False, f"Invalid value '{val}' at cell ({r_idx + 1}, {c_idx + 1}). Values must be digits 0-9."

    # Check for duplicate clues in rows, columns, and 3x3 subgrids
    for r in range(9):
        for c in range(9):
            val = grid[r][c]
            if val != 0:
                # Temporarily check if val violates constraints with respect to other cells
                if not is_valid(grid, r, c, val):
                    return False, f"Initial clue conflict: digit {val} at Row {r + 1}, Col {c + 1} violates Sudoku rules."

    return True, "Valid grid"


def solve_sudoku(grid: List[List[int]]) -> bool:
    """
    Solves the Sudoku puzzle using recursive Backtracking.
    
    Algorithm:
    1. Find an empty cell (0). If none exist, the puzzle is solved.
    2. Try assigning digits 1 through 9 to the cell.
    3. For each digit, check if it satisfies all 3 constraints using is_valid().
    4. If valid, recursively attempt to solve the remaining puzzle.
    5. If the recursive call succeeds, return True.
    6. If placing the digit leads to a dead end, reset the cell to 0 (backtrack)
       and try the next candidate digit.
    7. If all digits 1-9 fail, return False to trigger backtracking in the caller.
    """
    empty = find_empty_cell(grid)
    if empty is None:
        return True  # All cells filled successfully!

    row, col = empty

    for num in range(1, 10):
        if is_valid(grid, row, col, num):
            grid[row][col] = num  # Tentatively place candidate number

            if solve_sudoku(grid):  # Recurse
                return True

            grid[row][col] = 0  # Undo assignment (Backtrack)

    return False  # No candidate digit worked


def parse_row(row_str: str, row_num: int) -> List[int]:
    """
    Parses a string of 9 digits separated by spaces, commas, or consecutive numbers.
    """
    row_str = row_str.strip()
    # Check for consecutive digits without spaces: e.g. "530070000"
    if len(row_str) == 9 and row_str.isdigit():
        return [int(ch) for ch in row_str]

    # Otherwise split by commas or spaces
    tokens = row_str.replace(",", " ").split()
    if len(tokens) != 9:
        raise ValueError(f"Expected 9 numbers for Row {row_num}, but received {len(tokens)}.")

    digits = []
    for token in tokens:
        if not token.isdigit():
            raise ValueError(f"Invalid character '{token}'. Only numbers 0-9 are allowed.")
        val = int(token)
        if val < 0 or val > 9:
            raise ValueError(f"Value '{val}' out of range. Must be between 0 and 9.")
        digits.append(val)
    return digits


def get_user_puzzle() -> List[List[int]]:
    """
    Offers an interactive menu to choose a sample puzzle, enter a custom puzzle,
    or test an unsolvable configuration.
    """
    if len(sys.argv) > 1:
        arg = sys.argv[1].lower()
        if arg in ("--sample", "sample", "1"):
            return [row[:] for row in SAMPLE_PUZZLE]
        elif arg in ("--unsolvable", "unsolvable", "3"):
            return [row[:] for row in UNSOLVABLE_PUZZLE]

    print("=" * 60)
    print("               9x9 SUDOKU SOLVER (BACKTRACKING)")
    print("=" * 60)
    print("Select an option:")
    print("  1. Load standard sample puzzle (Recommended for quick testing)")
    print("  2. Enter custom 9x9 puzzle row by row (0 for empty cells)")
    print("  3. Load an unsolvable test puzzle")
    print("-" * 60)

    try:
        choice = input("Enter choice (1, 2, or 3) [Default: 1]: ").strip()
    except (KeyboardInterrupt, EOFError):
        print("\nExiting.")
        sys.exit(0)

    if choice == "2":
        print("\nEnter 9 rows. For each row, provide 9 digits (0 for empty cell).")
        print("Example row format: 5 3 0 0 7 0 0 0 0  or  530070000\n")
        custom_grid = []
        r = 1
        while r <= 9:
            try:
                line = input(f"Enter Row {r}: ")
                parsed = parse_row(line, r)
                custom_grid.append(parsed)
                r += 1
            except ValueError as err:
                print(f"  Error: {err} Please re-enter Row {r}.")
            except (KeyboardInterrupt, EOFError):
                print("\nInput cancelled.")
                sys.exit(0)
        return custom_grid
    elif choice == "3":
        print("Loaded unsolvable test puzzle.")
        return [row[:] for row in UNSOLVABLE_PUZZLE]
    else:
        print("Loaded standard sample puzzle.")
        return [row[:] for row in SAMPLE_PUZZLE]


def main():
    puzzle = get_user_puzzle()

    print("\n--- INITIAL SUDOKU PUZZLE ---")
    print_grid(puzzle)

    # Validate puzzle integrity
    is_valid_grid, message = validate_initial_grid(puzzle)
    if not is_valid_grid:
        print("\n" + "!" * 60)
        print("INVALID PUZZLE INPUT:")
        print(f"Error: {message}")
        print("!" * 60 + "\n")
        return

    # Keep a deep copy of original puzzle to ensure clues are preserved
    original_puzzle = [row[:] for row in puzzle]

    print("\nSolving puzzle using Backtracking Search...")
    solved = solve_sudoku(puzzle)

    if solved:
        # Verify that original clues remain unmodified
        for r in range(9):
            for c in range(9):
                if original_puzzle[r][c] != 0:
                    assert original_puzzle[r][c] == puzzle[r][c], "Original clue was altered!"

        print("\n--- SOLVED SUDOKU PUZZLE ---")
        print_grid(puzzle)
        print("\nSUCCESS: Puzzle solved successfully! All constraints satisfied.\n")
    else:
        print("\n" + "!" * 60)
        print("NO SOLUTION FOUND: This Sudoku puzzle cannot be solved.")
        print("!" * 60 + "\n")


if __name__ == "__main__":
    main()
