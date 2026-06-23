"""
Task 10: Change report builder

Methods to practice:
- splitlines(), strip(), lower(), upper(), title(), split(), rsplit(), endswith(), join()

Use Case:
Small automation scripts often turn raw change notes into a clean report.
This combines parsing, normalization, filtering, and formatting.

Assignment:
Build a compact change report from raw notes.

Input:
- multiline notes in the form '<site>|<device>|<change>|<result>'

Rules:
For each change note line:
1. Strip spaces from both sides of the line.
2. Skip empty lines.

Now parse one change note like this:
istanbul edge|sw1|vlan update CHG001|OK

3. Split the line into fields using '|'.
4. Strip spaces from each field.
5. Skip the line if it does not have exactly 4 fields.
6. Read the fields in this order:
   - site
   - device
   - change
   - result
7. Normalize result with lower().
8. Keep only lines whose result ends with 'ok'.
   - Example: 'OK' is kept.
   - Example: 'failed' is skipped.
9. Split the change field from the right side using rsplit(' ', 1).
   - action is the text before the last space.
   - ticket is the text after the last space.
   - Example: 'vlan update CHG001' -> action 'vlan update', ticket 'CHG001'
10. Format site with title().
    - Example: 'istanbul edge' -> 'Istanbul Edge'
11. Format device with upper().
    - Example: 'sw1' -> 'SW1'
12. Add one report line:
    - '<Site> / <DEVICE> / <ticket>: <action>'
13. Return all report lines joined with '\\n'.

Step output examples:
- After split('|') and strip(), one note should look like this:
  ['istanbul edge', 'sw1', 'vlan update CHG001', 'OK']
- After rsplit(' ', 1), change parts should look like this:
  action = 'vlan update'
  ticket = 'CHG001'
- After title(), upper(), and formatting, one report line should look like this:
  'Istanbul Edge / SW1 / CHG001: vlan update'

Expected result:
- 'Istanbul Edge / SW1 / CHG001: vlan update\\nLondon Core / R2 / CHG003: acl cleanup'
"""

# Task: change report builder

data = """
istanbul edge|sw1|vlan update CHG001|OK
new york core|fw1|policy push CHG002|failed
london core|r2|acl cleanup CHG003|ok
"""

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
    report = []

    for line in data.splitlines():
        line = line.strip()
        if not line:
            continue

        fields = [field.strip() for field in line.split('|')]
        if len(fields) != 4:
            continue

        site, device, change, result = fields
        if not result.lower().endswith('ok'):
            continue

        change_parts = change.rsplit(' ', 1)
        if len(change_parts) != 2:
            continue
        action, ticket = change_parts

        report.append(
            site.title() + ' / ' + device.upper() + ' / ' + ticket + ': ' + action
        )

    return '\\n'.join(report)
"""
