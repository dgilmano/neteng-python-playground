"""
Task 1: split()

Use Case:
Interface addresses are stored in CIDR format.
Extract only the IP address.

Assignment:
Extract IP from CIDR string - convert '192.168.1.1/24' to '192.168.1.1'.

Steps:
1. Inspect the input data.
2. Choose a suitable method: .split() or .partition(). Try to understand the difference between them.
3. Build the result in the requested format.
4. Return the result from solve(data).

Expected result:
- '192.168.1.1'
"""

# Task: split()

data = '192.168.1.1/24'

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
--- Option 1: split() ---
def solve_split(data):
    parts = data.split('/', 1)
    return parts[0]

--- Option 2: partition() ---
def solve_partition(data):
    ip, sep, mask = data.partition('/')
    return ip
"""
