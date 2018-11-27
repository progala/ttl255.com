from pprint import pprint

import pynetbox

from config import NETBOX_URL, NETBOX_TOKEN

# Instantiate pynetbox.api class with URL of your NETBOX and your API TOKEN
nb = pynetbox.api(url=NETBOX_URL, token=NETBOX_TOKEN)

# Get all of the prefixes in Netbox
print("Retrieving all prefixes from Netbox.")
print()
all_prefixes = nb.ipam.prefixes.all()
print(all_prefixes)
print()

# Check type of the individual prefix
print("Type of the individual prefix:", type(all_prefixes[5]))
print()

# Print site, tenant, role and description belonging to our prefix
my_pfx = all_prefixes[5]

fmt = "{:<20}{:<20}{:<20}{:<15}{:<20}"
header = ("Prefix", "Site", "Tenant", "Role", "Description")

print(fmt.format(*header))
print(
    fmt.format(
        str(my_pfx.prefix),
        my_pfx.site.name,
        my_pfx.tenant.name,
        my_pfx.role.name,
        my_pfx.description,
    )
)
print()

# Print type of my_pfx.prefx
print("Type of my_pfx.prefix: ", type(my_pfx.prefix))
print()

# Playing around with netaddr.ip.IPNetwork object
pfx = my_pfx.prefix
print("Prefix: ", pfx.cidr)
print("Hostmask of our network: ", pfx.hostmask)
print("10th IP on the network: ", pfx.ip + 10)
print()


# Case where get can't uniquely identify object
print("Attempting to retrieve 10.99.50.0/24 using get()")
try:
    single_prefix = nb.ipam.prefixes.get(q="10.99.50.0/24")

    # Never gets executed
    print(single_prefix)
except ValueError as e:
    print("Error:", e)
print()


# Use query from get() in filter()
print("Attempting to retrieve 10.99.50.0/24 using filter()")
single_prefix = nb.ipam.prefixes.filter(q="10.99.50.0/24")
print(single_prefix)
print()

# Add mask_length attribute and try get() again
print("Attempting to retrieve 10.99.50.0/24 using get() with mask length")
single_prefix = nb.ipam.prefixes.get(q="10.99.50.0", mask_length="24")
print("Single prefix retrieved: ", single_prefix)
print()

# Retrieve all info on the object by accessing _index_cache
print("List of tuples in _index_cache for prefix object:")
pprint(single_prefix._index_cache)
print()

# Retrieve all info on the object by accessing _full_cache
print("Referenced objects fully expanded when accessing _full_cache:")
pprint(single_prefix._full_cache)
