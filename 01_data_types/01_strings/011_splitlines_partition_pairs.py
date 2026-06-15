"""
Task 11: splitlines() + partition()

Use Case:
Simple device facts may arrive as multiline key-value text.
Parse each non-empty line into a (key, value) pair using partition().

Assignment:
Parse key-value lines into pairs - convert the multiline text into a list of tuples.

Steps:
1. Inspect the input data.
2. Split the text into lines.
3. Ignore empty lines.
4. For each line, use .partition(':') to split key and value.
5. Strip spaces around each key and value.
6. Return the list of pairs.

Expected result:
- [('hostname', 'r1'), ('site', 'nyc'), ('role', 'core')]
"""

# Task: splitlines() + partition()

data = 'hostname: r1\nsite: nyc\nrole: core'

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
        if not line.strip():
            continue
        key, sep, value = line.partition(':')
        result.append((key.strip(), value.strip()))
    return result

--- Option 2: helper function + comprehension ---
def parse_line(line):
    key, sep, value = line.partition(':')
    return (key.strip(), value.strip())


def solve_comprehension(data):
    return [parse_line(line) for line in data.splitlines() if line.strip()]
"""
