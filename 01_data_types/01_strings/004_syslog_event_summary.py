"""
Task 4: Syslog event summary

Methods to practice:
- splitlines(), strip(), find(), index(), slicing, partition(), rpartition(), lower(), endswith()

Use Case:
Syslog lines are mostly text, but useful values can be extracted using markers.
This is common when a full parser is not available.
Extract link events from syslog output.

Rules:
1. Create an empty list `result`.
2. Split the input data into lines and iterate through each line:
   for line in data.splitlines():
3. Remove leading and trailing spaces from the current line:
   line = line.strip()
4. Skip lines that do not contain the `%LINK-3-UPDOWN` event:
   if line.find("%LINK-3-UPDOWN") == -1:
       continue
5. Extract the device name from the beginning of the line using `partition(":")`:
   device, separator, rest = line.partition(":")
6. Split the line by the last colon using `rpartition(":")` to separate the syslog header from the actual message:
   header, separator, message = line.rpartition(":")
7. If the separator was not found, skip the line:
   if not separator:
       continue
8. Remove leading and trailing spaces from the message:
   message = message.strip()
9. Create a marker variable with the text that appears before the interface name:
   marker = "Interface "
10. Find the start and end positions of the interface name:
   - start position: where `"Interface "` begins
   - end position: the comma after the interface name
   try:
       start = message.index(marker)
       end = message.index(",", start)
   except ValueError:
       continue
11. Move `start` to the real beginning of the interface name by adding the marker length:
   start = start + len(marker)
12. Extract the interface name using string slicing:
   interface = message[start:end]
13. Convert the message to lowercase to make state detection case-insensitive:
   normalized = message.lower()
14. Detect the interface state:
   - if the message ends with `"up"`, set state to `"up"`
   - if the message ends with `"down"`, set state to `"down"`
   - otherwise, set state to `"unknown"`
   if normalized.endswith("up"):
       state = "up"
   elif normalized.endswith("down"):
       state = "down"
   else:
       state = "unknown"
15. Create a dictionary with parsed information and append it to the `result` list:
   result.append({
       "device": device.strip(),
       "interface": interface,
       "state": state,
   })
16. Return the `result` list.

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
