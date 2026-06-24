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
For each neighbor table line:
1. Strip spaces from both sides of the line.
2. Skip empty lines.
3. Skip the header line that starts with 'Device ID'.

Now parse one data row like this:
SW2         gi0/1        SWITCH       cisco 9300

4. Split the row into columns.
   - Use split(maxsplit=3) so the platform field can contain spaces.
5. Skip the row if it has fewer than 4 columns.
6. Read the columns in this order:
   - neighbor ID
   - local interface
   - capability
   - platform
7. Keep only neighbor IDs that are alphanumeric.
   - Example: 'SW2' is valid.
   - Example: 'bad-nei' is skipped.
8. Normalize local interface to uppercase.
   - Example: 'gi0/1' -> 'GI0/1'
9. Keep only capabilities that contain letters only.
10. Normalize capability to lowercase.
    - Example: 'SWITCH' -> 'switch'
11. Format platform with title().
    - Example: 'cisco 9300' -> 'Cisco 9300'
12. Add one dictionary to result:
    - {'neighbor': neighbor, 'local_interface': local_interface, 'capability': capability, 'platform': platform}

Step output examples:
- After steps 1-3, one kept row should look like this:
  SW2         gi0/1        SWITCH       cisco 9300
- After split(maxsplit=3), columns should look like this:
  ['SW2', 'gi0/1', 'SWITCH', 'cisco 9300']
- After normalization, one result item should look like this:
  {'neighbor': 'SW2', 'local_interface': 'GI0/1', 'capability': 'switch', 'platform': 'Cisco 9300'}

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
    result = []
    for items in data.splitlines():
        items = items.strip()
        if not items or items.startswith("Device ID"):
            continue
        data = items.split(maxsplit=3)
        if len(data) < 4:
            continue

        if not data[0].isalnum():
            continue

        if not data[2].isalpha():
            continue

        result.append(
            {
                'neighbor': data[0].upper(),
                'local_interface': data[1].upper(),
                'capability': data[2].lower(),
                'platform': data[3].title()
            }
        )
    return result


        

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
