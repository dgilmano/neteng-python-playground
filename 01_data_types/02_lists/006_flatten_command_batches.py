"""
Task 6: Flatten command batches

Use Case:
Automation runners may receive commands grouped by phase but need one flat command list.
Flatten command batches while preserving order.

Rules:
1. Create a variable `result` as an empty list.
2. Create a loop that iterates over every command batch in `data`:
   for batch in data:
3. Each `batch` is a list of commands.
4. Add all commands from the current batch to `result` using `extend()`:
   result.extend(batch)
5. Use `extend()` instead of `append()` because the goal is one flat list, not a nested list.
6. Preserve the original order of batches and commands.
7. Return the `result` list.

Expected result:
- ['terminal length 0', 'show clock', 'show ip interface brief', 'show version', 'show inventory']
"""

# Task: flatten command batches

data = [
    ['terminal length 0', 'show clock'],
    ['show ip interface brief'],
    ['show version', 'show inventory'],
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

    for batch in data:
        result.extend(batch)

    return result
"""
