"""
Problem 1: Water Jug Problem Solver
Artificial Intelligence Lab - Lab Test 1

Description:
Solves the classic Water Jug Problem for any two jug capacities and a target
volume using Breadth-First Search (BFS). BFS guarantees finding the shortest
sequence of operations to reach the target amount of water.
"""

from collections import deque
import math
import sys


def is_solvable(cap1: int, cap2: int, target: int) -> tuple[bool, str]:
    """
    Checks if a target amount of water can be measured using two jugs.
    Based on Bézout's Identity:
    1. The target cannot exceed the capacity of the largest jug.
    2. The target must be a multiple of the Greatest Common Divisor (GCD) of both capacities.
    """
    if cap1 <= 0 or cap2 <= 0:
        return False, "Jug capacities must be positive integers greater than 0."
    if target < 0:
        return False, "Target amount cannot be negative."
    if target > max(cap1, cap2):
        return False, f"Target ({target}L) cannot be greater than the maximum jug capacity ({max(cap1, cap2)}L)."
    
    gcd_val = math.gcd(cap1, cap2)
    if target % gcd_val != 0:
        return False, (
            f"Target ({target}L) is not a multiple of GCD({cap1}, {cap2}) = {gcd_val}. "
            "By Bezout's identity, no solution exists."
        )
    
    return True, "Solvable"


def solve_water_jug_bfs(cap1: int, cap2: int, target: int):
    """
    Finds the optimal sequence of moves to measure the target amount of water
    using Breadth-First Search (BFS).

    State representation: (jug1_current, jug2_current)
    Returns:
        List of steps: [(step_number, action_description, (jug1, jug2))]
        or None if no solution exists.
    """
    initial_state = (0, 0)
    
    # If the target is 0, we are already at the target
    if target == 0:
        return [(0, "Initial State (Both jugs are empty)", initial_state)]

    # Queue stores tuples of: (current_state, path_of_actions)
    # where path_of_actions is a list of (action_description, state)
    queue = deque()
    queue.append((initial_state, [("Initial State (Both jugs empty)", initial_state)]))
    
    # Visited set to prevent infinite loops and repeated states
    visited = set()
    visited.add(initial_state)

    while queue:
        (j1, j2), path = queue.popleft()

        # Check if either jug has reached the target
        if j1 == target or j2 == target:
            # Format the path with step numbers
            solution = []
            for step_num, (action, state) in enumerate(path):
                solution.append((step_num, action, state))
            return solution

        # Generate all 6 possible operations
        possible_transitions = []

        # 1. Fill Jug 1 completely
        if j1 < cap1:
            possible_transitions.append((
                f"Fill Jug 1 completely to {cap1}L",
                (cap1, j2)
            ))

        # 2. Fill Jug 2 completely
        if j2 < cap2:
            possible_transitions.append((
                f"Fill Jug 2 completely to {cap2}L",
                (j1, cap2)
            ))

        # 3. Empty Jug 1 completely
        if j1 > 0:
            possible_transitions.append((
                "Empty Jug 1 completely",
                (0, j2)
            ))

        # 4. Empty Jug 2 completely
        if j2 > 0:
            possible_transitions.append((
                "Empty Jug 2 completely",
                (j1, 0)
            ))

        # 5. Pour from Jug 1 into Jug 2 until Jug 2 is full or Jug 1 is empty
        if j1 > 0 and j2 < cap2:
            pour_amount = min(j1, cap2 - j2)
            possible_transitions.append((
                f"Pour {pour_amount}L from Jug 1 into Jug 2",
                (j1 - pour_amount, j2 + pour_amount)
            ))

        # 6. Pour from Jug 2 into Jug 1 until Jug 1 is full or Jug 2 is empty
        if j2 > 0 and j1 < cap1:
            pour_amount = min(j2, cap1 - j1)
            possible_transitions.append((
                f"Pour {pour_amount}L from Jug 2 into Jug 1",
                (j1 + pour_amount, j2 - pour_amount)
            ))

        # Explore child states
        for action, next_state in possible_transitions:
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [(action, next_state)]))

    return None


def print_solution(cap1: int, cap2: int, target: int, solution):
    """
    Prints the step-by-step solution in a clean, human-readable tabular format.
    """
    print("\n" + "=" * 70)
    print("                    WATER JUG PROBLEM SOLUTION")
    print("=" * 70)
    print(f"Configuration : Jug 1 Capacity = {cap1}L | Jug 2 Capacity = {cap2}L")
    print(f"Target Volume : {target}L")
    print("-" * 70)
    print(f"{'Step':<6} | {'Action Performed':<42} | {'Jug 1':<7} | {'Jug 2':<7}")
    print("-" * 70)

    for step_num, action, (j1, j2) in solution:
        print(f"{step_num:<6} | {action:<42} | {j1:<5}L | {j2:<5}L")

    print("-" * 70)
    final_step, _, (final_j1, final_j2) = solution[-1]
    which_jug = "Jug 1" if final_j1 == target else "Jug 2"
    print(f"SUCCESS: Target {target}L reached in {which_jug} at Step {final_step}!")
    print("=" * 70 + "\n")


def get_user_inputs():
    """
    Accepts jug capacities and target from command-line arguments or user prompt.
    """
    if len(sys.argv) == 4:
        try:
            c1 = int(sys.argv[1])
            c2 = int(sys.argv[2])
            tgt = int(sys.argv[3])
            return c1, c2, tgt
        except ValueError:
            print("Error: Command-line arguments must be valid integers.")
            sys.exit(1)

    print("=" * 50)
    print("         WATER JUG PROBLEM SOLVER (BFS)")
    print("=" * 50)

    while True:
        try:
            c1_str = input("Enter capacity of Jug 1 (litres): ").strip()
            c1 = int(c1_str)
            if c1 <= 0:
                print("Capacity must be a positive integer greater than 0.")
                continue

            c2_str = input("Enter capacity of Jug 2 (litres): ").strip()
            c2 = int(c2_str)
            if c2 <= 0:
                print("Capacity must be a positive integer greater than 0.")
                continue

            tgt_str = input("Enter target volume (litres): ").strip()
            tgt = int(tgt_str)
            if tgt < 0:
                print("Target cannot be negative.")
                continue

            return c1, c2, tgt
        except ValueError:
            print("Invalid input! Please enter valid integer values.\n")
        except (KeyboardInterrupt, EOFError):
            print("\nOperation cancelled by user.")
            sys.exit(0)


def main():
    cap1, cap2, target = get_user_inputs()

    print(f"\nChecking solvability for Jug 1 = {cap1}L, Jug 2 = {cap2}L, Target = {target}L...")
    solvable, reason = is_solvable(cap1, cap2, target)

    if not solvable:
        print("\n" + "!" * 60)
        print("CANNOT BE SOLVED:")
        print(f"Reason: {reason}")
        print("!" * 60 + "\n")
        return

    print("Problem is mathematically solvable! Searching for optimal path using BFS...")
    solution = solve_water_jug_bfs(cap1, cap2, target)

    if solution:
        print_solution(cap1, cap2, target, solution)
    else:
        print(f"\nNo solution found to reach {target}L with Jug 1 ({cap1}L) and Jug 2 ({cap2}L).\n")


if __name__ == "__main__":
    main()
