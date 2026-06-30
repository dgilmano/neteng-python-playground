"""
Task 7: Sliding error windows

Methods to practice:
- range()
- slicing
- sum()
- append()

Use Case:
Monitoring code often checks rolling windows of recent counters.
Return the sum of every 3-sample sliding window.

Rules:
1. Create a variable `result` as an empty list.
2. Create a variable `window_size` with the value `3`.
3. Use `range()` to loop over valid starting indexes:
   for index in range(len(data) - window_size + 1):
4. For each index, create a 3-item slice:
   window = data[index:index + window_size]
5. Calculate the sum of the current window using `sum(window)`.
6. Append the window sum to the `result` list using `result.append()`.
7. Return the `result` list after all windows are processed.

Expected result:
- [3, 8, 6, 8]
"""

# Task: sliding error windows

data = [0, 2, 1, 5, 0, 3]


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
    window_size = 3

    for index in range(len(data) - window_size + 1):
        window = data[index:index + window_size]
        result.append(sum(window))

    return result
"""
