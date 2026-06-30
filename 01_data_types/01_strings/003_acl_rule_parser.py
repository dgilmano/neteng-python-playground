"""
Task 3: ACL rule parser

Methods to practice:
- splitlines(), strip(), startswith(), lower(), split(), isdigit(), count()

Use Case:
ACL parsing requires fixed-position fields plus conditional logic for optional ports.
Comments and malformed lines should not break the parser.

Rules:
1. Create an empty list `result`.
2. Split the input data into lines and iterate through each line:
   for item in data.splitlines():
3. Remove leading and trailing spaces from the current line:
   line = item.strip()
4. Skip empty lines, comment lines starting with `"!"`, and "remark" lines:
   if not line or line.startswith("!") or line.startswith("remark"):
       continue
5. Convert the line to lowercase and split it into words:
   parts = line.lower().split()
6. Skip invalid rules:
   - if the line has fewer than 4 parts
   - if the first word is not `"permit"` or `"deny"`
   if len(parts) < 4 or parts[0] not in ("permit", "deny"):
       continue
7. Create a dictionary `rule` with the action and protocol from the current line. 
   Initialize the remaining fields with `None`.
   rule = {
       "action": parts[0],
       "protocol": parts[1],
       "source": None,
       "source_type": None,
       "destination": None,
       "port": None,
   }
8. If the source is in `host` format, verify that the rule contains at least 5 fields. If not, skip the rule.
   if parts[2] == "host":
       if len(parts) < 5:
           continue
9. For `host` format, save the source, source type, and destination in the `rule` dictionary.
   rule["source"] = parts[3]
   rule["source_type"] = "host"
   rule["destination"] = parts[4]
10. Otherwise, save the source and destination in the `rule` dictionary.
   rule["source"] = parts[2]
   rule["destination"] = parts[3]
11. In same else condition, detect the source type:
   - if source is `"any"`, set `source_type` to `"any"`
   - if source contains one `/`, set `source_type` to `"network"`
   - otherwise, set `source_type` to `"host"`
12. 11. Check if the rule contains the keyword `"eq"`. 
If it does, find its position using `parts.index("eq")`. Verify that the next value exists and is a number. 
If valid, convert it to an integer and save it in the `rule` dictionary.
   if "eq" in parts:
       eq_index = parts.index("eq")
       if eq_index + 1 < len(parts) and parts[eq_index + 1].isdigit():
           rule["port"] = int(parts[eq_index + 1])
13. Append the completed `rule` dictionary to the `result` list.
14. Return the `result` list.

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
        if len(parts) < 4 or parts[0] not in ("permit", "deny"):
            continue
        rule = {
            "action": parts[0],
            "protocol": parts[1],
            "source": None,
            "source_type": None,
            "destination": None,
            "port": None
        }
        if parts[2] == "host":
            if len(parts) < 5:
                continue
            rule['source'] = parts[3]
            rule["source_type"] = "host"
            rule["desctination"] = parts[4]
        else:
            rule["source"] = parts[2]
            rule["destination"] = parts[3]

            if parts[2] == "any":
                rule["source_type"] = "any"
            elif parts[2].count("/") == 1:
                rule["source_type"] = "network"
            else:
                rule["source_type"] = "host"

        if 'eq' in parts:
            eq_index = parts.index("eq")
            if eq_index + 1 < len(parts) and parts[eq_index + 1].isdigit():
                rule["port"] = int(parts[eq_index + 1])

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
