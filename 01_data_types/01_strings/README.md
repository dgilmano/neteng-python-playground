# Python Strings

## Theory

A string (`str`) is an immutable sequence of Unicode characters.

Strings are used to store and process text data such as hostnames, interface names, IP addresses, configuration lines, CLI commands, log messages, and user input.

Because strings are immutable, string methods do not modify the original string. Instead, they return a new string object.

Strings support:

- indexing
- slicing
- iteration
- comparison
- searching
- formatting

Many automation tasks rely heavily on string processing because network devices, APIs, configuration files, and logs represent information as text.

## Common String Operations

- normalize text
- split text into parts
- search for patterns
- replace text
- validate content
- extract information
- format output

## Practice Tasks

These exercises focus on realistic string parsing for network automation.
Each task combines several methods and also trains loops, conditions, indexes,
slicing, validation, normalization, and structured output.

| # | File | Scenario | Main Methods |
|---|---|---|---|
| 001 | `001_interface_brief_inventory.py` | Parse interface brief output | `splitlines()`, `strip()`, `split()`, `lower()`, `replace()`, `startswith()` |
| 002 | `002_vlan_allowed_expander.py` | Expand trunk allowed VLAN ranges | `partition()`, `split()`, `strip()`, `replace()`, `isdigit()`, `zfill()` |
| 003 | `003_acl_rule_parser.py` | Parse ACL lines with optional ports | `splitlines()`, `strip()`, `startswith()`, `lower()`, `split()`, `isdigit()`, `count()` |
| 004 | `004_syslog_event_summary.py` | Extract link events from syslog | `find()`, `index()`, slicing, `partition()`, `rpartition()`, `endswith()` |
| 005 | `005_interface_name_report.py` | Normalize interface names for reports | `split()`, `strip()`, `replace()`, `rsplit()`, `isdigit()`, `zfill()`, `join()` |
| 006 | `006_neighbor_table_parser.py` | Parse neighbor discovery table | `splitlines()`, `split()`, `startswith()`, `isalnum()`, `isalpha()`, `upper()`, `lower()`, `title()` |
| 007 | `007_config_block_extractor.py` | Extract one interface config block | `splitlines()`, `strip()`, `startswith()`, `lower()`, `join()` |
| 008 | `008_prompt_command_audit.py` | Audit dangerous config-mode commands | `partition()`, `startswith()`, `endswith()`, `lower()`, `count()` |
| 009 | `009_address_cleanup_validator.py` | Validate IP and MAC inventory data | `partition()`, `count()`, `split()`, `isdigit()`, `replace()`, `lower()`, `isalnum()` |
| 010 | `010_change_report_builder.py` | Build a clean change report | `splitlines()`, `strip()`, `split()`, `rsplit()`, `lower()`, `upper()`, `title()`, `endswith()`, `join()` |

---

## String Methods

### Case Conversion

```python
s.lower()
s.upper()
s.capitalize()
s.title()
s.swapcase()
s.casefold()
```

### Trimming and Removing

```python
s.strip()
s.lstrip()
s.rstrip()
s.removeprefix()
s.removesuffix()
```

### Searching and Counting

```python
s.find()
s.rfind()
s.index()
s.rindex()
s.count()
```

### Prefix and Suffix Checks

```python
s.startswith()
s.endswith()
```

### Splitting

```python
s.split()
s.rsplit()
s.partition()
s.rpartition()
s.splitlines()
```

### Joining

```python
s.join()
```

### Replacing and Translating

```python
s.replace()
s.translate()
str.maketrans()
```

### Content Checks

```python
s.isalpha()
s.isdigit()
s.isalnum()
s.islower()
s.isupper()
s.isspace()
s.istitle()
s.isascii()
s.isidentifier()
s.isdecimal()
s.isnumeric()
s.isprintable()
```

### Alignment and Padding

```python
s.center()
s.ljust()
s.rjust()
s.zfill()
```

### Formatting

```python
s.format()
s.format_map()
```

### Encoding

```python
s.encode()
```
