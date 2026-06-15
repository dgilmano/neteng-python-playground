"""
Task 20: join() with newline

Use Case:
Generated CLI commands are often stored as a list and later rendered as a multiline config block.
Join the commands with newline characters without adding an extra blank line at the end.

Assignment:
Join CLI commands with newline - convert the command list into one multiline string.

Steps:
1. Inspect the input data.
2. Use '\n' as the separator.
3. Join all commands into a single string.
4. Return the multiline string from solve(data).

Expected result:
- 'interface Gi0/1\ndescription WAN\nno shutdown'
"""

# Task: join() with newline

data = ['interface Gi0/1', 'description WAN', 'no shutdown']

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
    result = ''
    for index, command in enumerate(data):
        if index > 0:
            result += '\n'
        result += command
    return result

--- Option 2: join() ---
def solve_join(data):
    return '\n'.join(data)
"""
