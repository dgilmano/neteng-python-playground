config = "switchport trunk allowed vlan 1,3,10,20,30,100"
new_config = []

for item in config:
    if item.isdigit():
        new_config.extend(item)
print(new_config)

