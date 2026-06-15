"""
Task 2: split(maxsplit=1)

Use Case:
Hostnames often encode site, device, and role information in a predictable format.
Extract the site code before the first dash.

Assignment:
Extract site code from hostname - convert 'nyc-r1-core' to 'nyc'.

Steps:
1. Inspect the input data.
2. Split the hostname once at the first dash.
3. Take the first part as the site code.
4. Return the site code from solve(data).

Expected result:
- 'nyc'
"""

# Task: split(maxsplit=1)

data = 'nyc-r1-core'

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
    parts = data.split('-', 1)
    return parts[0]

--- Option 2: partition() ---
def solve_partition(data):
    site, sep, rest = data.partition('-')
    return site
"""
