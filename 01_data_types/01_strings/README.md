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

---

## Recommended Learning Order

### Essential

```python
s.split()
s.partition()
s.strip()
s.lower()
s.upper()
s.replace()
s.startswith()
s.endswith()
s.find()
s.count()
s.join()
```

### Intermediate

```python
s.index()
s.rsplit()
s.rpartition()
s.isdigit()
s.isalpha()
s.isalnum()
s.zfill()
s.title()
s.splitlines()
```

### Advanced

```python
s.removeprefix()
s.removesuffix()
s.capitalize()
s.swapcase()
s.casefold()
s.translate()
str.maketrans()
s.center()
s.ljust()
s.rjust()
s.format()
s.format_map()
s.encode()
```

### Rarely Used

```python
s.rfind()
s.rindex()
s.isspace()
s.istitle()
s.isascii()
s.isidentifier()
s.isdecimal()
s.isnumeric()
s.isprintable()
```