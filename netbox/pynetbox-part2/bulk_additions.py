import json

import pynetbox

from config import NETBOX_URL, NETBOX_TOKEN

# Specify number of Spine and Leaf switches
SPINE_NUM = 2
LEAF_NUM = 8

# Instantiate pynetbox.api class with URL of your NETBOX and your API TOKEN
nb = pynetbox.api(url=NETBOX_URL, token=NETBOX_TOKEN)

# List to store dictionaries with attributes for new devices
melb_devices = list()

# Retrieve objects needed for creation of Melbourne devices
site_melbourne = nb.dcim.sites.get(slug="melbourne-dc-01")
drole_leaf = nb.dcim.device_roles.get(slug="leaf-switch")
drole_spine = nb.dcim.device_roles.get(slug="spine-switch")
dtype_ar7060 = nb.dcim.device_types.get(slug="7060cx2-32s")
dtype_ar7280 = nb.dcim.device_types.get(slug="7280cr2-60")

# Generate attributes for spines
for i in range(1, SPINE_NUM + 1):
    melb_devices.append(
        dict(
            name="sw-spine-melbourne-0{swid}".format(swid=i),
            device_type=dtype_ar7280.id,
            device_role=drole_spine.id,
            site=site_melbourne.id,
        )
    )

# Generate attributes for leaves
for i in range(1, LEAF_NUM + 1):
    melb_devices.append(
        dict(
            name="sw-leaf-melbourne-0{swid}".format(swid=i),
            device_type=dtype_ar7060.id,
            device_role=drole_leaf.id,
            site=site_melbourne.id,
        )
    )

try:
    # Try creating all of the devices at once
    results = nb.dcim.devices.create(melb_devices)

    # Set formatting and header
    fmt = "{:<25}{:<15}{:<15}{:<15}"
    header = ("Device", "Dev Role", "Dev Type", "Site")

    # Print header
    print(fmt.format(*header))

    # Print summary info for each of the devices
    for r in results:
        print(
            fmt.format(
                r["name"],
                r["device_role"]["name"],
                r["device_type"]["model"],
                r["site"]["name"],
            )
        )

    # As a bonus, dump to json file objects returned by NetBox
    with open("melbourne_devices.json", encoding="utf-8", mode="w") as fout:
        json.dump(results, fout)

except pynetbox.lib.query.RequestError as e:
    print(e.error)

