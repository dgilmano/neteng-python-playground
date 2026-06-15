"""
Task 8: split() + star unpacking + join()

Use Case:
CLI table rows often have fixed columns followed by a free-form description.
Use star unpacking to keep the fixed fields and join the remaining words back into the description.

Assignment:
Parse interface status table row - convert 'Gi0/1 connected 10 WAN uplink' into a structured record.

Steps:
1. Inspect the input data.
2. Split the row into tokens.
3. Extract interface, status, and VLAN.
4. Capture the remaining words as the description.
5. Join the description words with spaces.
6. Return the structured record.

Expected result:
- {'interface': 'Gi0/1', 'status': 'connected', 'vlan': '10', 'description': 'WAN uplink'}
"""

# Task: split() + star unpacking + join()

data = 'Gi0/1 connected 10 WAN uplink'

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
--- Option 1: split() + indexes ---
def solve_index(data):
    tokens = data.split()
    return {
        'interface': tokens[0],
        'status': tokens[1],
        'vlan': tokens[2],
        'description': ' '.join(tokens[3:]),
    }

--- Option 2: star unpacking ---
def solve_unpack(data):
    interface, status, vlan, *description = data.split()
    return {
        'interface': interface,
        'status': status,
        'vlan': vlan,
        'description': ' '.join(description),
    }
"""
