"""
Problem 2: Missionaries and Cannibals Problem Solver
Artificial Intelligence Lab - Lab Test 1

Description:
Solves the classic Missionaries and Cannibals problem using Breadth-First
Search (BFS) in state-space. Finds the optimal sequence of river crossings
while ensuring missionaries are never outnumbered by cannibals on either bank.
"""

from collections import deque


TOTAL_MISSIONARIES = 3
TOTAL_CANNIBALS = 3
BOAT_CAPACITY = 2


def is_safe(m_left: int, c_left: int) -> bool:
    """
    Checks if a state satisfies the safety and validity constraints.
    - People counts must remain between 0 and 3 on both banks.
    - Cannibals must not outnumber missionaries on any bank where missionaries are present.
    """
    # Check bounds
    if not (0 <= m_left <= TOTAL_MISSIONARIES and 0 <= c_left <= TOTAL_CANNIBALS):
        return False

    m_right = TOTAL_MISSIONARIES - m_left
    c_right = TOTAL_CANNIBALS - c_left

    # Check Left bank safety
    if m_left > 0 and c_left > m_left:
        return False

    # Check Right bank safety
    if m_right > 0 and c_right > m_right:
        return False

    return True


def get_move_description(m: int, c: int, direction: str) -> str:
    """
    Returns a human-readable description of the passengers crossing the river.
    """
    passengers = []
    if m > 0:
        passengers.append(f"{m} Missionary" if m == 1 else f"{m} Missionaries")
    if c > 0:
        passengers.append(f"{c} Cannibal" if c == 1 else f"{c} Cannibals")
    
    passenger_str = " and ".join(passengers)
    return f"Move {passenger_str} ({direction})"


def solve_missionaries_cannibals():
    """
    Finds the shortest valid crossing sequence using Breadth-First Search (BFS).

    State representation: (m_left, c_left, boat_position)
    - m_left: number of missionaries on the Left bank (0 to 3)
    - c_left: number of cannibals on the Left bank (0 to 3)
    - boat_position: 'Left' or 'Right'
    
    Returns:
        List of steps: [(step_number, action_description, state)]
    """
    # Initial State: Everyone and boat on the Left bank
    initial_state = (TOTAL_MISSIONARIES, TOTAL_CANNIBALS, "Left")
    # Goal State: Everyone and boat on the Right bank
    goal_state = (0, 0, "Right")

    # Valid boat combinations: (m_cross, c_cross) such that 1 <= m + c <= 2
    valid_boat_moves = [
        (0, 2),  # 2 Cannibals
        (0, 1),  # 1 Cannibal
        (1, 1),  # 1 Missionary and 1 Cannibal
        (2, 0),  # 2 Missionaries
        (1, 0),  # 1 Missionary
    ]

    # Queue stores: (current_state, path)
    queue = deque()
    queue.append((initial_state, [("Initial State", initial_state)]))

    # Visited set to prevent infinite loops and state cycles
    visited = set()
    visited.add(initial_state)

    while queue:
        (m_left, c_left, boat), path = queue.popleft()

        # Check if goal state is achieved
        if (m_left, c_left, boat) == goal_state:
            solution = []
            for step_num, (action, state) in enumerate(path):
                solution.append((step_num, action, state))
            return solution

        # Determine direction of travel
        if boat == "Left":
            # Moving from Left to Right
            for m_move, c_move in valid_boat_moves:
                new_m_left = m_left - m_move
                new_c_left = c_left - c_move
                new_boat = "Right"

                if is_safe(new_m_left, new_c_left):
                    next_state = (new_m_left, new_c_left, new_boat)
                    if next_state not in visited:
                        visited.add(next_state)
                        action_desc = get_move_description(m_move, c_move, "Left -> Right")
                        queue.append((next_state, path + [(action_desc, next_state)]))

        else:
            # Moving from Right to Left
            for m_move, c_move in valid_boat_moves:
                new_m_left = m_left + m_move
                new_c_left = c_left + c_move
                new_boat = "Left"

                if is_safe(new_m_left, new_c_left):
                    next_state = (new_m_left, new_c_left, new_boat)
                    if next_state not in visited:
                        visited.add(next_state)
                        action_desc = get_move_description(m_move, c_move, "Right -> Left")
                        queue.append((next_state, path + [(action_desc, next_state)]))

    return None


def print_solution(solution):
    """
    Renders the solution step-by-step with clear riverbank visuals and details.
    """
    print("\n" + "=" * 78)
    print("           MISSIONARIES AND CANNIBALS PROBLEM - OPTIMAL SOLUTION (BFS)")
    print("=" * 78)
    print("Problem Setup : 3 Missionaries, 3 Cannibals, Boat Capacity = 2")
    print("Safety Rule   : Cannibals must never outnumber Missionaries on either bank!")
    print("=" * 78)

    for step_num, action, (m_left, c_left, boat) in solution:
        m_right = TOTAL_MISSIONARIES - m_left
        c_right = TOTAL_CANNIBALS - c_left
        boat_left = "[BOAT]" if boat == "Left" else "      "
        boat_right = "[BOAT]" if boat == "Right" else "      "

        m_left_str = f"{m_left} Missionary" if m_left == 1 else f"{m_left} Missionaries"
        c_left_str = f"{c_left} Cannibal" if c_left == 1 else f"{c_left} Cannibals"
        m_right_str = f"{m_right} Missionary" if m_right == 1 else f"{m_right} Missionaries"
        c_right_str = f"{c_right} Cannibal" if c_right == 1 else f"{c_right} Cannibals"

        print(f"\nStep {step_num}: {action}")
        print("-" * 78)
        print(f"  Left Bank  : {m_left_str:<15}, {c_left_str:<13}  {boat_left}")
        print(f"  ~~~~~~~~~~~ [       R I V E R       ] ~~~~~~~~~~~")
        print(f"  Right Bank : {m_right_str:<15}, {c_right_str:<13}  {boat_right}")

    print("\n" + "=" * 78)
    print(f"SUCCESS: All 3 Missionaries and 3 Cannibals crossed the river safely in {len(solution) - 1} moves!")
    print("=" * 78 + "\n")


def main():
    print("Solving the Missionaries and Cannibals Problem using BFS...")
    solution = solve_missionaries_cannibals()

    if solution:
        print_solution(solution)
    else:
        print("No valid sequence of crossings could be found.")


if __name__ == "__main__":
    main()
