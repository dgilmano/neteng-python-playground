"""
Task 3: Maintenance queue update

Use Case:
Operations queues need priority jobs at the front and cleanup jobs at the end.
Update a maintenance queue with one priority job and one final post-check job.

Rules:
1. Work with the existing `data` list.
2. Insert the priority job `"emergency-core"` at the beginning of the list using `insert()`:
   data.insert(0, "emergency-core")
3. Remember that index `0` means the first position in the list.
4. Append the final job `"post-check"` to the end of the list using `append()`:
   data.append("post-check")
5. Do not create a separate result list for this task.
6. Return the updated `data` list.

Expected result:
- ['emergency-core', 'backup-core', 'audit-fw', 'post-check']
"""

# Task: maintenance queue update

data = ['backup-core', 'audit-fw']


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
    data.insert(0, 'emergency-core')
    data.append('post-check')
    return data
"""
