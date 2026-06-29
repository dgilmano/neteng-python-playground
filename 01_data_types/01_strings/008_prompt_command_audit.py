"""
Task 8: Prompt command audit

Methods to practice:
- splitlines(), strip(), partition(), startswith(), endswith(), lower(), count()

Use Case:
Session logs include prompts and commands mixed together.
Automation can audit whether dangerous commands were entered in configuration mode.

Rules:
1. Create an empty list `result`.
2. Split the input data into lines and iterate through each line:
   for line in data.splitlines():
3. Remove leading and trailing spaces from the current line:
   line = line.strip()
4. Skip empty lines and lines that do not contain exactly one `#` character:
   if not line or line.count("#") != 1:
       continue
5. Split the line into the prompt and command using `partition("#")`:
   prompt, separator, command = line.partition("#")
   Example:
   "SW1(config)#hostname SW1"
   prompt = "SW1(config)"
   separator = "#"
   command = "hostname SW1"
6. Remove leading and trailing spaces from the prompt. Convert the command to lowercase after removing leading and trailing spaces:
   prompt = prompt.strip()
   command = command.strip().lower()
7. Keep only configuration mode prompts:
   - `(config)`
   - `(config-if)`
   if not prompt.endswith("(config)") and not prompt.endswith("(config-if)"):
       continue
8. Check if the command starts with `"no "` or is equal to `"shutdown"`:
   if command.startswith("no ") or command == "shutdown":
9. Append the prompt and command to the `result` list:
   result.append(prompt + " : " + command)
   Example:
   SW1(config-if) : shutdown
10. Return the `result` list.

Expected result:
- ['SW1(config-if): shutdown', 'SW1(config): no router ospf 1']
"""

# Task: prompt command audit

data = """
SW1#show version
SW1(config-if)# shutdown
SW1(config)# no router ospf 1
SW1#show ip int brief
SW1 show ip int brief
SW1(config)#hostname SW1
"""

def solve(data):
    result = []
    for items in data.splitlines():
        items = items.strip().rstrip()
        if not items or items.find("#") == -1:
            continue
        prompt, symbol, command = items.partition("#")
        prompt = prompt.strip()
        command = command.strip().lower()

        if not prompt.endswith("(config)") and not prompt.endswith("(config-if)"):
            continue
        
        if command.startswith("no") or command == "shutdown":
            result.append(prompt + ": " + command)
    return result
        


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

    for line in data.splitlines():
        line = line.strip()
        if not line or line.count('#') != 1:
            continue

        prompt, separator, command = line.partition('#')
        prompt = prompt.strip()
        command = command.strip().lower()

        if not prompt.endswith('(config)') and not prompt.endswith('(config-if)'):
            continue

        if command.startswith('no ') or command == 'shutdown':
            result.append(prompt + ' : ' + command)

    return result
"""
