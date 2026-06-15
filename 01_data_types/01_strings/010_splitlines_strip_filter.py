"""
Task 10: splitlines() + strip() + filter

Use Case:
Configuration diffs are easier when blank lines are removed and every line is trimmed.
Convert a raw multiline string into a clean list of config lines.

Assignment:
Normalize multiline config for diff - return only non-empty stripped lines.

Steps:
1. Inspect the input data.
2. Split the string into lines with .splitlines().
3. Strip each line.
4. Skip empty lines.
5. Return the cleaned list of lines.

Expected result:
- ['interface Gi0/1', 'description WAN', 'no shutdown']
"""

# Task: splitlines() + strip() + filter

data = ' interface Gi0/1 \n\n  description WAN  \n no shutdown '

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
--- Option 1: explicit loop ---
def solve_loop(data):
    result = []
    for line in data.splitlines():
        cleaned = line.strip()
        if cleaned:
            result.append(cleaned)
    return result

--- Option 2: list comprehension ---
def solve_comprehension(data):
    return [line.strip() for line in data.splitlines() if line.strip()]
"""
