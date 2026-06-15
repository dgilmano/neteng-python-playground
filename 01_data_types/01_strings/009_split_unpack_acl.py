"""
Task 9: split() + ACL unpacking

Use Case:
ACL lines have a predictable token layout.
Extract the action, protocol, source, destination, and destination port.

Assignment:
Parse ACL permit line - convert 'permit tcp 10.0.0.0/24 any eq 443' into a structured record.

Steps:
1. Inspect the input data.
2. Split the ACL line into tokens.
3. Extract the fixed-position fields.
4. Convert the port token to int.
5. Return the structured record.

Expected result:
- {'action': 'permit', 'protocol': 'tcp', 'source': '10.0.0.0/24', 'destination': 'any', 'port': 443}
"""

# Task: split() + ACL unpacking

data = 'permit tcp 10.0.0.0/24 any eq 443'

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
        'action': tokens[0],
        'protocol': tokens[1],
        'source': tokens[2],
        'destination': tokens[3],
        'port': int(tokens[5]),
    }

--- Option 2: split() + unpacking ---
def solve_unpack(data):
    action, protocol, source, destination, eq, port = data.split()
    return {
        'action': action,
        'protocol': protocol,
        'source': source,
        'destination': destination,
        'port': int(port),
    }
"""
