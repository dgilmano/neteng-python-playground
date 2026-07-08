"""
Task 9: Interface description combiner

Methods to practice:
- zip()
- enumerate()
- append()
- isinstance()
- len()
- .strip()
- .upper()
- .lower()
- continue
- structured output

Use Case:
Sometimes interface inventory data arrives from three different sources as parallel lists.
In real automation, these lists may have different lengths, blank values, invalid item types, or inconsistent formatting.
A production script should combine only valid rows, normalize values, and keep an audit trail for skipped rows.

Rules:
1. Create an empty dictionary called `result` with two keys:
   - `"records"` for valid combined rows.
   - `"skipped"` for incomplete or invalid rows.
2. Check that `data` contains exactly three lists:
   - `interfaces`
   - `descriptions`
   - `roles`
3. If `data` is not valid, return a structured result with the reason in `skipped`.
4. Unpack `data` into three variables:
   interfaces, descriptions, roles = data
5. Calculate the longest list length.
   Why: `zip()` stops at the shortest list, but production code should report missing values.
6. Iterate by index over the longest list using `range()`.
7. Safely read values from each list.
   If a value does not exist, use an empty string.
8. Check that interface, description, and role are strings.
   If not, append a skipped record with the row number and reason, then continue.
9. Normalize values:
   - interface → `strip().upper()`
   - description → `strip()`
   - role → `strip().lower()`
10. Skip rows where any normalized value is empty.
11. Create a dictionary for the valid row with:
    - `"interface"`
    - `"description"`
    - `"role"`
12. Append the dictionary to `result["records"]`.
13. After the loop, return the `result` dictionary.

Expected output:
{
    "records": [
        {"interface": "GI0/1", "description": "uplink", "role": "core"},
        {"interface": "GI0/2", "description": "server", "role": "access"},
    ],
    "skipped": [
        {"row": 3, "reason": "incomplete row"},
        {"row": 4, "reason": "incomplete row"},
        {"row": 5, "reason": "invalid value type"},
    ],
}
"""

# Task: interface description combiner

data = (
    ["Gi0/1", " Gi0/2 ", "Gi0/3", "Gi0/4", 100],
    ["uplink", "server", " ", "firewall"],
    ["core", "access", "edge"],
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
    result = {
        "records": [],
        "skipped": [],
    }

    if not isinstance(data, tuple) or len(data) != 3:
        result["skipped"].append({
            "row": None,
            "reason": "input must contain three lists",
        })
        return result

    interfaces, descriptions, roles = data

    if (
        not isinstance(interfaces, list)
        or not isinstance(descriptions, list)
        or not isinstance(roles, list)
    ):
        result["skipped"].append({
            "row": None,
            "reason": "input values must be lists",
        })
        return result

    max_length = max(len(interfaces), len(descriptions), len(roles))

    for index in range(max_length):
        interface = interfaces[index] if index < len(interfaces) else ""
        description = descriptions[index] if index < len(descriptions) else ""
        role = roles[index] if index < len(roles) else ""

        row_number = index + 1

        if (
            not isinstance(interface, str)
            or not isinstance(description, str)
            or not isinstance(role, str)
        ):
            result["skipped"].append({
                "row": row_number,
                "reason": "invalid value type",
            })
            continue

        interface = interface.strip().upper()
        description = description.strip()
        role = role.strip().lower()

        if not interface or not description or not role:
            result["skipped"].append({
                "row": row_number,
                "reason": "incomplete row",
            })
            continue

        result["records"].append({
            "interface": interface,
            "description": description,
            "role": role,
        })

    return result
"""
