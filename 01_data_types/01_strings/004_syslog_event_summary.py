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
For each syslog line:
1. Strip spaces from both sides of the line.
2. Skip empty lines.
3. Skip lines that do not contain '%LINK-3-UPDOWN'.

Now parse only matching lines like this:
SW1: %LINK-3-UPDOWN: Interface Gi0/1, changed state to up

4. Extract device:
   - device is the text before the first ':'.
   - Use partition(':').
   - Example: 'SW1'
5. Extract message:
   - message is the text after the last ':'.
   - Use rpartition(':').
   - Example: 'Interface Gi0/1, changed state to up'
6. Extract interface from message:
   - interface starts after 'Interface '.
   - interface ends before the comma ','.
   - Use index() and slicing.
   - Example: 'Gi0/1'
7. Determine state from message:
   - 'up' if the message ends with 'up'
   - 'down' if the message ends with 'down'
   - 'unknown' otherwise
8. Add one dictionary to result:
   - {'device': device, 'interface': interface, 'state': state}

Step output examples:
- After filtering, one matching line should look like this:
  'SW1: %LINK-3-UPDOWN: Interface Gi0/1, changed state to up'
- After partition/rpartition, extracted values should look like this:
  device = 'SW1'
  message = 'Interface Gi0/1, changed state to up'
- After slicing the message, one result item should look like this:
  {'device': 'SW1', 'interface': 'Gi0/1', 'state': 'up'}

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
    result = []
    for item in data.splitlines():
        if not item:
            continue
        if item.find("%LINK-3-UPDOWN") == -1:
            continue
        
        device, __, __ = item.partition(":")
        __, __, message = item.rpartition(":")

        message = message.strip()
        marker = 'Interface '

        try:
            start = message.index(marker)
            end = message.index(',', start)
        except ValueError:
            continue
    
        start = start + len(marker)
        interface_name = message[start:end]
        fixed_message = message.lower()

        if fixed_message.endswith('up'):
            state = 'up'
        elif fixed_message.endswith('down'):
            state = 'down'
        else:
            state = 'unknown'

        result.append(
            {
                'device': device,
                'interface': interface_name,
                'state': state
            }
        )

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
