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
1. Split the text into lines and strip each line.
2. Skip empty lines.
3. Split each line into four fields using '|'.
4. Format site with title().
5. Format device with upper().
6. Normalize result with lower().
7. Keep only lines whose result ends with 'ok'.
8. For the change field, use rsplit(' ', 1) to separate action text and ticket ID.
9. Return newline-joined report lines:
   '<Site> / <DEVICE> / <ticket>: <action>'

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
