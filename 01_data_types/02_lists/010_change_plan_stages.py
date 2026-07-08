"""
Task 10: Change plan organizer

Methods to practice:
- for
- enumerate()
- append()
- extend()
- .get()
- .strip()
- .lower()
- isinstance()
- continue
- membership checks
- structured output

Use Case:
Change plans often come from ticketing systems as a list of stage records.
Some stages are ready, blocked, already complete, duplicated, or malformed.
A production script should normalize stages, remove duplicates, skip invalid entries, and return a clear execution order.

Rules:
1. Create an empty dictionary called `result` with two keys:
   - `"execution_order"` for valid stages in order.
   - `"skipped"` for invalid or ignored stages.
2. Create two empty lists:
   - `ready`
   - `blocked`
3. Create an empty set called `seen` to track duplicate stage names.
4. Create a loop to iterate through every stage record in `data`.
   Use `enumerate()` so every skipped record can include the original row number.
5. Check whether the current item is a dictionary.
   If it is not, append a skipped record with the row number and reason, then continue.
6. Create variables for the fields you will use later:
   - `stage`
   - `status`
7. Validate that `stage` is a string and is not empty after `.strip()`.
   If not, append a skipped record with the row number and reason, then continue.
8. Validate that `status` is a string and is not empty after `.strip()`.
   If not, append a skipped record with the row number and reason, then continue.
9. Normalize values:
   - stage → `strip().lower()`
   - status → `strip().lower()`
10. Check whether the stage was already seen.
    If yes, append a skipped record with the row number and reason, then continue.
11. If the status is `"ready"`, append the stage to `ready`.
12. If the status is `"blocked"`, append the stage to `blocked`.
13. If the status is `"done"`, append a skipped record with the row number and reason, then continue.
14. If the status is anything else, append a skipped record with the row number and reason, then continue.
15. Add accepted stage names to `seen`.
16. Create the final execution order:
    - ready stages first
    - blocked stages after ready stages
    execution_order = []
    execution_order.extend(ready)
    execution_order.extend(blocked)
17. Store the final order in `result["execution_order"]`.
18. Return the `result` dictionary.

Expected output:
{
    "execution_order": ["validate", "verify", "deploy", "rollback"],
    "skipped": [
        {"row": 2, "reason": "stage already done"},
        {"row": 4, "reason": "missing stage name"},
        {"row": 7, "reason": "unknown status unknown"},
        {"row": 8, "reason": "record is not a dictionary"},
        {"row": 9, "reason": "duplicate stage"},
        {"row": 10, "reason": "missing status"},
    ],
}
"""

# Task: change plan organizer

data = [
    {"stage": " validate ", "status": "READY"},
    {"stage": "backup", "status": "done"},
    {"stage": " deploy ", "status": "blocked"},
    {"stage": "  ", "status": "ready"},
    {"stage": "verify", "status": "READY"},
    {"stage": "rollback", "status": "BLOCKED"},
    {"stage": "check", "status": "unknown"},
    ["not", "a", "dictionary"],
    {"stage": " validate ", "status": "READY"},
    {"stage": "post-check", "status": ""},
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
    result = {
        "execution_order": [],
        "skipped": [],
    }

    ready = []
    blocked = []
    seen = set()

    for index, record in enumerate(data, start=1):
        if not isinstance(record, dict):
            result["skipped"].append({
                "row": index,
                "reason": "record is not a dictionary",
            })
            continue

        stage = record.get("stage")
        status = record.get("status")

        if not isinstance(stage, str) or not stage.strip():
            result["skipped"].append({
                "row": index,
                "reason": "missing stage name",
            })
            continue

        if not isinstance(status, str) or not status.strip():
            result["skipped"].append({
                "row": index,
                "reason": "missing status",
            })
            continue

        stage = stage.strip().lower()
        status = status.strip().lower()

        if stage in seen:
            result["skipped"].append({
                "row": index,
                "reason": "duplicate stage",
            })
            continue

        if status == "ready":
            ready.append(stage)
            seen.add(stage)
            continue

        if status == "blocked":
            blocked.append(stage)
            seen.add(stage)
            continue

        if status == "done":
            result["skipped"].append({
                "row": index,
                "reason": "stage already done",
            })
            continue

        result["skipped"].append({
            "row": index,
            "reason": f"unknown status {status}",
        })

    execution_order = []
    execution_order.extend(ready)
    execution_order.extend(blocked)

    result["execution_order"] = execution_order

    return result
"""
