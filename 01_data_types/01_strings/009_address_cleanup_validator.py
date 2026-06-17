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
1. Each valid line uses 'hostname ip=<ip> mac=<mac>'.
2. Hostname must be alphanumeric.
3. IPv4 address must contain exactly three dots and four numeric octets.
4. Each octet must be between 0 and 255.
5. MAC may contain dots, colons, or dashes.
6. Remove '.', ':', and '-' from MAC and convert it to lowercase.
7. MAC is valid only when the normalized value is 12 alphanumeric characters.
8. Return only valid records.

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
