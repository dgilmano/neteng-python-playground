"""
Task 10: Change report builder

Methods to practice:
- splitlines(), strip(), lower(), upper(), title(), split(), rsplit(), endswith(), join()

Use Case:
Small automation scripts often turn raw change notes into a clean report.
This combines parsing, normalization, filtering, and formatting.

Rules:
1. Create an empty list `report`.
2. Split the input data into lines and iterate through each line:
   for line in data.splitlines():
3. Remove leading and trailing spaces from the current line:
   line = line.strip()
4. Skip empty lines:
   if not line:
       continue
5. Split the current line by the `"|"` separator, remove leading and trailing spaces from each field, and store the result in a list:
   fields = [field.strip() for field in line.split("|")]
6. Skip invalid lines that do not contain exactly 4 fields:
   if len(fields) != 4:
       continue
7. Assign the fields to separate variables:
   site, device, change, result = fields
8. Keep only successful changes by checking whether the result ends with `"ok"`:
   if not result.lower().endswith("ok"):
       continue
   Example:
   "OK".lower().endswith("ok")      # True
   "ok".lower().endswith("ok")      # True
   "failed".lower().endswith("ok")  # False
9. Split the change description into the action and ticket number using `rsplit(" ", 1)`:
   change_parts = change.rsplit(" ", 1)
   Example:
   "vlan update CHG001"
   change_parts = ["vlan update", "CHG001"]
10. Skip invalid change descriptions that do not contain exactly 2 parts:
   if len(change_parts) != 2:
       continue
11. Assign the action and ticket number to separate variables:
   action, ticket = change_parts
12. Format the output:
   - convert the site name to title case using `title()`
   - convert the device name to uppercase using `upper()`
   - combine all values into a single string
   report.append(
       site.title() + " / " +
       device.upper() + " / " +
       ticket + ": " +
       action
   )
Example:
   Istanbul Edge / SW1 / CHG001: vlan update
13. Join all report entries into a single string using `"\n".join()` and return the result:
   return "\n".join(report)

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
    report = []

    for line in data.splitlines():
        line = line.strip()
        if not line:
            continue

        fields = [field.strip() for field in line.split("|")]
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
