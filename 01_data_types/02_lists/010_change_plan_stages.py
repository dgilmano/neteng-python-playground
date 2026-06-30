"""
Task 10: Change plan stages

Methods to practice:
- append()
- extend()
- list ordering

Use Case:
Change plans often need runnable stages first and blocked stages clearly separated.
Return stage names with ready stages first, then blocked stages, skipping completed stages.

Rules:
1. Create a variable `ready` as an empty list.
2. Create a variable `blocked` as an empty list.
3. Create a loop that iterates over every stage dictionary in `data`.
4. Read the stage status using the `"status"` key.
5. If status is `"ready"`, append the stage name to the `ready` list:
   ready.append(item["stage"])
6. If status is `"blocked"`, append the stage name to the `blocked` list:
   blocked.append(item["stage"])
7. Skip stages with status `"done"`.
8. After the loop, add blocked stages after ready stages using `extend()`:
   ready.extend(blocked)
9. Return the `ready` list.

Expected result:
- ['validate', 'verify', 'deploy']
"""

# Task: change plan stages

data = [
    {'stage': 'validate', 'status': 'ready'},
    {'stage': 'backup', 'status': 'done'},
    {'stage': 'deploy', 'status': 'blocked'},
    {'stage': 'verify', 'status': 'ready'},
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
    ready = []
    blocked = []

    for item in data:
        if item['status'] == 'ready':
            ready.append(item['stage'])
        elif item['status'] == 'blocked':
            blocked.append(item['stage'])

    ready.extend(blocked)
    return ready
"""
