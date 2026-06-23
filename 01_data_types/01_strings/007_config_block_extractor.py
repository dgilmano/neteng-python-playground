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
For each running-config line:
1. Keep the original line so you can check indentation.
2. Also create a stripped version of the line for comparisons and output.
3. Skip empty lines.

Now find this target block:
interface Gi0/1

4. Before the target block starts, skip all other lines.
5. When the stripped line equals 'interface Gi0/1':
   - start collecting lines.
   - add 'interface Gi0/1' to result.
6. After the target block starts, keep its indented child commands.
   - Example: ' description WAN uplink'
7. Stop when the next non-indented top-level line starts.
   - Example: 'interface Gi0/2'
8. Strip every line before adding it to result.
   - Example: ' description WAN uplink' -> 'description WAN uplink'
9. Skip child commands that start with 'shutdown'.
10. Return the collected lines joined with '\\n'.

Step output examples:
- After stripping the target line, it should look like this:
  'interface Gi0/1'
- After stripping child commands and skipping shutdown, result should look like this:
  ['interface Gi0/1', 'description WAN uplink', 'ip address 192.0.2.1 255.255.255.252']
- After join('\n'), output should look like this:
  'interface Gi0/1\ndescription WAN uplink\nip address 192.0.2.1 255.255.255.252'

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
