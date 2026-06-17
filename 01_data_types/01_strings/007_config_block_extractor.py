"""
Task 7: Config block extractor

Methods to practice:
- splitlines(), strip(), startswith(), lower(), join()

Use Case:
Automation often needs only one section from a full running-config.
The section starts with a marker and ends before the next top-level command.

Assignment:
Extract one interface block and return cleaned commands.

Input:
- multiline running-config text

Rules:
1. Find the block that starts with 'interface Gi0/1'.
2. Keep the interface line and its indented child commands.
3. Stop when the next non-indented top-level line starts.
4. Strip every returned line.
5. Skip child commands that start with 'shutdown'.
6. Return the cleaned block as a newline-joined string.

Expected result:
- 'interface Gi0/1\\ndescription WAN uplink\\nip address 192.0.2.1 255.255.255.252'
"""

# Task: config block extractor

data = """
hostname SW1
interface Gi0/1
 description WAN uplink
 ip address 192.0.2.1 255.255.255.252
 shutdown disabled by policy
interface Gi0/2
 description LAN
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
    result = []
    in_block = False

    for raw_line in data.splitlines():
        line = raw_line.rstrip()
        stripped = line.strip()
        if not stripped:
            continue

        if stripped == 'interface Gi0/1':
            in_block = True
            result.append(stripped)
            continue

        if in_block and raw_line and not raw_line.startswith(' '):
            break

        if in_block:
            if stripped.lower().startswith('shutdown'):
                continue
            result.append(stripped)

    return '\\n'.join(result)
"""
