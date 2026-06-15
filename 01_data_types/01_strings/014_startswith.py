"""
Task 14: startswith()

Use Case:
Network scripts often need to classify CLI commands before running them.
Check whether a command is a show command by looking at the beginning of the string.

Assignment:
Check show command prefix - return True for 'show ip interface brief'.

Steps:
1. Inspect the input data.
2. Use .startswith() to check whether the command begins with 'show '.
3. Return the boolean result.

Expected result:
- True
"""

# Task: startswith()

data = 'show ip interface brief'

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
--- Option 1: explicit if ---
def solve_if(data):
    if data.startswith('show '):
        return True
    return False

--- Option 2: direct boolean return ---
def solve_direct(data):
    return data.startswith('show ')
"""
