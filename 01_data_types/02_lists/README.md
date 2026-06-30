# Python Lists

## Theory

A list (`list`) is an ordered collection of items.

Each item has its own position, called an **index**.

Lists are used to store multiple values in one variable, for example:

- command queues
- parsed table rows
- inventory batches
- counters
- ordered reports

Lists in Python are **mutable**, which means they can be changed after they are created.

### Properties

- Access a single item using **indexing**.
- Access a part of a list using **slicing**.
- The first item has index `0`.
- Lists preserve the order of items.

### Mutability

A list is a mutable object, you can modify them directly.

- You can replace an item by index.
- You can add new items with methods like `append()`, `extend()`, and `insert()`.
- You can remove items with methods like `remove()`, `pop()`, and `clear()`.
- Methods like `append()`, `extend()`, `insert()`, `sort()`, and `reverse()` change the list in place.
- Functions like `sorted()` return a new list and do not change the original list.
- A list can contain different data types, but in practice it is usually cleaner to keep one type of data per list.
- If two variables point to the same list, changes through one variable are visible through the other.
- To create a separate copy, use `copy()`, slicing, or `list()`.

Example:

```python
interfaces = ["Gi0/1", "Gi0/2", "Gi0/3"]

# Replace an item
interfaces[0] = "Gi0/10"

# Add a new item
interfaces.append("Gi0/4")

print(interfaces)
# ['Gi0/10', 'Gi0/2', 'Gi0/3', 'Gi0/4']
```

## Common Lists Operations

- access items by index
- slice ordered data
- append or insert new work items
- extend one list with another
- sort and select records
- flatten nested batches
- deduplicate while preserving order
- combine parallel lists
---

## List Methods

### Adding Items

```python
data.append(item)           # Add an item to the end of the list.
data.extend(items)          # Add all items from another iterable.
data.insert(index, item)    # Insert an item at the specified index.
```

### Removing Items

```python
data.pop()                  # Remove and return the last item.
data.pop(index)             # Remove and return the item at the given index.
data.remove(item)           # Remove the first matching item.
data.clear()                # Remove all items from the list.
```

### Searching and Counting

```python
data.index(item)            # Return the index of the first matching item.
data.count(item)            # Count occurrences of an item.
```

### Sorting and Reversing

```python
data.sort()                 # Sort the list in place.
data.sort(reverse=True)     # Sort the list in descending order.
data.reverse()              # Reverse the list in place.
sorted(data)                # Return a new sorted list.
reversed(data)              # Return a reverse iterator.
```

### Copying

```python
data.copy()                 # Create a shallow copy of the list.
list(data)                  # Create a shallow copy using the constructor.
data[:]                     # Create a shallow copy using slicing.
```

### Indexing and Slicing

```python
data[0]                     # Access the first item.
data[-1]                    # Access the last item.
data[1:4]                   # Slice items from index 1 to 3.
data[:3]                    # Slice the first three items.
data[3:]                    # Slice from index 3 to the end.
data[::2]                   # Slice every second item.
```

### Membership

```python
item in data                # Check whether an item exists.
item not in data            # Check whether an item does not exist.
```

### Iteration

```python
for item in data            # Iterate over list items.
enumerate(data)             # Iterate with index.
zip(list_a, list_b)         # Iterate over multiple lists together.
```

### Built-in Functions

```python
len(data)                   # Return the number of items.
min(data)                   # Return the smallest item.
max(data)                   # Return the largest item.
sum(data)                   # Return the sum of numeric items.
any(data)                   # Return True if any item is truthy.
all(data)                   # Return True if all items are truthy.
```

## Practice Tasks

These exercises focus on realistic network automation workflows.
Each task combines core `lists` operations with loops, conditions, and structured output.

| # | File | Scenario | Main Methods |
|---|---|---|---|
| 001 | `001_interface_inventory_filter.py` | Filter usable physical interfaces | `append()`, indexing, loop filtering |
| 002 | `002_vlan_command_builder.py` | Build ordered VLAN config commands | `append()`, loop, `zfill()` |
| 003 | `003_maintenance_queue_update.py` | Insert and append maintenance jobs | `insert()`, `append()` |
| 004 | `004_route_metric_top_three.py` | Sort candidate routes by metric | `sorted()`, `lambda`, slicing |
| 005 | `005_neighbor_row_report.py` | Read columns from neighbor rows | indexing, `append()`, loop |
| 006 | `006_flatten_command_batches.py` | Flatten nested command batches | `extend()`, nested lists |
| 007 | `007_sliding_error_windows.py` | Calculate rolling error totals | `range()`, slicing, `sum()` |
| 008 | `008_deduplicate_devices_order.py` | Remove duplicate inventory entries | `append()`, `set()`, membership |
| 009 | `009_zip_interface_descriptions.py` | Combine parallel interface lists | `zip()`, `append()` |
| 010 | `010_change_plan_stages.py` | Build an ordered execution plan | `append()`, `extend()`, stable partition |
