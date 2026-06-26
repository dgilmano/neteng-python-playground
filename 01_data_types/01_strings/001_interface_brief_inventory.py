"""
Task 1: Interface brief inventory

Methods to practice:
- splitlines(), strip(), split(), lower(), replace(), startswith()

Use Case:
Parse CLI table output from "show ip interface brief" into structured data.
Keep only physical interfaces, shorten interface names, normalize statuses to lowercase, and return a list of dictionaries.

Rules:
1. Create a variable `result` as an empty list.
2. Create a loop using the `splitlines()` method to split the input string into separate lines and iterate through each line.
3. Inside the loop, apply the `strip()` method to remove leading and trailing spaces from each line.
4. Skip empty lines using:
   if not line:
       continue
5. Skip the header line that starts with "Interface" using:
   if line.startswith("Interface"):
       continue
6. Split the current line into columns using the `split()` method and store the result in a new variable.
7. Skip invalid rows that contain fewer than 4 columns.
8. Extract the interface name from the first column.
9. Skip Loopback interfaces using:
   if interface.startswith("Loopback"):
       continue
10. Replace long interface names with their short forms using the `replace()` method:
    - GigabitEthernet → Gi
    - FastEthernet → Fa
11. Convert the line status and protocol status to lowercase using the `lower()` method.
12. Create a dictionary with the parsed interface information and append it to the `result` list using `result.append()`.
13. Return the `result` list.

Expected result:
- [
    {'interface': 'Gi0/1', 'ip': '192.168.1.10', 'line_status': 'up', 'protocol_status': 'up'},
    {'interface': 'Gi0/2', 'ip': 'unassigned', 'line_status': 'down', 'protocol_status': 'down'},
    {'interface': 'Fa0/3', 'ip': '10.0.0.1', 'line_status': 'up', 'protocol_status': 'down'},
  ]
"""

# Task: interface brief inventory
# Input: multiline CLI output

data = """
Interface              IP-Address      Status Protocol
GigabitEthernet0/1     192.168.1.10    UP     UP
GigabitEthernet0/2     unassigned      down   DOWN
Loopback0              10.255.255.1    up     up
FastEthernet0/3        10.0.0.1        Up     Down
"""

def solve(data):
    result = []
    for line in data.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith("Interface"):
            continue
        if line.startswith("Loopback"):
            continue
        column = line.split()
        if len(column) < 4:
            continue
        interface_name = column[0]
        interface_name = interface_name.replace("GigabitEthernet", "Gi").replace("FastEthernet", 'Fa')
        result.append(
            {
                'interface': interface_name,
                'ip': column[1],
                'line_status': column[2].lower(),
                'protocol_status': column[3].lower()
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
        if line.startswith('Interface'):
            continue

        columns = line.split()
        if len(columns) < 4:
            continue

        interface = columns[0]
        if interface.startswith('Loopback'):
            continue

        interface = interface.replace('GigabitEthernet', 'Gi')
        interface = interface.replace('FastEthernet', 'Fa')

        result.append({
            'interface': interface,
            'ip': columns[1],
            'line_status': columns[2].lower(),
            'protocol_status': columns[3].lower(),
        })

    return result
"""
