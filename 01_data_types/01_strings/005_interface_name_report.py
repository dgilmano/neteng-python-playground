"""
Task 5: Interface name report

Methods to practice:
- split(), strip(), replace(), rsplit(), isdigit(), zfill(), join()

Use Case:
Reports are easier to scan when interface names use one style and numbers are aligned.
Raw data may mix long and short forms.

Assignment:
Normalize a list of interfaces and build one report string.

Input:
- 'GigabitEthernet0/1, Gi0/12, FastEthernet0/3, Loopback0'

Rules:
For each comma-separated interface name:
1. Split the input string by commas.
2. Strip spaces from both sides of the interface name.

Now parse one interface name like this:
GigabitEthernet0/1

3. Normalize long interface names:
   - replace 'GigabitEthernet' with 'Gi'
   - replace 'FastEthernet' with 'Fa'
4. Skip the interface if it does not contain '/'.
   - Example: 'Loopback0' is skipped.
5. Split the interface from the right side using rsplit('/', 1).
   - prefix is the text before the last '/'.
   - number is the text after the last '/'.
   - Example: 'Gi0/12' -> prefix 'Gi0', number '12'
6. Skip the interface if number is not numeric.
7. Pad number to 3 digits with zfill(3).
   - Example: '1' -> '001'
8. Add the normalized interface to result:
   - prefix + '/' + padded number
9. Join all normalized interfaces with ', '.

Step output examples:
- After split(','), raw items should look like this:
  ['GigabitEthernet0/1', ' Gi0/12', ' FastEthernet0/3', ' Loopback0']
- After strip() and replace(), one interface should look like this:
  'Gi0/1'
- After rsplit() and zfill(3), one normalized interface should look like this:
  'Gi0/001'

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
