"""
Task 18: find() + slicing with markers

Use Case:
Logs and API responses may wrap useful configuration text between known markers.
Extract only the config block and remove surrounding whitespace.

Assignment:
Extract config block between markers - return the text between '<start>' and '<end>'.

Steps:
1. Inspect the input data.
2. Find the start marker position.
3. Add the marker length to move past '<start>'.
4. Find the end marker position.
5. Slice the string between those two positions.
6. Strip surrounding whitespace and return the config block.

Expected result:
- 'interface Gi0/1\n ip address dhcp'
"""

# Task: find() + slicing with markers

data = 'noise <start>interface Gi0/1\n ip address dhcp<end> noise'

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
--- Option 1: find() + slicing ---
def solve_find(data):
    start_marker = '<start>'
    end_marker = '<end>'
    start = data.find(start_marker) + len(start_marker)
    end = data.find(end_marker)
    return data[start:end].strip()

--- Option 2: split() twice ---
def solve_split(data):
    after_start = data.split('<start>', 1)[1]
    block = after_start.split('<end>', 1)[0]
    return block.strip()
"""
