"""
Task 1: Interface brief inventory

Methods to practice:
- splitlines(), strip(), split(), lower(), replace(), startswith()

Use Case:
Network automation often starts by turning CLI tables into structured data.
The output may contain headers, mixed interface name formats, and mixed status case.

Assignment:
Parse a simplified "show ip interface brief" output.
Return only physical interfaces, normalize long interface names, and normalize statuses.

Input:
- multiline CLI output

Rules:
1. Skip empty lines.
2. Skip the header line that starts with "Interface".
3. Skip loopback interfaces.
4. Convert "GigabitEthernet" to "Gi" and "FastEthernet" to "Fa".
5. Convert line and protocol statuses to lowercase.
6. Keep only rows that have at least 4 columns.

Step output examples:
- After split(), one data row should look like this:
  ['GigabitEthernet0/1', '192.168.1.10', 'UP', 'UP']
- After interface and status normalization, one result item should look like this:
  {'interface': 'Gi0/1', 'ip': '192.168.1.10', 'line_status': 'up', 'protocol_status': 'up'}

Expected result:
- [
    {'interface': 'Gi0/1', 'ip': '192.168.1.10', 'line_status': 'up', 'protocol_status': 'up'},
    {'interface': 'Gi0/2', 'ip': 'unassigned', 'line_status': 'down', 'protocol_status': 'down'},
    {'interface': 'Fa0/3', 'ip': '10.0.0.1', 'line_status': 'up', 'protocol_status': 'down'},
  ]
"""

# Task: interface brief inventory

data = """
Interface              IP-Address      Status Protocol
GigabitEthernet0/1     192.168.1.10    UP     UP
GigabitEthernet0/2     unassigned      down   DOWN
Loopback0              10.255.255.1    up     up
FastEthernet0/3        10.0.0.1        Up     Down
"""

def solve(data):
    result = []
    for items in data.splitlines():
        items.strip()
        if not items or items.startswith('Interface'):
            continue
        if items.startswith("Loopback"):
            continue

        columes = items.split()
        if len(columes) < 4:
            continue

        interface = columes[0].replace("GigabitEthernet","Gi")
        interface = columes[0].replace("FastEthernet", "Fa")

        result.append({
            'interface': interface,
            'ip': columes[1],
            'line_status': columes[2],
            'protocol_status': columes[3].lower()
        })
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
