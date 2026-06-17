"""
Task 6: Neighbor table parser

Methods to practice:
- splitlines(), strip(), split(), startswith(), isalnum(), isalpha(), title(), upper(), lower()

Use Case:
Neighbor discovery tables are useful for topology inventory.
The parser should clean names, validate device IDs, and normalize platform text.

Assignment:
Parse a simple neighbor table.

Input:
- multiline neighbor table

Rules:
1. Skip empty lines and the header line.
2. Split each row into columns.
3. Keep rows with at least 4 columns.
4. Keep only neighbor IDs that are alphanumeric.
5. Normalize the local interface to uppercase.
6. Keep only capabilities that contain letters only.
7. Normalize capability to lowercase.
8. Format platform with title().
9. Return a list of dictionaries.

Expected result:
- [
    {'neighbor': 'SW2', 'local_interface': 'GI0/1', 'capability': 'switch', 'platform': 'Cisco 9300'},
    {'neighbor': 'R1', 'local_interface': 'GI0/2', 'capability': 'router', 'platform': 'Cisco Isr'},
  ]
"""

# Task: neighbor table parser

data = """
Device ID   Local Intf   Capability   Platform
SW2         gi0/1        SWITCH       cisco 9300
bad-nei     gi0/9        SWITCH       cisco 2960
R1          gi0/2        ROUTER       cisco isr
"""

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
def solve(data):
    result = []

    for line in data.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith('Device ID'):
            continue

        columns = line.split(maxsplit=3)
        if len(columns) < 4:
            continue

        neighbor = columns[0]
        if not neighbor.isalnum():
            continue

        capability = columns[2]
        if not capability.isalpha():
            continue

        result.append({
            'neighbor': neighbor,
            'local_interface': columns[1].upper(),
            'capability': capability.lower(),
            'platform': columns[3].title(),
        })

    return result
"""
