"""
Task 7: Rolling error windows

Methods to practice:
- range()
- slicing
- sum()
- append()
- isinstance()
- continue
- structured output
- min()
- max()

Use Case:
Monitoring dashboards often inspect rolling windows of recent error counters.
Some samples may be missing, malformed, negative, or too high to be trusted.
A production script should validate each window, skip bad windows, and keep an audit trail.

Rules:
1. Create an empty dictionary called `result` with two keys:
   - `"windows"` for valid rolling windows.
   - `"skipped"` for windows that could not be calculated.
   result = {"windows": [], "skipped": []}
2. Create a variable `window_size` with the value `3`.
3. Use `range()` to iterate over every valid starting position:
   for start in range(len(data) - window_size + 1):
4. Create a 3-item slice for the current window:
   window = data[start:start + window_size]
5. Calculate the end index for the current window:
   end = start + window_size - 1
6. Validate every value in the window.
   Each value must be:
   - an integer
   - greater than or equal to `0`
   - less than or equal to `1000`
7. If the window contains a value that is not an integer, append a skipped record with the reason `"window contains non-integer value"` and continue.
8. If the window contains a negative value, append a skipped record with the reason `"window contains negative value"` and continue.
9. If the window contains a value greater than `1000`, append a skipped record with the reason `"window contains out-of-range value"` and continue.
10. Calculate the total number of errors in the valid window using `sum()`.
11. Append the window details to `result["windows"]`.
    Include:
    - `start`
    - `end`
    - `samples`
    - `total`
    - `min`
    - `max`
12. After the loop, return the `result` dictionary.

Expected output:
{
    "windows": [
        {"start": 0, "end": 2, "samples": [3, 0, 2], "total": 5, "min": 0, "max": 3},
        {"start": 6, "end": 8, "samples": [1, 3, 2], "total": 6, "min": 1, "max": 3},
    ],
    "skipped": [
        {"start": 1, "end": 3, "samples": [0, 2, "bad"], "reason": "window contains non-integer value"},
        {"start": 2, "end": 4, "samples": [2, "bad", -1], "reason": "window contains non-integer value"},
        {"start": 3, "end": 5, "samples": ["bad", -1, 1200], "reason": "window contains non-integer value"},
        {"start": 4, "end": 6, "samples": [-1, 1200, 1], "reason": "window contains negative value"},
        {"start": 5, "end": 7, "samples": [1200, 1, 3], "reason": "window contains out-of-range value"},
    ],
}
"""

# Task: rolling error windows

data = [3, 0, 2, "bad", -1, 1200, 1, 3, 2]

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
        "windows": [],
        "skipped": [],
    }

    window_size = 3

    for start in range(len(data) - window_size + 1):
        window = data[start:start + window_size]
        end = start + window_size - 1

        has_non_integer = False
        has_negative = False
        has_out_of_range = False

        for value in window:
            if not isinstance(value, int):
                has_non_integer = True
                break

            if value < 0:
                has_negative = True
                break

            if value > 1000:
                has_out_of_range = True
                break

        if has_non_integer:
            result["skipped"].append({
                "start": start,
                "end": end,
                "samples": window,
                "reason": "window contains non-integer value",
            })
            continue

        if has_negative:
            result["skipped"].append({
                "start": start,
                "end": end,
                "samples": window,
                "reason": "window contains negative value",
            })
            continue

        if has_out_of_range:
            result["skipped"].append({
                "start": start,
                "end": end,
                "samples": window,
                "reason": "window contains out-of-range value",
            })
            continue

        result["windows"].append({
            "start": start,
            "end": end,
            "samples": window,
            "total": sum(window),
            "min": min(window),
            "max": max(window),
        })

    return result
"""
