"""
Task 4: split() + replace()

Use Case:
Logs and command histories may contain sensitive values such as API tokens.
Mask the token value while keeping the rest of the command readable.

Assignment:
Mask sensitive token in command - convert 'api login token abc123' to 'api login token <hidden>'.

Steps:
1. Inspect the input data.
2. Find the part before the token value.
3. Replace only the sensitive value with '<hidden>'.
4. Return the masked command from solve(data).

Expected result:
- 'api login token <hidden>'
"""

# Task: split() + replace()

data = 'api login token abc123'

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
--- Option 1: split by marker ---
def solve_split(data):
    prefix = data.split('token ', 1)[0]
    return prefix + 'token <hidden>'

--- Option 2: replace known token ---
def solve_replace(data):
    return data.replace('abc123', '<hidden>')
"""
