"""
Task 8: Prompt command audit

Methods to practice:
- splitlines(), strip(), partition(), startswith(), endswith(), lower(), count()

Use Case:
Session logs include prompts and commands mixed together.
Automation can audit whether dangerous commands were entered in configuration mode.

Assignment:
Parse command history and report dangerous config-mode commands.

Input:
- multiline terminal session log

Rules:
For each terminal session line:
1. Strip spaces from both sides of the line.
2. Skip empty lines.
3. Skip lines that do not contain exactly one '#'.

Now parse one command line like this:
SW1(config-if)# shutdown

4. Use partition('#') to split the line into:
   - prompt: text before '#'
   - command: text after '#'
5. Strip spaces from prompt and command.
6. Normalize command to lowercase.
   - Example: ' shutdown' -> 'shutdown'
7. Keep commands only from configuration prompts:
   - prompt ends with '(config)'
   - or prompt ends with '(config-if)'
8. A dangerous command is one of these:
   - command starts with 'no '
   - command equals 'shutdown'
9. Add one string to result:
   - '<prompt>: <command>'

Step output examples:
- After strip() and filtering, one command line should look like this:
  'SW1(config-if)# shutdown'
- After partition('#') and normalization, values should look like this:
  prompt = 'SW1(config-if)'
  command = 'shutdown'
- After adding a dangerous command, result should look like this:
  ['SW1(config-if): shutdown']

Expected result:
- ['SW1(config-if): shutdown', 'SW1(config): no router ospf 1']
"""

# Task: prompt command audit

data = """
SW1#show version
SW1(config-if)# shutdown
SW1(config)# no router ospf 1
SW1#show ip int brief
SW1(config)#hostname SW1
"""

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
            result.append(prompt + ': ' + command)

    return result
"""
