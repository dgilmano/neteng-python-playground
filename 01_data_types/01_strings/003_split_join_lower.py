"""
Task 3: split() + join() + lower()

Use Case:
CLI output and configuration snippets often contain inconsistent spacing and capitalization.
Normalize a line before comparing it with an expected config line.

Assignment:
Normalize interface config line - convert '  Interface   Gi0/1   UP  ' to 'interface gi0/1 up'.

Steps:
1. Inspect the input data.
2. Split the string into words with .split().
3. Join the words back with a single space.
4. Convert the result to lowercase.
5. Return the normalized line from solve(data).

Expected result:
- 'interface gi0/1 up'
"""

# Task: split() + join() + lower()

data = '  Interface   Gi0/1   UP  '

def solve(data):
    raise NotImplementedError("Write your solution here")

if __name__ == "__main__":
    try:
        print(solve(data))
    except NotImplementedError:
        print("<NotImplementedError: implement solve(data)>")
    print("# Check against Expected result above.")

# =============================================================================
# Example Solution
# =============================================================================
"""
--- Option 1: step by step ---
def solve_steps(data):
    words = data.strip().split()
    line = ' '.join(words)
    return line.lower()

--- Option 2: compact chain ---
def solve_compact(data):
    return ' '.join(data.split()).lower()
"""
