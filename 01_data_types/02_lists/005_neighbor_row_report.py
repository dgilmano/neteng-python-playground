"""
Task 5: Neighbor row report

Methods to practice:
- index access
- append()
- list iteration

Use Case:
Discovery tables are often represented as rows where each column has a fixed position.
Turn neighbor rows into readable link strings.

Rules:
1. Create a variable `result` as an empty list.
2. Create a loop that iterates over every row in `data`:
   for row in data:
3. Read the local device from index `0`.
4. Read the local interface from index `1`.
5. Read the neighbor device from index `2`.
6. Read the neighbor interface from index `3`.
7. Store these values in clear variables such as `local_device`, `local_interface`, `neighbor_device`, and `neighbor_interface`.
8. Build a string in this format:
   "<local> <local_if> -> <neighbor> <neighbor_if>"
9. Append the formatted string to the `result` list using `result.append()`.
10. Return the `result` list.

Expected result:
- ['r1 Gi0/1 -> sw1 Gi0/24', 'r2 Gi0/2 -> sw2 Gi0/24']
"""

# Task: neighbor row report

data = [
    ['r1', 'Gi0/1', 'sw1', 'Gi0/24'],
    ['r2', 'Gi0/2', 'sw2', 'Gi0/24'],
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

    for row in data:
        local_device = row[0]
        local_interface = row[1]
        neighbor_device = row[2]
        neighbor_interface = row[3]
        result.append(local_device + ' ' + local_interface + ' -> ' + neighbor_device + ' ' + neighbor_interface)

    return result
"""
