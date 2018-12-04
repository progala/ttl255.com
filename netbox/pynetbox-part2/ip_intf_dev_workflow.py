import pynetbox

from config import NETBOX_URL, NETBOX_TOKEN

# Instantiate pynetbox.api class with URL of your NETBOX and your API TOKEN
nb = pynetbox.api(url=NETBOX_URL, token=NETBOX_TOKEN)

# Retrieve objects needed for creation of the device
dev_type = nb.dcim.device_types.get(slug="3750g-48ts")
dev_role = nb.dcim.device_roles.get(slug="management-switch")
dev_site = nb.dcim.sites.get(slug="kampala-dc-01")

# Prepare dict with attributes for our device
dev_dict = dict(
    name="sw-mgmt-kampala-01",
    device_type=dev_type.id,
    device_role=dev_role.id,
    site=dev_site.id,
)

# Add device to NetBox and store resulting object in "new_dev"
new_dev = nb.dcim.devices.create(dev_dict)

# Prepare dict with attributes for Management interface
intf_dict = dict(
    name="Vl841",
    form_factor=0,
    description="Management SVI",
    device=new_dev["id"]
)

# Add interface to NetBox and store resulting object in "new_intf"
new_intf = nb.dcim.interfaces.create(intf_dict)

# Prepare dict with attributes for Management IP address
ip_add_dict = dict(
    address="10.1.6.18/32",
    status=1,
    description="Management IP for {}".format(dev_dict["name"]),
    interface=new_intf["id"],
)

# Add interface to NetBox and store resulting object in "new_ip"
new_ip = nb.ipam.ip_addresses.create(ip_add_dict)

# Display summary, just to see if objects were really created
print(
    "Device '{dev}' created with interface '{intf}', which has IP {ipadd}.".format(
        dev=new_dev["name"], intf=new_intf["name"], ipadd=new_ip["address"]
    )
)
