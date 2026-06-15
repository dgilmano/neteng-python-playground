"""
Task 5: split() + unpacking + int()

Use Case:
Configuration lines often contain numeric values that need to become integers before validation or comparison.
Extract the VLAN ID from a config line and convert it to int.

Assignment:
Parse VLAN id from config line - convert 'vlan 120 name USERS' to 120.

Steps:
1. Inspect the input data.
2. Split the config line into tokens.
3. Take the VLAN ID token.
4. Convert the VLAN ID to int.
5. Return the integer from solve(data).

Expected result:
- 120
"""

# Task: split() + unpacking + int()

data = 'vlan 120 name USERS'

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
--- Option 1: split() + index ---
def solve_steps(data):
    tokens = data.split()
    vlan_id = tokens[1]
    return int(vlan_id)

--- Option 2: unpacking ---
def solve_unpack(data):
    keyword, vlan_id, *_ = data.split()
    return int(vlan_id)
"""
