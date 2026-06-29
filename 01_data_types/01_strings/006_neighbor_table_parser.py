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
1. Create an empty list `result`.
2. Split the input data into lines and iterate through each line:
   for line in data.splitlines():
3. Remove leading and trailing spaces from the current line:
   line = line.strip()
4. Skip empty lines:
   if not line:
       continue
5. Skip the table header:
   if line.startswith("Device ID"):
       continue
6. Split the current line into 4 columns using `split(maxsplit=3)`:
   columns = line.split(maxsplit=3)
7. Skip invalid rows that contain fewer than 4 columns:
   if len(columns) < 4:
       continue
8. Save the neighbor name from the first column:
   neighbor = columns[0]
9. Check that the neighbor name contains only letters and digits:
   if not neighbor.isalnum():
       continue
Example:
   "SW2".isalnum()      # True
   "bad-nei".isalnum()  # False
10. Save the capability from the third column:
    capability = columns[2]
11. Check that the capability contains only letters:
    if not capability.isalpha():
        continue
Example:
   "SWITCH".isalpha()   # True
   SWITCH1".isalpha()  # False
12. Create a dictionary with the parsed information. Normalize the values using:
    - `upper()` for the local interface
    - `lower()` for the capability
    - `title()` for the platform
   result.append({
       "neighbor": neighbor,
       "local_interface": columns[1].upper(),
       "capability": capability.lower(),
       "platform": columns[3].title(),
   })
13. Return the `result` list.

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
