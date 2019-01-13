import pynetbox

from config import NETBOX_URL, NETBOX_TOKEN

# Instantiate pynetbox.api class with URL of your NETBOX and your API TOKEN
nb = pynetbox.api(url=NETBOX_URL, token=NETBOX_TOKEN)

# Retrieve device object to which updates will be made
rtr = nb.dcim.devices.get(name="rtr-inet-seoul-01")

# This router shouldn't have any of the below attributes set
print("Device name: ", rtr.name)
print("Current tenant: ", rtr.tenant)
print("Current serial number: ", rtr.serial)
print("Current asset tag: ", rtr.asset_tag)
print()

# Retrieve tenant we want to assign to the router
rtr_tenant = nb.tenancy.tenants.get(name="RogNet Corp", group="internal")

# Assign values to attributes
rtr.tenant = rtr_tenant
rtr.serial = "436F6F6C21"
rtr.asset_tag = "0027182"

# Ask Pynetbox to Update object in Netbox
rtr.save()

# Retrieve same router again just to prove it was updated
rtr_modified = nb.dcim.devices.get(name="rtr-inet-seoul-01")

print("Device name: ", rtr_modified.name)
print("New tenant: ", rtr_modified.tenant)
print("New serial number: ", rtr_modified.serial)
print("New asset tag: ", rtr_modified.asset_tag)
print()


# Retrieve router object for update with dictionary
rtr2 = nb.dcim.devices.get(name="sw-mgmt-kampala-01")

# This router shouldn't have any of the below attributes set
print("Device name: ", rtr2.name)
print("Current tenant: ", rtr2.tenant)
print("Current serial number: ", rtr2.serial)
print("Current asset tag: ", rtr2.asset_tag)
print()

# Retrieve tenant for rtr2
rtr2_tenant = nb.tenancy.tenants.get(name="Uganda Press", group="customers")

# Prepare dictionary with attributes set to desired values
rtr2_update_dict = dict(
    tenant=rtr2_tenant,
    serial="4E69636521",
    asset_tag="0057721",
)

# Ask Pynetbox to update object with attributes/values in rtr2_update_dict
rtr2.update(rtr2_update_dict)

# Retrieve same router again just to prove it was updated
rtr2_modified = nb.dcim.devices.get(name="sw-mgmt-kampala-01")

print("Device name: ", rtr2_modified.name)
print("New tenant: ", rtr2_modified.tenant)
print("New serial number: ", rtr2_modified.serial)
print("New asset tag: ", rtr2_modified.asset_tag)