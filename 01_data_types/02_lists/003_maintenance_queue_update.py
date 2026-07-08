"""
Task 3: Maintenance queue update

Methods to practice:
- insert()
- append()
- continue
- membership checks
- duplicate removal
- strip()
- lower()
- set()

Use Case:
Maintenance queues often contain duplicate jobs, inconsistent formatting, empty records, and invalid items.
Update the queue while keeping job order, adding mandatory jobs, and reporting skipped records.

Rules:
1. Create an empty list `queue` for valid jobs.
2. Create an empty set `seen` to track duplicate job names.
3. Create an empty list `skipped` to store skipped records and reasons.
4. Iterate through every job in `data`.
5. Skip values that are not strings. Save the reason in `skipped`.
6. Normalize each job using `strip()` and `lower()`.
7. Skip empty jobs. Save the reason in `skipped`.
8. Skip duplicate jobs while keeping the first occurrence. Save the reason in `skipped`.
9. Add valid unique jobs to `queue`.
10. Insert `emergency-core` at the beginning if it is not already present.
11. Append `post-check` at the end if it is not already present.
12. Return a dictionary containing:
    - `queue`
    - `skipped`
    - `total_jobs`

Expected result:
{
    'queue': ['emergency-core', 'backup-core', 'audit-fw', 'post-check'],
    'skipped': [
        {'job': ' backup-core ', 'reason': 'duplicate'},
        {'job': '', 'reason': 'empty job'},
        {'job': None, 'reason': 'not a string'}
    ],
    'total_jobs': 4
}
"""

data = [
    'backup-core',
    'audit-fw',
    ' backup-core ',
    '',
    None,
]

def solve(data):
    queue = []
    seen = set()
    skipped = []
    for job in data:
        if not isinstance(job, str):
            skipped.append({
                'job': job,
                'reason': 'not string'
            })
            continue
        job_strip = job.strip().lower()
        if not job_strip:
            skipped.append({
                'job': job,
                'reason': 'empty job'
            })
            continue
        if job_strip in seen:
            skipped.append({
                'job': job,
                'reason': 'duplicate'
            })
            continue
        seen.add(job_strip)
        queue.append(job_strip)
    if 'emergency-core' not in seen:
        queue.insert(0, 'emergency-core')
    if 'post-check' not in seen:
        queue.append('post-check')
    
    return {
        'queue': queue,
        'skipped': skipped,
        'total_jobs': len(queue)
    }
        

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
    queue = []
    seen = set()
    skipped = []
    for job in data:
        if not isinstance(job, str):
            skipped.append({
                'job': job,
                'reason': 'not a string'
            })
            continue
        normalized_job = job.strip().lower()
        if not normalized_job:
            skipped.append({
                'job': job,
                'reason': 'empty job'
            })
            continue

        if normalized_job in seen:
            skipped.append({
                'job': job,
                'reason': 'duplicate'
            })
            continue
        seen.add(normalized_job)
        queue.append(normalized_job)

    if 'emergency-core' not in seen:
        queue.insert(0, 'emergency-core')

    if 'post-check' not in seen:
        queue.append('post-check')

    return {
        'queue': queue,
        'skipped': skipped,
        'total_jobs': len(queue)
    }
"""
