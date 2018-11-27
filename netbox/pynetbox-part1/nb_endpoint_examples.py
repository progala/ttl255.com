from pprint import pprint

import pynetbox

from config import NETBOX_URL, NETBOX_TOKEN

# Instantiate pynetbox.api class with URL of your NETBOX and your API TOKEN
nb = pynetbox.api(url=NETBOX_URL, token=NETBOX_TOKEN)

# Retrieve all regions from Netbox
all_regions = nb.dcim.regions.all()
print("Retrieving all regions from Netbox.")
print()
print(all_regions)
print()

# Retrieve all sites in South America
print("Retrieving all sites belonging to South America region:")
sites = nb.dcim.sites.filter(region="south-america")
print()
print(sites)
print()

# Retrieve all devices from Netbox
print("Retrieving all devices from Netbox.")
devices = nb.dcim.devices.all()
print()
print(devices)
print()

# Get single device by name
print("Get device named 'sw-leaf-warsaw-01'.")
leaf_warsaw = nb.dcim.devices.get(name="sw-leaf-warsaw-01")
print()
print(leaf_warsaw)
print()

# Get device type object
# We can retrieve object by id if we know what the id is
print("Get device model used by 'sw-leaf-warsaw-01'.")
leaf_dev_type = nb.dcim.device_types.get(leaf_warsaw.device_type.id)
print(
    "Manufacturer: {manuf} - Model: {model}".format(
        manuf=leaf_dev_type.manufacturer, model=leaf_dev_type.model
    )
)
print()

# Find all devices of the same type as "sw-leaf-warsaw-01"
aristas_7060 = nb.dcim.devices.filter(device_type_id=leaf_dev_type.id)
print("Devices using {model} model:".format(model=leaf_dev_type.model))
print(aristas_7060)
