from pprint import pprint

import pynetbox

from config import NETBOX_URL, NETBOX_TOKEN

# Instantiate pynetbox.api class with URL of your NETBOX and your API TOKEN
nb = pynetbox.api(url=NETBOX_URL, token=NETBOX_TOKEN)

# Create new device object
# Will fail as incorrect values are passed
try:
    result = nb.dcim.devices.create(
        name="rtr-inet-seoul-01",
        device_type="asr-1002-x",
        device_role="internet-edge",
        site="seoul-dc-01",
    )
except pynetbox.lib.query.RequestError as e:
    print(e.error)


# Retrieve info needed for creating our device
ndev_dtype = nb.dcim.device_types.get(slug="asr-1002-x")
ndev_drole = nb.dcim.device_roles.get(slug="internet-edge")
ndev_site = nb.dcim.sites.get(slug="seoul-dc-01")

# Display ids of retrieved objects
req_fields = (
    "Site: {site}, ID: {site_id}\n"
    "Device Type: {dtype}, ID: {dtype_id}\n"
    "Device Role: {drole}, ID: {drole_id}".format(
        site=ndev_site,
        site_id=ndev_site.id,
        dtype=ndev_dtype,
        dtype_id=ndev_dtype.id,
        drole=ndev_drole,
        drole_id=ndev_drole.id,
    )
)

print(req_fields)


# Device creation attempt no 2
# This will succeed as correct values are passed
try:
    result = nb.dcim.devices.create(
        name="rtr-inet-seoul-01",
        device_type=ndev_dtype.id,
        device_role=ndev_drole.id,
        site=ndev_site.id,
    )
except pynetbox.lib.query.RequestError as e:
    print(e.error)
else:
    pprint(result)

# Trying to create duplicated device object
# This will fail and an error message will be shown
try:
    result = nb.dcim.devices.create(
        name="rtr-inet-seoul-01",
        device_type=ndev_dtype.id,
        device_role=ndev_drole.id,
        site=ndev_site.id,
    )
except pynetbox.lib.query.RequestError as e:
    print(e.error)
else:
    pprint(result)