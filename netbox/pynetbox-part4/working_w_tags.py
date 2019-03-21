from pprint import pprint

import pynetbox

from config import NETBOX_URL, NETBOX_TOKEN

# Instantiate pynetbox.api class with URL of your NETBOX and your API TOKEN
nb = pynetbox.api(url=NETBOX_URL, token=NETBOX_TOKEN)

# Create prefix and assign tags to it
pfx_atts = {"prefix": "10.255.1.0/28", "tags": ["mc_src", "prod", "a_side", "nyse"]}
new_pfx = nb.ipam.prefixes.create(pfx_atts)

# Show attributes of newly created prefix
pprint(dict(new_pfx))


# Apply tag to an existing device, possibly overwriting an existing tag
dev_to_tag = nb.dcim.devices.get(name="rtr-inet-seoul-01")
dev_to_tag.tags = ["decom_candidate"]
update_success = dev_to_tag.save()

print("Object updated:", update_success)


# Apply tags to an existing object without overwriting existing tags

# Retrieve device we want to tag
dev_to_tag = nb.dcim.devices.get(name="rtr-inet-seoul-01")
print("Tags currently attached to {0}: {1}".format(dev_to_tag.name, dev_to_tag.tags))
print()

# Attach new tags
dev_to_tag.tags = dev_to_tag.tags + ["decom_scheduled", "with_dco"]

# Alternatively use list's 'extend' method
# dev_to_tag.tags.extend(["decom_scheduled", "with_dco"])

dev_to_tag.save()

updated_dev = nb.dcim.devices.get(name="rtr-inet-seoul-01")
print("Tags attached to {0} after update: {1}".format(dev_to_tag.name, dev_to_tag.tags))
