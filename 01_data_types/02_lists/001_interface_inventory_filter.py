"""
Task 1: Interface inventory filter

Methods to practice:
- append()
- continue
- loop filtering
- dictionary access

Use Case:
A network inventory often contains partial records, loopbacks, and interfaces that are not ready to use.
Return a list of operational physical interfaces with a human-readable summary.

Rules:
1. Create two empty lists:
   - `result` for valid interfaces.
   - `skipped` for skipped interfaces.
2. Create a loop to iterate through every interface record:
   for interface in data:
3. Create variables for the fields you will use later. Use the `get()` method to safely extract values from the interface dictionary.
   - `name`
   - `status`       | convert `status` to lowercase.
   - `protocol`     | convert `protocol` to lowercase.
   - `description`  | remove leading and trailing spaces from `description`.
4. Skip non-physical interfaces. Save the reason in `skipped`.
5. Skip interfaces that are not fully operational (`status` or `protocol` is not `"up"`). Save the reason in `skipped`.
6. Skip interfaces without a description. Save the reason in `skipped`.
7. Create a dictionary containing:
   - `name`
   - `description`
   - `speed`
   - `summary` (`"<name> - <description> - <speed>"`)
8. Append the dictionary to `result`.
9. Return a dictionary containing:
    - `interfaces`
    - `skipped`
    - `total`

Expected result:
- [{'name': 'Gi0/1', 'description': 'uplink', 'speed': '10G'}, {'name': 'Gi0/3', 'description': 'storage', 'speed': '25G'}]
"""

# Task: interface inventory filter

data = [
    {'name': 'Gi0/1',     'type': 'physical', 'status': 'up',   'protocol': 'up',   'description': 'uplink',      'speed': '10G'},
    {'name': 'Gi0/2',     'type': 'physical', 'status': 'down', 'protocol': 'up',   'description': 'server',      'speed': '1G'},
    {'name': 'Gi0/3',     'type': 'physical', 'status': 'up',   'protocol': 'down', 'description': 'backup',      'speed': '10G'},
    {'name': 'Gi0/4',     'type': 'physical', 'status': 'down', 'protocol': 'down', 'description': 'maintenance', 'speed': '1G'},
    {'name': 'Loopback0', 'type': 'loopback', 'status': 'up',   'protocol': 'up',   'description': 'router-id',   'speed': 'N/A'},
    {'name': 'Gi0/5',     'type': 'physical', 'status': 'up',   'protocol': 'up',   'description': '',            'speed': '25G'},
]


def solve(data):
    result = []
    skipped = []

    for item in data:
        name = item.get('name', 'unknown')
        status = item.get('status', '').lower()
        protocol = item.get('protocol', '').lower()
        description = item.get('description', '').strip()

        if item.get('type') != 'physical':
            skipped.append({
                'name': name,
                'reason': 'not physical'
            })
            continue
        
        if item.get("status") != 'up' or item.get("protocol") != 'up':
            skipped.append({
                "name": name,
                "reason": 'not operational'
            })
            continue

        if not description:
            skipped.append({
                "name": name,
                "reason": "missing description"
            })
            continue

        result.append({
            "name": name,
            'description': description,
            'speed': item.get('speed'),
        })

    return {
        'interfaces': result,
        'skipped': skipped,
        'total operational interfaces': len(result)
    }


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
    skipped = []

    for interface in data:
        name = interface.get("name", "unknown")
        status = interface.get("status", "").lower()
        protocol = interface.get("protocol", "").lower()
        description = interface.get("description", "").strip()

        if interface.get("type") != "physical":
            skipped.append({"name": name, "reason": "not physical"})
            continue

        if status != "up" or protocol != "up":
            skipped.append({"name": name, "reason": "not operational"})
            continue

        if not description:
            skipped.append({"name": name, "reason": "missing description"})
            continue

        result.append({
            "name": name,
            "description": description,
            "speed": interface.get("speed", "unknown"),
            "summary": f"{name} - {description} - {interface.get('speed', 'unknown')}",
        })

    return {
        "interfaces": result,
        "skipped": skipped,
        "total operational interfaces": len(result),
    }
"""
