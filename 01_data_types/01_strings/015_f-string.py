"""
Task 15: f-string

Use Case:
Network automation often builds CLI commands from structured values.
Use string formatting to create an interface description command from an interface name and description text.

Assignment:
Build interface description command - convert ('Gi0/1', 'WAN uplink') to 'interface Gi0/1 description WAN uplink'.

Steps:
1. Inspect the input data.
2. Unpack the tuple into interface and description.
3. Build the CLI command string.
4. Return the command from solve(data).

Expected result:
- 'interface Gi0/1 description WAN uplink'
"""

# Task: f-string

data = ('Gi0/1', 'WAN uplink')

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
--- Option 1: string concatenation ---
def solve_concat(data):
    interface, description = data
    return 'interface ' + interface + ' description ' + description

--- Option 2: f-string ---
def solve_fstring(data):
    interface, description = data
    return f'interface {interface} description {description}'
"""
