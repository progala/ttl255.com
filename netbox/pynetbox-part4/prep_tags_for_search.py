import ipaddress
import itertools

import pynetbox

from config import NETBOX_URL, NETBOX_TOKEN

# Instantiate pynetbox.api class with URL of your NETBOX and your API TOKEN
nb = pynetbox.api(url=NETBOX_URL, token=NETBOX_TOKEN)

# Prepare tags we want to combine
mc_side = ["a_side", "b_side"]
mc_exchange = ["nasdaq", "nyse"]
mc_type = ["prod", "cert", "dr"]

# Create product of the tag families
mc_tag_prod = itertools.product(mc_side, mc_exchange, mc_type)

# Create list with lists of resulting tag combinations
# E.g. ['mc_src', 'a_side', 'nasdaq', 'prod']
mc_tags = sorted([["mc_src"] + (list(t)) for t in mc_tag_prod])

# Container from which we will be assigning prefixes
mc_src_container = ipaddress.IPv4Network("10.255.0.0/16")
mc_src_pfxs = mc_src_container.subnets(new_prefix=28)

# Create new prefixes and attach tags to them
for pfx, tag_list in zip(mc_src_pfxs, mc_tags):
    new_pfx = nb.ipam.prefixes.create(prefix=str(pfx), tags=tag_list)
    print("Prefix: {0}, tags: {1}".format(new_pfx.prefix, new_pfx.tags))
