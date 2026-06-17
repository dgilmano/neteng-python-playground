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
1. Split by commas.
2. Strip each interface name.
3. Convert long names:
   - GigabitEthernet -> Gi
   - FastEthernet -> Fa
4. For interfaces with '/', pad the last numeric part to 3 digits.
5. Skip interfaces whose last part after '/' is not numeric.
6. Join normalized interfaces with ', '.

Expected result:
- 'Gi0/001, Gi0/012, Fa0/003'
"""

# Task: interface name report

data = 'GigabitEthernet0/1, Gi0/12, FastEthernet0/3, Loopback0'

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
