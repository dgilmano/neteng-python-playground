"""
Task 6: Command batch flattener

Methods to practice:
- for
- nested loops
- enumerate()
- append()
- extend()
- .get()
- isinstance()
- .strip()
- .lower()
- continue
- membership checks
- structured output

Use Case:
In a real automation runbook, commands often arrive in batches from different modules.
Some batches may be malformed, some commands may be blank, duplicated, or unsafe.
A production script should normalize useful commands, skip bad ones, avoid duplicates, and keep an audit trail.

Rules:
1. Create an empty dictionary called `result` with two keys:
   - `"processed"` for valid commands.
   - `"skipped"` for invalid or skipped items.
   result = {"processed": [], "skipped": []}
2. Create an empty set called `seen` to track duplicate commands.
3. Create a loop that iterates through every batch in `data`.
   Use `enumerate()` so every skipped record can include the original batch number.
   for batch_index, batch in enumerate(data, start=1):
4. Check whether the current batch is a list.
   If it is not, append a skipped record with the batch number and reason, then continue.
5. Create an empty list called `valid_commands` for valid commands from the current batch.
6. Create a nested loop that iterates through every command in the current batch.
   Use `enumerate()` so every skipped command can include the original command number.
   for command_index, command in enumerate(batch, start=1):
7. Check whether the command is a string.
   If it is not, append a skipped record with the batch number, command number, and reason, then continue.
8. Normalize the command:
   - remove leading and trailing spaces using `strip()`.
   - convert it to lowercase using `lower()`.
9. Skip blank commands. Append the batch number, command number, and reason to `result["skipped"]`.
10. Skip duplicate commands while keeping the first occurrence.
    Append the batch number, command number, and reason to `result["skipped"]`.
11. Skip unsafe commands that start with:
    - `"reload"`
    - `"write erase"`
    - `"delete"`
12. Add valid commands to `seen`.
13. Append valid commands from the current batch to `valid_commands`.
14. After processing the current batch, extend `result["processed"]` with `valid_commands`:
    result["processed"].extend(valid_commands)
15. After all batches are processed, return the `result` dictionary.

Expected output:
{
    "processed": [
        "terminal length 0",
        "show clock",
        "show ip interface brief",
        "show version",
        "show inventory",
    ],
    "skipped": [
        {"batch": 1, "command": 3, "reason": "blank command"},
        {"batch": 2, "command": 2, "reason": "command is not a string"},
        {"batch": 3, "command": 3, "reason": "duplicate command"},
        {"batch": 4, "reason": "batch is not a list"},
        {"batch": 5, "command": 1, "reason": "unsafe command"},
    ],
}
"""

# Task: command batch flattener

data = [
    ["terminal length 0", " show clock ", ""],
    ["show ip interface brief", None],
    ["show version", "show inventory", " SHOW CLOCK "],
    "not-a-list",
    ["reload now", " show running-config "],
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
        "processed": [],
        "skipped": [],
    }
    seen = set()

    for batch_index, batch in enumerate(data, start=1):
        if not isinstance(batch, list):
            result["skipped"].append({
                "batch": batch_index,
                "reason": "batch is not a list",
            })
            continue
        valid_commands = []

        for command_index, command in enumerate(batch, start=1):
            if not isinstance(command, str):
                result["skipped"].append({
                    "batch": batch_index,
                    "command": command_index,
                    "reason": "command is not a string",
                })
                continue

            command = command.strip().lower()

            if not command:
                result["skipped"].append({
                    "batch": batch_index,
                    "command": command_index,
                    "reason": "blank command",
                })
                continue

            if command in seen:
                result["skipped"].append({
                    "batch": batch_index,
                    "command": command_index,
                    "reason": "duplicate command",
                })
                continue

            if (
                command.startswith("reload")
                or command.startswith("write erase")
                or command.startswith("delete")
            ):
                result["skipped"].append({
                    "batch": batch_index,
                    "command": command_index,
                    "reason": "unsafe command",
                })
                continue

            seen.add(command)
            valid_commands.append(command)

        result["processed"].extend(valid_commands)

    return result
"""
