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
        item = item.strip()
        print(item)
        


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
        if not line or line.startswith('!'):
            continue

        tokens = line.split()
        if len(tokens) < 4:
            continue

        action = tokens[0].lower()
        if action not in ('permit', 'deny'):
            continue

        protocol = tokens[1].lower()
        source_index = 2

        if tokens[source_index] == 'host':
            if source_index + 2 >= len(tokens):
                continue
            source = tokens[source_index + 1]
            source_type = 'host'
            destination_index = source_index + 2
        else:
            source = tokens[source_index]
            if source == 'any':
                source_type = 'any'
            elif source.count('/') == 1:
                source_type = 'network'
            else:
                source_type = 'host'
            destination_index = source_index + 1

        destination = tokens[destination_index]
        port = None

        if 'eq' in tokens:
            eq_index = tokens.index('eq')
            if eq_index + 1 < len(tokens) and tokens[eq_index + 1].isdigit():
                port = int(tokens[eq_index + 1])

        result.append({
            'action': action,
            'protocol': protocol,
            'source': source,
            'source_type': source_type,
            'destination': destination,
            'port': port,
        })

    return result
"""
