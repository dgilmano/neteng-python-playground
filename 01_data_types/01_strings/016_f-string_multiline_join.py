"""
Task 16: f-string + multiline join()

Use Case:
Automation often renders a multiline config block from structured input values.
Use f-strings for each line and join them with newline characters.

Assignment:
Render multiline config from template fields - build an interface access-port config.

Steps:
1. Inspect the input data.
2. Build each config line with an f-string.
3. Store the lines in a list.
4. Join the lines with '\n'.
5. Return the multiline config string.

Expected result:
- 'interface Gi0/10\n description USER-PORT\n switchport access vlan 20'
"""

# Task: f-string + multiline join()

data = {'interface': 'Gi0/10', 'description': 'USER-PORT', 'vlan': 20}

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
--- Option 1: f-strings + join() ---
def solve_lines(data):
    lines = []
    lines.append(f"interface {data['interface']}")
    lines.append(f" description {data['description']}")
    lines.append(f" switchport access vlan {data['vlan']}")
    return '\n'.join(lines)

--- Option 2: parenthesized multiline string ---
def solve_template(data):
    return (
        f"interface {data['interface']}\n"
        f" description {data['description']}\n"
        f" switchport access vlan {data['vlan']}"
    )
"""
