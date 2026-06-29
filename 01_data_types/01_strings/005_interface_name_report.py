"""
Task 5: Interface name report

Methods to practice:
- split(), strip(), replace(), rsplit(), isdigit(), zfill(), join()

Use Case:
Reports are easier to scan when interface names use one style and numbers are aligned.
Raw data may mix long and short forms.

Input:
- 'GigabitEthernet0/1, Gi0/12, FastEthernet0/3, Loopback0'

Rules:
1. Create an empty list `result`.
2. Split the input string by commas and iterate through each interface:
   for interface in data.split(","):
3. Remove leading and trailing spaces from the current interface:
   interface = interface.strip()
4. Replace long interface names with their short forms:
   - GigabitEthernet → Gi
   - FastEthernet → Fa
   interface = interface.replace("GigabitEthernet", "Gi")
   interface = interface.replace("FastEthernet", "Fa")
5. Skip invalid interface names that do not contain `/`:
   if "/" not in interface:
       continue
6. Split the interface into the prefix and interface number using `rsplit("/", 1)`:
   prefix, number = interface.rsplit("/", 1)
   Example:
   "Gi0/12"
   prefix = "Gi0"
   number = "12"
7. Check that the interface number contains only digits:
   if not number.isdigit():
       continue
8. Pad the interface number with leading zeros using `zfill(3)` and append the formatted interface to the `result` list:
   result.append(prefix + "/" + number.zfill(3))
   Example:
   prefix = "Gi0"
   number = "12"
   result.append(prefix + "/" + number.zfill(3))
   # "Gi0/012"
9. Join all formatted interface names into a single string using `", ".join()` and return the result:
   return ", ".join(result)
   Expected result:
   - 'Gi0/001, Gi0/012, Fa0/003'
"""

# Task: interface name report

data = 'GigabitEthernet0/1, Gi0/12, FastEthernet0/3, Loopback0'

def solve(data):
    result = []

    for item in data.split(','):
        item = item.strip()
        item = item.replace('GigabitEthernet', "Gi")
        item = item.replace('FastEthernet', 'Fa')
        if '/' not in item:
            continue

        prefix, number = item.rsplit('/', 1)
        if not number.isdigit():
            continue

        result.append(prefix + '/' + number.zfill(3))

    return ", ".join(result)
    

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

    for interface in data.split(','):
        interface = interface.strip()
        interface = interface.replace('GigabitEthernet', 'Gi')
        interface = interface.replace('FastEthernet', 'Fa')

        if '/' not in interface:
            continue

        prefix, number = interface.rsplit('/', 1)
        if not number.isdigit():
            continue

        result.append(prefix + '/' + number.zfill(3))

    return ', '.join(result)
"""
