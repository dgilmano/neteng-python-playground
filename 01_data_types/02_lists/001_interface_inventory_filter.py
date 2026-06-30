"""
Task 1: Interface inventory filter

Use Case:
Interface inventories often include loopbacks, shutdown links, and partial records.
Return the names of physical interfaces whose line and protocol status are both up.

Rules:
1. Create a variable `result` as an empty list.
2. Create a loop that iterates over every interface record in `data`:
   for interface in data:
3. Inside the loop, read the interface type using dictionary key access:
   interface["type"]
4. Skip records where the type is not `"physical"`:
   if interface["type"] != "physical":
       continue
5. Read the line status using the `"status"` key.
6. Skip records where status is not `"up"`:
   if interface["status"] != "up":
       continue
7. Read the protocol status using the `"protocol"` key.
8. Skip records where protocol is not `"up"`:
   if interface["protocol"] != "up":
       continue
9. Extract the interface name from the `"name"` key.
10. Append the interface name to the `result` list using `result.append()`.
11. Return the `result` list.

Expected result:
- ['Gi0/1', 'Gi0/3']
"""

# Task: interface inventory filter

data = [
    {'name': 'Gi0/1', 'type': 'physical', 'status': 'up', 'protocol': 'up'},
    {'name': 'Gi0/2', 'type': 'physical', 'status': 'down', 'protocol': 'down'},
    {'name': 'Loopback0', 'type': 'loopback', 'status': 'up', 'protocol': 'up'},
    {'name': 'Gi0/3', 'type': 'physical', 'status': 'up', 'protocol': 'up'},
]


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

    for interface in data:
        if interface['type'] != 'physical':
            continue
        if interface['status'] != 'up':
            continue
        if interface['protocol'] != 'up':
            continue

        result.append(interface['name'])

    return result
"""
