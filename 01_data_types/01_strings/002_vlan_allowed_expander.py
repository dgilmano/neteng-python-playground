"""
Task 2: VLAN allowed-list expander

Methods to practice:
- partition(), split(), strip(), replace(), isdigit(), zfill()

Use Case:
Parse a trunk allowed VLAN command into a clean expanded VLAN list.
Keep only valid numeric VLANs, expand ranges, skip invalid tokens, and return VLAN IDs as 4-character strings.

Rules:
1. Create an empty list `result`.
2. Use `partition("vlan")` to separate the VLAN part from the original string:
   prefix, separator, vlan_text = data.partition("vlan")
3. If the word `"vlan"` was not found, return an empty list:
   if not separator:
       return []
4. Remove spaces from `vlan_text`:
   vlan_text = vlan_text.replace(" ", "")
5. Split `vlan_text` by commas and iterate through each token:
   for token in vlan_text.split(","):
6. Skip empty tokens:
   if not token:
       continue
7. If the token contains `"-"`, treat it as a VLAN range.
8. Split the range into `start` and `end`, then iterate from `start` to `end` inclusive:
   start, end = token.split("-")
   for vlan_id in range(int(start), int(end) + 1):
9. Convert each VLAN ID to a string, format it with 4 digits, and append it to `result`:
   result.append(str(vlan_id).zfill(4))
10. After processing a range, use `continue` to move to the next token.
11. If the token is not a range but is a number, format it with 4 digits and append it to `result`:
   if token.isdigit():
       result.append(token.zfill(4))
12. Return the `result` list.

Expected result:
- ['0001', '0003', '0010', '0011', '0012', '0020']
"""

# Task: VLAN allowed-list expander
# Input: trunk allowed VLAN command

data = 'switchport trunk allowed vlan 1, 3,10-12,abc,20'

def solve(data):
    result = []
    vlan = data.partition("vlan")[2].strip()
    if not vlan:
        return []
    vlan_text = vlan.replace(" ", "")
    for item in vlan_text.split(","):
        if not item:
            continue
        if "-" in item:
            start, end = item.split("-")
            for vlan_id in range(int(start), int(end) + 1):
                result.append(str(vlan_id).zfill(3))
                continue
        if item.isdigit():
            result.append(str(item).zfill(3))

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
    prefix, separator, vlan_text = data.partition('vlan')
    if not separator:
        return []

    vlan_text = vlan_text.replace(' ', '')
    result = []

    for token in vlan_text.split(','):
        token = token.strip()
        if not token:
            continue

        if '-' in token:
            start, dash, end = token.partition('-')
            if start.isdigit() and end.isdigit():
                for vlan_id in range(int(start), int(end) + 1):
                    result.append(str(vlan_id).zfill(4))
            continue

        if token.isdigit():
            result.append(token.zfill(4))

    return result
"""
