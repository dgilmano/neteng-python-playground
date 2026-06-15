"""
Task 6: split() + isdigit() + all()

Use Case:
Automation scripts often receive IP addresses as plain strings.
Validate that the string has four numeric octets and each octet is in the IPv4 range.

Assignment:
Validate simple IPv4 string - return True for '192.168.1.10'.

Steps:
1. Inspect the input data.
2. Split the string by dots.
3. Check that there are exactly four parts.
4. Check that every part contains only digits.
5. Convert each part to int and verify that it is between 0 and 255.
6. Return the boolean result.

Expected result:
- True
"""

# Task: split() + isdigit() + all()

data = '192.168.1.10'

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
--- Option 1: explicit loop ---
def solve_loop(data):
    parts = data.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit():
            return False
        value = int(part)
        if value < 0 or value > 255:
            return False
    return True

--- Option 2: all() ---
def solve_all(data):
    parts = data.split('.')
    return len(parts) == 4 and all(part.isdigit() and 0 <= int(part) <= 255 for part in parts)
"""
