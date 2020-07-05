# yaml_load_and_print.py
import yaml


with open("yaml_files/interfaces_same_ids.yml") as fin:
    interfaces = yaml.safe_load(fin)

# Show IDs referenced by "properties" key
print("Ethernet1 properties object id:", id(interfaces["Ethernet1"]["properties"]))
print("Ethernet2 properties object id:", id(interfaces["Ethernet2"]["properties"]))
