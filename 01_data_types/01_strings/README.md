# Python Strings

## Theory

A string (`str`) is an ordered sequence of characters used to store and process text data.

Each character in a string has its own position, called an **index**.

Strings in Python are **immutable**, which means they cannot be changed after they are created.

- Access a single character using **indexing**.
- Access a part of a string using **slicing**.
- The first character has index `0`.

### String Immutability

A string is an immutable object. This means you cannot modify an existing string directly.

- You cannot change a single character or part of a string.
- Operations that appear to modify a string actually create and return a new string.
- To "change" a string, assign the new value to a variable.

Example:

```python
text = "hello"

# Creates a new string
text = text.upper()

print(text)
# HELLO
```

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

---

## String Methods

### Case Conversion

```python
s.lower()         # Convert all characters to lowercase.
s.upper()         # Convert all characters to uppercase.
s.capitalize()    # Capitalize the first character.
s.title()         # Capitalize the first letter of each word.
s.swapcase()      # Swap lowercase and uppercase characters.
s.casefold()      # Aggressive lowercase conversion for case-insensitive comparisons.
```

### Trimming and Removing

```python
s.strip()         # Remove leading and trailing whitespace.
s.lstrip()        # Remove leading whitespace.
s.rstrip()        # Remove trailing whitespace.
s.removeprefix()  # Remove the specified prefix.
s.removesuffix()  # Remove the specified suffix.
```

### Searching and Counting

```python
s.find()          # Find the first occurrence or return -1.
s.rfind()         # Find the last occurrence or return -1.
s.index()         # Find the first occurrence or raise ValueError.
s.rindex()        # Find the last occurrence or raise ValueError.
s.count()         # Count occurrences of a substring.
```

### Prefix and Suffix Checks

```python
s.startswith()    # Check whether the string starts with a prefix.
s.endswith()      # Check whether the string ends with a suffix.
```

### Splitting

```python
s.split()         # Split the string into a list.
s.rsplit()        # Split from the right.
s.partition()     # Split into three parts at the first separator.
s.rpartition()    # Split into three parts at the last separator.
s.splitlines()    # Split into lines.
```

### Joining

```python
s.join()          # Join iterable elements into a single string.
```

### Replacing and Translating

```python
s.replace()       # Replace occurrences of a substring.
s.translate()     # Replace characters using a translation table.
str.maketrans()   # Create a translation table.
```

### Content Checks

```python
s.isalpha()       # Only alphabetic characters.
s.isdigit()       # Only digit characters.
s.isalnum()       # Only letters and digits.
s.islower()       # All cased characters are lowercase.
s.isupper()       # All cased characters are uppercase.
s.isspace()       # Only whitespace characters.
s.istitle()       # Title Case string.
s.isascii()       # Only ASCII characters.
s.isidentifier()  # Valid Python identifier.
s.isdecimal()     # Only decimal digits.
s.isnumeric()     # Only numeric characters.
s.isprintable()   # Only printable characters.
```

### Alignment and Padding

```python
s.center()        # Center the string.
s.ljust()         # Left-align the string.
s.rjust()         # Right-align the string.
s.zfill()         # Pad with leading zeros.
```

### Formatting

```python
s.format()        # Format a string using placeholders.
s.format_map()    # Format using a mapping (dictionary).
```

### Encoding

```python
s.encode()        # Encode the string into bytes.
```
---

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