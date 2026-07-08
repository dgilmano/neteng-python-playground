"""
Task 5: Device reachability digest

Methods to practice:
- for
- enumerate()
- append()
- .get()
- .strip()
- .lower()
- .upper()
- isinstance()
- float()
- continue
- structured output

Use Case:
A network monitoring job collects ping results from multiple devices every few minutes.
Some records arrive with missing fields, invalid values, or inconsistent formatting.
A production script should clean good records, skip bad ones, and keep an audit trail of why each row was ignored.

Rules:
1. Create an empty dictionary called `result` with two keys:
   - `"processed"` for valid reachability records
   - `"skipped"` for records that were ignored
   Example:
   result = {"processed": [], "skipped": []}
2. Create a loop that iterates through every record in `data`.
   Use `enumerate()` so each skipped record can include the original row number.
   Example:
   for index, record in enumerate(data, start=1):
3. Check whether the current item is a dictionary.
   If it is not, append a skipped record with a reason and continue.
   Why: production input is sometimes malformed, and the script should fail safely.
4. Read the needed values using `.get()`.
   This is safer than direct indexing because missing keys do not crash the script.
   Example:
   device = record.get("device")
5. Validate the required fields before processing.
   Each field should be a non-empty string after `.strip()`.
   If a field is missing or blank, append a skipped record with a reason and continue.
   Why: a reachability entry without a device or IP address cannot be trusted.
6. Normalize the values once they pass validation.
   Use `.strip()` to remove extra spaces, then `.upper()` for the device name.
   Use `.strip()` for the IP address and `.lower()` for the status.
   Why: normalized values make later reporting predictable.
7. Check whether the status is `"reachable"`.
   If it is not, append a skipped record with a reason and continue.
   Why: the report should contain only successful reachability results.
8. Convert latency and packet loss to numbers.
   If either value cannot be converted, append a skipped record with a reason and continue.
   Why: numeric values are needed for a useful summary.
9. Validate the numeric range.
   Accept packet loss only if it is between `0` and `100`.
   If it is outside that range, append a skipped record with a reason and continue.
10. Build a clean summary string for the valid record.
    Example format:
    "R1 10.0.0.1 reachable 12.5ms 0.0%"
11. Append the normalized record to `result["processed"]`.
    Each processed record should include the normalized fields and the summary string.
12. After the loop, return the `result` dictionary.

Expected result:
{
    "processed": [
        {
            "device": "R1",
            "ip": "10.0.0.1",
            "status": "reachable",
            "latency_ms": 12.5,
            "packet_loss": 0.0,
            "summary": "R1 10.0.0.1 reachable 12.5ms 0.0%",
        },
        {
            "device": "SW1",
            "ip": "10.0.0.2",
            "status": "reachable",
            "latency_ms": 20.0,
            "packet_loss": 0.5,
            "summary": "SW1 10.0.0.2 reachable 20.0ms 0.5%",
        },
    ],
    "skipped": [
        {"row": 3, "reason": "missing IP address"},
        {"row": 4, "reason": "status is timeout"},
        {"row": 5, "reason": "invalid latency"},
        {"row": 6, "reason": "packet loss out of range"},
        {"row": 7, "reason": "missing device"},
        {"row": 8, "reason": "record is not a dictionary"},
    ],
}
"""

# Task: device reachability digest
data = [
    {
        "device": " r1 ",
        "ip": "10.0.0.1",
        "status": "reachable",
        "latency_ms": "12.5",
        "packet_loss": "0",
    },
    {
        "device": " sw1 ",
        "ip": "10.0.0.2",
        "status": "Reachable",
        "latency_ms": "20",
        "packet_loss": "0.5",
    },
    {
        "device": "r2",
        "ip": "",
        "status": "reachable",
        "latency_ms": "8",
        "packet_loss": "0",
    },
    {
        "device": "r3",
        "ip": "10.0.0.3",
        "status": "timeout",
        "latency_ms": "15",
        "packet_loss": "0",
    },
    {
        "device": "r4",
        "ip": "10.0.0.4",
        "status": "reachable",
        "latency_ms": "N/A",
        "packet_loss": "0",
    },
    {
        "device": "r5",
        "ip": "10.0.0.5",
        "status": "reachable",
        "latency_ms": "10",
        "packet_loss": "150",
    },
    {
        "device": "",
        "ip": "10.0.0.6",
        "status": "reachable",
        "latency_ms": "7",
        "packet_loss": "0",
    },
    ["not", "a", "dictionary"],
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
    result = {"processed": [], "skipped": []}

    for index, record in enumerate(data, start=1):
        if not isinstance(record, dict):
            result["skipped"].append({
                "row": index,
                "reason": "record is not a dictionary",
            })
            continue

        device = record.get("device")
        ip_address = record.get("ip")
        status = record.get("status")
        latency_ms = record.get("latency_ms")
        packet_loss = record.get("packet_loss")

        if not isinstance(device, str) or not device.strip():
            result["skipped"].append({"row": index, "reason": "missing device"})
            continue

        if not isinstance(ip_address, str) or not ip_address.strip():
            result["skipped"].append({"row": index, "reason": "missing IP address"})
            continue

        if not isinstance(status, str) or not status.strip():
            result["skipped"].append({"row": index, "reason": "missing status"})
            continue

        device = device.strip().upper()
        ip_address = ip_address.strip()
        status = status.strip().lower()

        if status != "reachable":
            result["skipped"].append({"row": index, "reason": f"status is {status}"})
            continue

        try:
            latency_value = float(latency_ms)
        except (TypeError, ValueError):
            result["skipped"].append({"row": index, "reason": "invalid latency"})
            continue

        if latency_value < 0:
            result["skipped"].append({"row": index, "reason": "latency out of range"})
            continue

        try:
            loss_value = float(packet_loss)
        except (TypeError, ValueError):
            result["skipped"].append({"row": index, "reason": "invalid packet loss"})
            continue

        if not 0 <= loss_value <= 100:
            result["skipped"].append({"row": index, "reason": "packet loss out of range"})
            continue

        result["processed"].append({
            "device": device,
            "ip": ip_address,
            "status": status,
            "latency_ms": latency_value,
            "packet_loss": loss_value,
            "summary": f"{device} {ip_address} {status} {latency_value}ms {loss_value}%",
        })

    return result
"""
