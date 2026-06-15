"""
Task 17: find() + rfind() + slicing

Use Case:
Network descriptions and labels are often wrapped in quotes inside configuration text.
Extract only the quoted value without the quote characters.

Assignment:
Extract quoted description - convert 'description "WAN uplink"' to 'WAN uplink'.

Steps:
1. Inspect the input data.
2. Find the first quote character.
3. Find the last quote character.
4. Slice the string between those two positions.
5. Return the quoted description from solve(data).

Expected result:
- 'WAN uplink'
"""

# Task: find() + rfind() + slicing

data = 'description "WAN uplink"'

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
--- Option 1: find() and rfind() ---
def solve_find(data):
    start = data.find('"') + 1
    end = data.rfind('"')
    return data[start:end]

--- Option 2: split() ---
def solve_split(data):
    return data.split('"')[1]
"""
