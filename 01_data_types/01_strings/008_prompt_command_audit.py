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
1. Process one line at a time.
2. A command line contains '#'.
3. Use partition('#') to split prompt and command.
4. Strip both parts.
5. Keep commands only when the prompt ends with '(config)' or '(config-if)'.
6. A dangerous command is one that starts with 'no ' or equals 'shutdown'.
7. Normalize commands to lowercase.
8. Return a list of '<prompt>: <command>' strings.

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
