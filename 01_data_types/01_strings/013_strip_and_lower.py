"""
Task 13: strip() + lower()

Use Case:
Device names may come from inventory files, CLI output, or user input with extra spaces and inconsistent capitalization.
Normalize the hostname before using it as a key, label, or comparison value.

Assignment:
Normalize device hostname - convert '  NYC-R1  ' to 'nyc-r1'.

Steps:
1. Inspect the input data.
2. Remove leading and trailing spaces with .strip().
3. Convert the hostname to lowercase with .lower().
4. Return the result from solve(data).

Expected result:
- 'nyc-r1'
"""

# Task: strip() + lower()

data = '  NYC-R1  '

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
    cleaned = data.strip()
    normalized = cleaned.lower()
    return normalized

--- Option 2: method chaining ---
def solve_chain(data):
    return data.strip().lower()
"""
