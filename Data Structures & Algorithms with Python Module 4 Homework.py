# Data Structures & Algorithms with Python Module 4 Homework:


# You have a total of 6 exercises. 3 from Queues and 3 from Stacks :)


# QUEUE:

# 1. Reverse the first 3 elements of a queue

# TODO: Reverse only the first 3 items in the queue. Keep the rest in the same order.

# Example:
# Input queue: [1, 2, 3, 4, 5]
# Output queue: [3, 2, 1, 4, 5]

# Tips:

# Queues remove from the front (index 0).

# A stack is useful for reversing order.

# Steps idea: take 3 items off the queue -> then push to a stack -> pop from stack back to the front.

from collections import deque

def reverse_first_3(q):
    stack = []

    # Step 1: Take first 3 elements and push to stack
    for _ in range(3):
        stack.append(q.popleft())

    # Step 2: Pop from stack and enqueue back
    while stack:
        q.append(stack.pop())

    # Step 3: Move remaining elements to back
    size = len(q)
    for _ in range(size - 3):
        q.append(q.popleft())

    return q


# 2. Rolling queue (keep only last 5 numbers)

# TODO: Ask the user for numbers until they enter an empty string. Store them in a queue, but keep only the last 5 numbers entered.

# Example:
# User enters: 1, 2, 3, 4, 5, 6, 7
# Queue at the end should contain: [3, 4, 5, 6, 7]

# Tips:

# Use input() in a loop.

# When the queue grows beyond length 5, remove from the front.

# Convert input to int after checking it’s not empty.
from collections import deque

def rolling_queue():
    q = deque()

    while True:
        user_input = input("Enter a number (press Enter to stop): ")

        # Stop if empty input
        if user_input == "":
            break

        # Convert to int
        num = int(user_input)

        # Add to queue
        q.append(num)

        # Keep only last 5
        if len(q) > 5:
            q.popleft()

    print("Final queue:", list(q))





# 3. Round-robin time processing

# TODO: You have a queue of tasks. Each task is a tuple (name, time_needed).

# Each round:
# Take the front task.
# Give it 2 time units of work.
# If it still needs time, put it back to the end with updated remaining time.
# If it finishes, remove it and record its name.

# Return/print: the order in which tasks finish.

# Example:
# Tasks: [("A", 3), ("B", 6), ("C", 1)]
# Completion order (one possible expected result): ["A", "C", "B"]

# Tips:

# Use a while queue: loop.

# Subtract 2 each time you process a task.

# If remaining time is > 0, re-enqueue it.

# Otherwise, append its name to a finished list.
from collections import deque

def round_robin(tasks):
    q = deque(tasks)      # Initialize queue
    finished = []         # Completion order

    while q:
        name, time = q.popleft()

        # Give 2 time units
        time -= 2

        if time > 0:
            # Put back in queue
            q.append((name, time))
        else:
            # Task finished
            finished.append(name)

    return finished





# STACK: 


# 1. Find the minimum value in a stack

# TODO: Given a stack of numbers (a Python list), print the smallest number in it.

# Example:
# Stack: [5, 2, 9, 1, 7]
# Output: 1

# Tips:

# Python has a built-in function that finds the smallest number in a list.

# Make sure the stack is not empty before trying to find a minimum.
def find_min(stack):
    if not stack:
        print("Stack is empty. No minimum value.")
        return

    minimum = min(stack)
    print("Minimum value:", minimum)






# 2. Undo last N actions

# TODO: You have a stack of actions (strings). Undo the last n actions safely:

# Pop up to n items from the stack.

# If n is larger than the stack size, just undo what exists.

# Example:
# Actions: ["open", "edit", "save", "close"], n = 2
# Undone: ["close", "save"]
# Left in stack: ["open", "edit"]

# Tips:

# Use a for loop that runs n times.

# Before popping, check if the stack is empty.

# Store undone actions in a separate list.
def undo_actions(stack, n):
    undone = []

    for _ in range(n):
        if not stack:   # Check if stack is empty
            break

        action = stack.pop()
        undone.append(action)

    return undone, stack





# 3. Simplify a file path using a stack

# TODO: Simplify a Unix-like path:

# "." means "stay here" -> ignore it

# ".." means "go back one folder" -> pop from stack if possible

# Folder names push onto the stack
# Ignore extra slashes

# Example:
# Input: "/home//user/.././docs"
# Output: "/home/docs"

# Tips:

# Split the path by "/" to get parts.

# Skip empty parts and ".".

# On "..", pop if the stack isn’t empty.

# At the end, join the stack back into a path starting with "/".
def simplify_path(path):
    parts = path.split("/")
    stack = []

    for part in parts:

        # Ignore empty parts and "."
        if part == "" or part == ".":
            continue

        # Go back one folder
        elif part == "..":
            if stack:
                stack.pop()

        # Valid folder name
        else:
            stack.append(part)

    # Build final path
    simplified = "/" + "/".join(stack)

    return simplified



