"""
Task 12: partition()

Use Case:
Network output often contains key-value text fields, such as description: WAN uplink.
Use partition() when you want to split a string once and keep the text after a separator.

Assignment:
Extract value after colon with partition() - convert 'description: WAN uplink' to 'WAN uplink'.

Steps:
1. Inspect the input data.
2. Use .partition(':') to split the string into before, separator, and after parts.
3. Remove extra spaces from the value with .strip().
4. Return the cleaned value from solve(data).

Expected result:
- 'WAN uplink'
"""

# Task: partition()

data = 'description: WAN uplink'

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
--- Option 1: partition() + named variables ---
def solve_partition(data):
    key, sep, value = data.partition(':')
    return value.strip()

--- Option 2: partition() + index ---
def solve_index(data):
    return data.partition(':')[2].strip()
"""
