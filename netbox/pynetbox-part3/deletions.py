from pprint import pprint

import pynetbox

from config import NETBOX_URL, NETBOX_TOKEN

# Instantiate pynetbox.api class with URL of your NETBOX and your API TOKEN
nb = pynetbox.api(url=NETBOX_URL, token=NETBOX_TOKEN)

# Check if object already exists and delete if so
# This allows us to run example multiple times
rtr = nb.dcim.devices.get(name="bad-isp-delete")
if rtr:
    rtr.delete()


# Retrieve info needed for creating our device
ndev_dtype = nb.dcim.device_types.get(slug="asr-1002-x")
ndev_drole = nb.dcim.device_roles.get(slug="internet-edge")
ndev_site = nb.dcim.sites.get(slug="seoul-dc-01")

# Create device
try:
    result = nb.dcim.devices.create(
        name="bad-isp-delete",
        device_type=ndev_dtype.id,
        device_role=ndev_drole.id,
        site=ndev_site.id,
    )
except pynetbox.RequestError as e:
    print(e.error)

# Retrieve object so that we can call delete() on it
rtr = nb.dcim.devices.get(name="bad-isp-delete")

# Confirm we'ge to the right device
print("Netbox result before deletion:", rtr.name)
print()

# Delete object
rtr.delete()

# Netbox no longer knows anything about our device
rtr_ = nb.dcim.devices.get(name="bad-isp-delete")
print("Netbox result after deletion:", rtr_)
print()

# But object is still in the memory
print("Object is still in the memory:")
print()
pprint(dict(rtr))