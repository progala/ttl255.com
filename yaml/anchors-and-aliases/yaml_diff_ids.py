# yaml_diff_ids.py
import yaml


interfaces = dict(
    Ethernet1=dict(description="Uplink to core-1", speed=1000, mtu=9000),
    Ethernet2=dict(description="Uplink to core-2", speed=1000, mtu=9000),
)

interfaces["Ethernet1"]["properties"] = ["pim", "ptp", "lldp"]
interfaces["Ethernet2"]["properties"] = ["pim", "ptp", "lldp"]

# Show IDs referenced by "properties" key
print("Ethernet1 properties object id:", id(interfaces["Ethernet1"]["properties"]))
print("Ethernet2 properties object id:", id(interfaces["Ethernet2"]["properties"]))

# Dump YAML to stdout
print("\n##### Resulting YAML:\n")
print(yaml.safe_dump(interfaces))

# Dump YAML to file
with open("yaml_files/interfaces_diff_ids.yml", "w") as fout:
    yaml.safe_dump(interfaces, fout)
