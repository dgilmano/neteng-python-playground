"""
Task 8: Device deduplicator

Methods to practice:
- for
- enumerate()
- set()
- append()
- .strip()
- .lower()
- .upper()
- isinstance()
- continue
- membership check
- structured output

Use Case:
Inventory exports from multiple collectors often contain duplicate hostnames.
Some records may be empty, malformed, or use inconsistent casing.
A production script should normalize names, remove duplicates while preserving first-seen order, and keep an audit trail.

Rules:
1. Create an empty dictionary called `result` with two keys:
   - `"devices"` for valid unique devices.
   - `"skipped"` for invalid or duplicate entries.
2. Create an empty set called `seen`.
3. Create a loop to iterate through every item in `data`.
   Use `enumerate()` so every skipped record can include the original row number.
4. Check whether the current item is a string.
   If not, append a skipped record with the row number and reason, then continue.
5. Remove leading and trailing spaces using `strip()`.
6. If the cleaned device name is empty, append a skipped record with the row number and reason, then continue.
7. Create a normalized name using `lower()` for duplicate detection.
8. If the normalized name is already in `seen`, append a skipped record with the row number and reason, then continue.
9. Add the normalized name to `seen`.
10. Append the cleaned device name to `result["devices"]`.
    Use `upper()` for readable and consistent output.
11. After the loop, return the `result` dictionary.

Expected output:
{
    "devices": ["R1", "SW1", "FW1", "R2"],
    "skipped": [
        {"row": 3, "reason": "duplicate device"},
        {"row": 4, "reason": "device is not a string"},
        {"row": 5, "reason": "blank device name"},
        {"row": 7, "reason": "duplicate device"},
        {"row": 9, "reason": "blank device name"},
    ],
}
"""

data = ["r1", " SW1 ", "R1", None, " ", "fw1", "sw1", "r2", ""]

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
        "devices": [],
        "skipped": [],
    }

    seen = set()

    for index, device in enumerate(data, start=1):
        if not isinstance(device, str):
            result["skipped"].append({
                "row": index,
                "reason": "device is not a string",
            })
            continue

        cleaned_device = device.strip()

        if not cleaned_device:
            result["skipped"].append({
                "row": index,
                "reason": "blank device name",
            })
            continue

        normalized_device = cleaned_device.lower()

        if normalized_device in seen:
            result["skipped"].append({
                "row": index,
                "reason": "duplicate device",
            })
            continue

        seen.add(normalized_device)
        result["devices"].append(cleaned_device.upper())

    return result
"""
