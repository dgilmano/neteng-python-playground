"""
Task 9: Address cleanup validator

Methods to practice:
- splitlines(), strip(), partition(), count(), split(), isdigit(), lower(), replace(), isalnum()

Use Case:
Inventory files often contain key-value lines with IP and MAC addresses.
The parser should normalize valid values and reject malformed ones.

Assignment:
Parse address inventory lines into normalized records.

Input:
- multiline text with hostname, IP, and MAC fields

Rules:
For each inventory line:
1. Strip spaces from both sides of the line.
2. Skip empty lines.

Now parse one inventory line like this:
SW1 ip=192.168.1.10 mac=AA:BB:CC:00:11:22

3. Split the line into fields by spaces.
4. A valid line must have exactly 3 fields:
   - hostname
   - ip=<ip>
   - mac=<mac>
5. Keep only hostnames that are alphanumeric.
   - Example: 'SW1' is valid.
   - Example: 'bad-host' is skipped.
6. Use partition('=') to split the IP field.
   - key must be 'ip'.
   - value is the IPv4 address.
7. Use partition('=') to split the MAC field.
   - key must be 'mac'.
   - value is the MAC address.
8. Validate the IPv4 address:
   - it must contain exactly three dots.
   - splitting by '.' must produce four octets.
   - each octet must contain only digits.
   - each octet value must be between 0 and 255.
9. Normalize the MAC address:
   - remove '.', ':', and '-'.
   - convert the result to lowercase.
10. Validate the normalized MAC address:
    - it must be exactly 12 characters long.
    - it must contain only alphanumeric characters.
11. Add one dictionary to result:
    - {'hostname': hostname, 'ip': ip, 'mac': mac}

Step output examples:
- After split(), one inventory line should look like this:
  ['SW1', 'ip=192.168.1.10', 'mac=AA:BB:CC:00:11:22']
- After partition('='), values should look like this:
  ip = '192.168.1.10'
  mac = 'AA:BB:CC:00:11:22'
- After MAC normalization, mac should look like this:
  'aabbcc001122'
- After validation, one result item should look like this:
  {'hostname': 'SW1', 'ip': '192.168.1.10', 'mac': 'aabbcc001122'}

Expected result:
- [
    {'hostname': 'SW1', 'ip': '192.168.1.10', 'mac': 'aabbcc001122'},
    {'hostname': 'R2', 'ip': '10.0.0.1', 'mac': '001122334455'},
  ]
"""

# Task: address cleanup validator

data = """
SW1 ip=192.168.1.10 mac=AA:BB:CC:00:11:22
bad-host ip=192.168.1.300 mac=aa.bb.cc.dd.ee.ff
R2 ip=10.0.0.1 mac=0011.2233.4455
FW1 ip=10.0.0 mac=00-11-22-33-44-55
"""

def valid_ip(ip):
    if ip.count(".") != 3:
        return False
    for items in ip.split("."):
        if not items.isdigit():
            return False
        value = int(items)
        if value < 0 or value > 255:
            return False
    return True

def solve(data):
    result = []
    for items in data.splitlines():
        if not items:
            continue
        
        parts = items.split()
        if len(parts) != 3:
            continue

        hostname = parts[0]
        if not hostname.isalnum():
            continue

        ip_key, sep, ip_addr = parts[1].partition('=')
        mac_key, sep, mac_addr = parts[2].partition('=')
        if ip_key != 'ip' or mac_key != 'mac':
            continue

        if not valid_ip(ip_addr):
            continue

        mac = mac_addr.replace('.', '').replace(':', '').replace('-', '').lower()
        if len(mac) != 12 or not mac.isalnum():
            continue

        result.append({'hostname': hostname, 'ip': ip_addr, 'mac': mac})

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
def valid_ip(ip):
    if ip.count('.') != 3:
        return False
    for octet in ip.split('.'):
        if not octet.isdigit():
            return False
        value = int(octet)
        if value < 0 or value > 255:
            return False
    return True

def solve(data):
    result = []

    for line in data.splitlines():
        line = line.strip()
        if not line:
            continue

        parts = line.split()
        if len(parts) != 3:
            continue

        hostname = parts[0]
        if not hostname.isalnum():
            continue

        ip_key, separator, ip = parts[1].partition('=')
        mac_key, separator, mac = parts[2].partition('=')
        if ip_key != 'ip' or mac_key != 'mac':
            continue

        if not valid_ip(ip):
            continue

        mac = mac.replace('.', '').replace(':', '').replace('-', '').lower()
        if len(mac) != 12 or not mac.isalnum():
            continue

        result.append({'hostname': hostname, 'ip': ip, 'mac': mac})

    return result
"""
