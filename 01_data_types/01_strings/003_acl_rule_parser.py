"""
Task 3: ACL rule parser

Methods to practice:
- splitlines(), strip(), startswith(), lower(), split(), isdigit(), count()

Use Case:
ACL parsing requires fixed-position fields plus conditional logic for optional ports.
Comments and malformed lines should not break the parser.

Assignment:
Parse ACL lines into structured records.

Input:
- multiline ACL text

Rules:
1. Strip every line.
2. Skip empty lines and comment lines that start with '!'.
3. Support only permit/deny actions.
4. Normalize action and protocol to lowercase.
5. Extract source and destination fields by index.
6. Support source in these forms: any, host <ip>, or network/prefix.
7. If the line contains "eq <port>", convert the port to int.
8. If the port is missing or invalid, use None.
9. Add a simple source_type field:
   - 'network' if source contains exactly one slash
   - 'any' if source is 'any'
   - 'host' otherwise

Expected result:
- [
    {'action': 'permit', 'protocol': 'tcp', 'source': '10.0.0.0/24', 'source_type': 'network', 'destination': 'any', 'port': 443},
    {'action': 'deny', 'protocol': 'ip', 'source': 'any', 'source_type': 'any', 'destination': 'any', 'port': None},
    {'action': 'permit', 'protocol': 'udp', 'source': '192.0.2.10', 'source_type': 'host', 'destination': 'any', 'port': 53},
  ]
"""

# Task: ACL rule parser

data = """
! edge firewall
Permit TCP 10.0.0.0/24 any eq 443
deny ip any any
permit udp host 192.0.2.10 any eq 53
remark skip this line
"""

def solve(data):
    result = []
    for item in data.splitlines():
        line = item.strip()
        if not line or line.startswith("!") or line.startswith("remark"):
            continue
        parts = line.lower().split()
        rule = {
            'action': parts[0],
            'protocol': parts[1],
            'source': None,
            'source_type': None,
            'destination': None,
            'port': None
        }
        if parts[2] == 'host':
            rule['source'] = parts[3]
            rule['source_type'] = "host"
            rule['destination'] = parts[4]
            if "eq" in parts:
                port = parts[-1]
                if port.isdigit():
                    rule["port"] = int(port)
                else:
                    rule["port"] = None
        else:
            rule["source"] = parts[2]
            rule["destination"] = parts[3]
            if parts[2] == "any":
                rule["source_type"] = "any"
            else:
                rule["source_type"] = "network"
            if "eq" in parts:
                rule["port"] = int(parts[-1])

        result.append(rule)
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
    for item in data.splitlines():
        line = item.strip()
        if not line or line.startswith("!") or line.startswith("remark"):
            continue

        parts = line.lower().split()
        if len(parts) < 4 or parts[0] not in ("permit", "deny"):
            continue

        rule = {
            "action": parts[0],
            "protocol": parts[1],
            "source": None,
            "source_type": None,
            "destination": None,
            "port": None,
        }

        if parts[2] == "host":
            if len(parts) < 5:
                continue
            rule["source"] = parts[3]
            rule["source_type"] = "host"
            rule["destination"] = parts[4]
        else:
            rule["source"] = parts[2]
            rule["destination"] = parts[3]
            if parts[2] == "any":
                rule["source_type"] = "any"
            elif parts[2].count("/") == 1:
                rule["source_type"] = "network"
            else:
                rule["source_type"] = "host"

        if "eq" in parts:
            eq_index = parts.index("eq")
            if eq_index + 1 < len(parts) and parts[eq_index + 1].isdigit():
                rule["port"] = int(parts[eq_index + 1])

        result.append(rule)

    return result
"""
