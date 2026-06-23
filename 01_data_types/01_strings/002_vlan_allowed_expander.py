"""
Task 2: VLAN allowed-list expander

Methods to practice:
- partition(), split(), strip(), replace(), isdigit(), zfill()

Use Case:
Switch configuration often stores allowed VLANs as compact strings.
Automation may need a clean expanded list before comparing desired and actual state.

Assignment:
Parse a trunk allowed VLAN command and expand VLAN ranges.

Input:
- 'switchport trunk allowed vlan 1, 3,10-12,abc,20'

Rules:
1. Use partition('vlan') to separate the command prefix from the VLAN list.
2. Remove spaces from the VLAN list.
3. Split by commas.
4. Keep single numeric VLANs.
5. Expand numeric ranges like 10-12.
6. Skip invalid tokens like abc.
7. Return VLAN IDs as 4-character strings using zfill().

Step output examples:
- After partition('vlan') and removing spaces, VLAN text should look like this:
  '1,3,10-12,abc,20'
- After split(','), tokens should look like this:
  ['1', '3', '10-12', 'abc', '20']
- After expanding ranges and applying zfill(4), result should look like this:
  ['0001', '0003', '0010', '0011', '0012', '0020']

Expected result:
- ['0001', '0003', '0010', '0011', '0012', '0020']
"""

# Task: VLAN allowed-list expander

data = 'switchport trunk allowed vlan 1, 3,10-12,abc,20'

def solve(data):
    result = []
    vlan_part = data.partition('vlan')[2].strip()
    for items in vlan_part.split(','):
        items = items.strip()

        if '-' in items:
            start, end = items.split("-")
            for i in range(int(start), int(end) + 1):
                result.append(i)
        if items.isdigit():
            result.append(int(items.zfill(4)))
        
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
