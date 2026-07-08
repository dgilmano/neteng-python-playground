# Python Lists

## Theory

A list (`list`) is an ordered collection of items.

Each item has its own position, called an **index**.

Lists are mutable, which means they can be changed after they are created.

They are commonly used for:

- command queues
- parsed table rows
- inventory batches
- ordered reports
- rolling windows of measurements

## Common List Operations

- access items by index
- slice ordered data
- append or insert new work items
- extend one list with another
- sort and select records
- flatten nested batches
- deduplicate while preserving order
- combine parallel lists

## Practice Tasks

These exercises are designed to feel more like real network automation work than simple one-liners. They combine list mutation, filtering, ordering, grouping, and structured processing.

| # | File | Scenario | Main Methods |
|---|---|---|---|
| 001 | `001_interface_inventory_filter.py` | Filter operational physical interfaces | `append()`, `continue`, filtering |
| 002 | `002_vlan_command_builder.py` | Generate normalized VLAN CLI commands | `append()`, `zfill()` |
| 003 | `003_maintenance_queue_update.py` | Update a maintenance queue with priorities and cleanup work | `insert()`, `append()`, membership |
| 004 | `004_route_metric_top_three.py` | Choose the best active routes by metric | `sorted()`, `lambda`, slicing |
| 005 | `005_neighbor_row_report.py` | Convert neighbor rows into readable link strings | indexing, `append()`, filtering |
| 006 | `006_flatten_command_batches.py` | Flatten nested command batches | `extend()`, nested lists |
| 007 | `007_sliding_error_windows.py` | Calculate rolling error totals | `range()`, slicing, `sum()` |
| 008 | `008_deduplicate_devices_order.py` | Deduplicate devices while preserving first-seen order | `set()`, membership, `append()` |
| 009 | `009_zip_interface_descriptions.py` | Combine parallel lists into structured records | `zip()`, `append()` |
| 010 | `010_change_plan_stages.py` | Partition change stages into ready and blocked work | `append()`, `extend()` |
