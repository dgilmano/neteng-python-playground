"""
Task 7: Config block extractor

Methods to practice:
- splitlines(), strip(), startswith(), lower(), join()

Use Case:
Automation often needs only one section from a full running-config.
The section starts with a marker and ends before the next top-level command.

Rules:
1. Create an empty list `result`.
2. Create a flag variable `in_block` and set it to `False`.
3. Split the input data into lines and iterate through each line:
   for raw_line in data.splitlines():
4. Remove trailing spaces using `rstrip()` and store the result in `line`:
   line = raw_line.rstrip()
5. Remove leading and trailing spaces using `strip()` and store the result in `stripped`:
   stripped = line.strip()
6. Skip empty lines:
   if not stripped:
       continue
7. Check if the current line is the interface you want to extract:
   if stripped == "interface Gi0/1":
8. If the interface is found:
   - set `in_block` to `True`
   - append the interface name to the `result` list
   - continue to the next iteration
   in_block = True
   result.append(stripped)
   continue
9. If you are already inside the interface block and the current line does not start with a space, stop processing because a new configuration block has started.
   if in_block and raw_line and not raw_line.startswith(" "):
       break
   Example:
   interface Gi0/1
   description WAN
   ip address ...
   interface Gi0/2
   - The loop stops when it reaches:
      interface Gi0/2
10. While processing the interface block, skip lines that start with `"shutdown"`:
   if stripped.lower().startswith("shutdown"):
       continue
11. Append all remaining configuration lines to the `result` list:
   result.append(stripped)
12. Join all lines into a single string using `"\n".join()` and return the result:
   return "\n".join(result)

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
    result = []
    in_block = False

    for item in data.splitlines():
        raw_line = item
        line = item.strip()

        if not line:
            continue

        if line == "interface Gi0/1":
            in_block = True
            result.append(line)
            continue

        if in_block and raw_line.startswith("interface "):
            break

        if in_block:
            if line.lower().startswith("shutdown"):
                continue
            result.append(line)

    return "\n".join(result)

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
