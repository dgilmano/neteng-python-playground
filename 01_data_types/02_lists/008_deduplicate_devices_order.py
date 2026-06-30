"""
Task 8: Deduplicate devices in order

Use Case:
Merged inventories can contain duplicate hostnames but the first order still matters.
Remove duplicate devices while preserving their first-seen order.

Rules:
1. Create a variable `result` as an empty list.
2. Create a variable `seen` as an empty set:
   seen = set()
3. Create a loop that iterates over devices in the original order:
   for device in data:
4. Check whether the current device is already in `seen`.
5. If the device is already in `seen`, skip it using `continue`.
6. If the device is new, add it to the `seen` set using `seen.add()`.
7. Append the new device to the `result` list using `result.append()`.
8. Preserve the first-seen order of devices.
9. Return the `result` list.

Expected result:
- ['r1', 'sw1', 'fw1', 'r2']
"""

# Task: deduplicate devices in order

data = ['r1', 'sw1', 'r1', 'fw1', 'sw1', 'r2']


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
    seen = set()

    for device in data:
        if device in seen:
            continue
        seen.add(device)
        result.append(device)

    return result
"""
