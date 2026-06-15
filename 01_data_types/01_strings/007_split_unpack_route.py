"""
Task 7: split() + route unpacking

Use Case:
Routing output often has fixed token positions.
Extract the route code, prefix, and next hop from a simple route line.

Assignment:
Parse route line into fields - convert 'S 0.0.0.0/0 via 192.0.2.1' to ('S', '0.0.0.0/0', '192.0.2.1').

Steps:
1. Inspect the input data.
2. Split the route line into tokens.
3. Extract the route code.
4. Extract the prefix.
5. Extract the next-hop address after the word 'via'.
6. Return the fields as a tuple.

Expected result:
- ('S', '0.0.0.0/0', '192.0.2.1')
"""

# Task: split() + route unpacking

data = 'S 0.0.0.0/0 via 192.0.2.1'

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
    return (tokens[0], tokens[1], tokens[3])

--- Option 2: split() + unpacking ---
def solve_unpack(data):
    code, prefix, via, next_hop = data.split()
    return (code, prefix, next_hop)
"""
