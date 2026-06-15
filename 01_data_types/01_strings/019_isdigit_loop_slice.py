"""
Task 19: isdigit() + loop + slicing

Use Case:
Interface names combine a letter-based family with a numeric port path.
Split the interface into its family prefix and numeric port part.

Assignment:
Split interface name at the first digit - convert 'Gi0/12' to ('Gi', '0/12').

Steps:
1. Inspect the input data.
2. Move through the string until you find the first digit.
3. Slice the string before that index for the interface family.
4. Slice the string from that index for the port path.
5. Return both parts as a tuple.

Expected result:
- ('Gi', '0/12')
"""

# Task: isdigit() + loop + slicing

data = 'Gi0/12'

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
--- Option 1: while loop + isdigit() ---
def solve_loop(data):
    index = 0
    while index < len(data) and not data[index].isdigit():
        index += 1
    return (data[:index], data[index:])

--- Option 2: enumerate() + next() ---
def solve_next(data):
    index = next(i for i, ch in enumerate(data) if ch.isdigit())
    return (data[:index], data[index:])
"""
