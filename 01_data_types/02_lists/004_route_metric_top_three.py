"""
Task 4: Route metric top three

Methods to practice:
- sorted()
- lambda key
- slicing

Use Case:
Route analysis often ranks candidate next hops by metric.
Return the three best route candidates ordered by metric from lowest to highest.

Rules:
1. Use the `sorted()` function to create a new sorted list.
2. Do not use `data.sort()` because it changes the original list in place.
3. Sort routes by the `"metric"` field using a `lambda` key:
   sorted_routes = sorted(data, key=lambda route: route["metric"])
4. Store the sorted result in a variable such as `sorted_routes`.
5. Use slicing to get only the first three routes:
   sorted_routes[:3]
6. Return the sliced list.

Expected result:
- [{'prefix': '10.0.2.0/24', 'next_hop': 'wan3', 'metric': 5}, {'prefix': '10.0.0.0/24', 'next_hop': 'wan1', 'metric': 10}, {'prefix': '10.0.1.0/24', 'next_hop': 'wan2', 'metric': 20}]
"""

# Task: route metric top three

data = [
    {'prefix': '10.0.0.0/24', 'next_hop': 'wan1', 'metric': 10},
    {'prefix': '10.0.1.0/24', 'next_hop': 'wan2', 'metric': 20},
    {'prefix': '10.0.2.0/24', 'next_hop': 'wan3', 'metric': 5},
    {'prefix': '10.0.3.0/24', 'next_hop': 'wan4', 'metric': 50},
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
    sorted_routes = sorted(data, key=lambda route: route['metric'])
    return sorted_routes[:3]
"""
