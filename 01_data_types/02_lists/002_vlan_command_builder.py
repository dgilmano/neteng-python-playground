"""
Task 2: VLAN command builder

Use Case:
Change scripts often turn a list of VLAN IDs into a list of CLI commands.
Build one normalized VLAN command for each VLAN ID.

Rules:
1. Create a variable `commands` as an empty list.
2. Create a loop that iterates over VLAN IDs in the original order:
   for vlan_id in data:
3. Inside the loop, convert the current VLAN ID to a string using `str()`.
4. Format the VLAN string as 4 characters using the `zfill(4)` method.
5. Store the formatted VLAN string in a variable such as `vlan_text`.
6. Build a command in the form:
   "vlan " + vlan_text
7. Append the command to the `commands` list using `commands.append()`.
8. Do not sort or reorder VLAN IDs.
9. Return the `commands` list.

Expected result:
- ['vlan 0010', 'vlan 0020', 'vlan 0030', 'vlan 0100']
"""

# Task: vlan command builder

data = [10, 20, 30, 100]


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
    commands = []

    for vlan_id in data:
        vlan_text = str(vlan_id).zfill(4)
        commands.append('vlan ' + vlan_text)

    return commands
"""
