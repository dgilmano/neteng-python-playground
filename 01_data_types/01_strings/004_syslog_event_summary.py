"""
Task 4: Syslog event summary

Methods to practice:
- splitlines(), strip(), find(), index(), slicing, partition(), rpartition(), lower(), endswith()

Use Case:
Syslog lines are mostly text, but useful values can be extracted using markers.
This is common when a full parser is not available.

Assignment:
Extract link events from syslog output.

Input:
- multiline syslog text

Rules:
1. Process the text line by line.
2. Use find() to keep only lines that contain '%LINK-3-UPDOWN'.
3. Use rpartition(':') to separate the syslog header from the message.
4. Use index() plus slicing to extract the interface after 'Interface '.
5. Determine state:
   - 'up' if the message ends with 'up'
   - 'down' if the message ends with 'down'
   - 'unknown' otherwise
6. Return dictionaries with device, interface, and state.
7. The device is the text before the first colon.

Expected result:
- [
    {'device': 'SW1', 'interface': 'Gi0/1', 'state': 'up'},
    {'device': 'SW1', 'interface': 'Gi0/2', 'state': 'down'},
  ]
"""

# Task: syslog event summary

data = """
SW1: %LINK-3-UPDOWN: Interface Gi0/1, changed state to up
SW1: %LINEPROTO-5-UPDOWN: Line protocol on Interface Gi0/1, changed state to up
SW1: %LINK-3-UPDOWN: Interface Gi0/2, changed state to down
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

    for line in data.splitlines():
        line = line.strip()
        if line.find('%LINK-3-UPDOWN') == -1:
            continue

        device, separator, rest = line.partition(':')
        header, separator, message = line.rpartition(':')
        if not separator:
            continue

        message = message.strip()
        marker = 'Interface '
        try:
            start = message.index(marker)
            end = message.index(',', start)
        except ValueError:
            continue

        start = start + len(marker)
        interface = message[start:end]
        normalized = message.lower()

        if normalized.endswith('up'):
            state = 'up'
        elif normalized.endswith('down'):
            state = 'down'
        else:
            state = 'unknown'

        result.append({
            'device': device.strip(),
            'interface': interface,
            'state': state,
        })

    return result
"""
