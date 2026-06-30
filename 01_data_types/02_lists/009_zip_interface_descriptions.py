"""
Task 9: Zip interface descriptions

Use Case:
CSV columns are often parsed into parallel lists that need to become structured records.
Pair interface names with descriptions and return structured dictionaries.

Rules:
1. Unpack `data` into two variables:
   interfaces, descriptions = data
2. Create a variable `result` as an empty list.
3. Use `zip()` to iterate over both lists at the same time:
   for interface, description in zip(interfaces, descriptions):
4. For each pair, create a dictionary with two keys:
   - `"interface"`
   - `"description"`
5. Store the current interface name under the `"interface"` key.
6. Store the current description under the `"description"` key.
7. Append the dictionary to the `result` list using `result.append()`.
8. Return the `result` list.

Expected result:
- [{'interface': 'Gi0/1', 'description': 'uplink'}, {'interface': 'Gi0/2', 'description': 'server'}, {'interface': 'Gi0/3', 'description': 'spare'}]
"""

# Task: zip interface descriptions

data = (
    ['Gi0/1', 'Gi0/2', 'Gi0/3'],
    ['uplink', 'server', 'spare'],
)


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
    interfaces, descriptions = data
    result = []

    for interface, description in zip(interfaces, descriptions):
        result.append({'interface': interface, 'description': description})

    return result
"""
