"""
Task 4: Route metric top three
Methods to practice:
- sorted()
- lambda key
- slicing
- append()
- continue
- get()
- isinstance()
- filtering

Use Case:
Route selection often involves filtering invalid or inactive candidates, ranking active routes by metric, and breaking ties deterministically.
Return the best three active routes and report skipped routes.

Rules:
1. Create an empty list `candidates` for valid active routes.
2. Create an empty list `skipped` for skipped routes.
3. Iterate through every route in `data`.
4. Create variables for the fields you will use later:
   - `prefix`
   - `next_hop`
   - `metric`
   - `active`
5. Skip inactive routes. Save the reason in `skipped`.
6. Skip routes without `prefix` or `next_hop`. Save the reason in `skipped`.
7. Skip routes where `metric` is not an integer. Save the reason in `skipped`.
8. Append valid active routes to `candidates`.
9. Sort `candidates` by metric first and prefix second:
   sorted_routes = sorted(candidates, key=lambda route: (route["metric"], route["prefix"]))
10. Return only the first three routes using slicing:
   top_routes = sorted_routes[:3]
11. Return a dictionary containing:
   - `routes`
   - `skipped`
   - `total_active_candidates`

Expected result:
{
    "routes": [
        {"prefix": "10.0.2.0/24", "next_hop": "wan3", "metric": 5, "active": True},
        {"prefix": "10.0.5.0/24", "next_hop": "wan6", "metric": 5, "active": True},
        {"prefix": "10.0.0.0/24", "next_hop": "wan1", "metric": 10, "active": True}
    ],
    "skipped": [
        {"prefix": "10.0.4.0/24", "reason": "inactive"},
        {"prefix": "10.0.6.0/24", "reason": "invalid metric"},
        {"prefix": "", "reason": "missing prefix or next_hop"}
    ],
    "total_active_candidates": 4
}

"""

data = [
    {"prefix": "10.0.0.0/24", "next_hop": "wan1", "metric": 10, "active": True},
    {"prefix": "10.0.1.0/24", "next_hop": "wan2", "metric": 20, "active": True},
    {"prefix": "10.0.2.0/24", "next_hop": "wan3", "metric": 5, "active": True},
    {"prefix": "10.0.3.0/24", "next_hop": "wan4", "metric": 50, "active": True},
    {"prefix": "10.0.4.0/24", "next_hop": "wan5", "metric": 5, "active": False},
    {"prefix": "10.0.5.0/24", "next_hop": "wan6", "metric": 5, "active": True},
    {"prefix": "10.0.6.0/24", "next_hop": "wan7", "metric": "bad", "active": True},
    {"prefix": "", "next_hop": "wan8", "metric": 15, "active": True},
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
    candidates = []
    skipped = []

    for route in data:
        prefix = route.get("prefix", "").strip()
        next_hop = route.get("next_hop", "").strip()
        metric = route.get("metric")
        active = route.get("active", False)
        if not active:

            skipped.append({
                "prefix": prefix,
                "reason": "inactive"
            })
            continue

        if not prefix or not next_hop:
            skipped.append({
                "prefix": prefix,
                "reason": "missing prefix or next_hop"
            })
            continue

        if not isinstance(metric, int):
            skipped.append({
                "prefix": prefix,
                "reason": "invalid metric"
            })
            continue

        candidates.append({
            "prefix": prefix,
            "next_hop": next_hop,
            "metric": metric,
            "active": active,
        })

    sorted_routes = sorted(
        candidates,
        key=lambda route: (route["metric"], route["prefix"])
    )
    top_routes = sorted_routes[:3]

    return {
        "routes": top_routes,
        "skipped": skipped,
        "total_active_candidates": len(candidates)
    }
"""
