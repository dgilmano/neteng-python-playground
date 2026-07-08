"""
Task 2: VLAN command builder

Methods to practice:
- append()
- extend()
- continue
- isinstance()
- get()
- str()
- zfill()
- upper()

Use Case:
Network automation often requires generating configuration commands from structured inventory data.
Build VLAN configuration blocks from a list of VLAN records.

Rules:

1. Create an empty list called `commands`.
2. Create a loop to iterate through every VLAN record:
   for vlan in data:
3. Create variables for the fields you will use later. Use the `get()` method to safely extract values from the VLAN dictionary:
   - `vlan_id`
   - `name`
4. Skip records where `vlan_id` is not an integer.
5. Skip records where `vlan_id` is outside the valid VLAN range: `1-4094`.
6. Skip records without a VLAN name.
7. Convert `vlan_id` to a string and normalize it to 4 digits using `zfill(4)`.
8. Normalize the VLAN name using `strip()` and `upper()`.
9. Add a VLAN configuration block to `commands` using `extend()`:
   commands.extend([
       f"vlan {vlan_text}",
       f" name {name}",
       " exit",
   ])
10. Return the `commands` list.

Expected result:
[
    'vlan 0010',
    ' name DATA',
    ' exit',
    'vlan 0020',
    ' name VOICE',
    ' exit',
    'vlan 0030',
    ' name MGMT',
    ' exit',
    'vlan 0100',
    ' name SERVERS',
    ' exit'
]
"""

# Task: vlan command builder

data = [
    {'vlan_id': 10, 'name': 'DATA'},
    {'vlan_id': 20, 'name': ' voice '},
    {'vlan_id': 30, 'name': 'MGMT'},
    {'vlan_id': 100, 'name': 'servers'},
    {'vlan_id': 5000, 'name': 'INVALID'},
    {'vlan_id': 'abc', 'name': 'BROKEN'},
    {'vlan_id': 40, 'name': ''},
]


def solve(data):
    commands = []
    for item in data:
        vlan_id = item.get('vlan_id', '')
        name = item.get('name', '').strip().upper()

        if not isinstance(vlan_id, int):
            continue
        if vlan_id < 1 or vlan_id > 4094:
            continue
        if not name:
            continue
        
        vlan_text = str(vlan_id).zfill(4)
        commands.extend([
            f'vlan {vlan_text}',
            f'name {name}',
            f'exit'
        ])
    return commands


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
    commands = []
    for vlan in data:
        vlan_id = vlan.get('vlan_id')
        name = vlan.get('name', '').strip().upper()
        if not isinstance(vlan_id, int):
            continue
        if vlan_id < 1 or vlan_id > 4094:
            continue
        if not name:
            continue
        vlan_text = str(vlan_id).zfill(4)
        commands.extend([
            f"vlan {vlan_text}",
            f" name {name}",
            " exit",
        ])
    return commands
"""
