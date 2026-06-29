"""
Task 9: Address cleanup validator

Methods to practice:
- splitlines(), strip(), partition(), count(), split(), isdigit(), lower(), replace(), isalnum()

Use Case:
Inventory files often contain key-value lines with IP and MAC addresses.
The parser should normalize valid values and reject malformed ones.

Rules:
1. Create an empty list `result`.
2. Split the input data into lines and iterate through each line:
   for line in data.splitlines():
3. Remove leading and trailing spaces from the current line:
   line = line.strip()
4. Skip empty lines:
   if not line:
       continue
5. Split the current line into three parts:
   - hostname
   - IP field
   - MAC field
   parts = line.split()
6. Skip invalid lines that do not contain exactly 3 parts:
   if len(parts) != 3:
       continue
7. Save the hostname from the first column:
   hostname = parts[0]
8. Check that the hostname contains only letters and digits:
   if not hostname.isalnum():
       continue
   Example:
   "SW1".isalnum()       # True
   "bad-host".isalnum()  # False
9. Split the IP field and MAC field using the `partition("=")` method:
   ip_key, separator, ip = parts[1].partition("=")
   mac_key, separator, mac = parts[2].partition("=")
   Example:
   "ip=192.168.1.10"
   ip_key = "ip"
   separator = "="
   ip = "192.168.1.10"
10. Verify that the field names are correct:
   - IP field must start with `"ip"`
   - MAC field must start with `"mac"`
   if ip_key != "ip" or mac_key != "mac":
       continue
11. Validate the IP address using the `valid_ip()` function:
   if not valid_ip(ip):
       continue
12. Normalize the MAC address by removing separators and converting it to lowercase:
   mac = mac.replace(".", "").replace(":", "").replace("-", "").lower()
   xample:
   AA:BB:CC:00:11:22 → aabbcc001122
   0011.2233.4455    → 001122334455
   00-11-22-33-44-55 → 001122334455
13. Check that the normalized MAC address contains exactly 12 alphanumeric characters:
   if len(mac) != 12 or not mac.isalnum():
       continue
14. Create a dictionary with the parsed information and append it to the `result` list:
   result.append({
       "hostname": hostname,
       "ip": ip,
       "mac": mac,
   })
15. Return the `result` list.

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
