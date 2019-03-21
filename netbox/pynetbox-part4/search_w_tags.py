import pynetbox

from config import NETBOX_URL, NETBOX_TOKEN

# Instantiate pynetbox.api class with URL of your NETBOX and your API TOKEN
nb = pynetbox.api(url=NETBOX_URL, token=NETBOX_TOKEN)

# Filter prefixes using single tag
nyse_pfxs = nb.ipam.prefixes.filter(tag=["nyse"])
print(nyse_pfxs)

# Filter prefixes that have both tags "nasdaq" and "a_side"
tg_nasdaq_aside = ["nasdaq", "a_side"]
tagged_pfxs = nb.ipam.prefixes.filter(tag=tg_nasdaq_aside)
print(tagged_pfxs)

# Get prefixes that are tagged with nyse, prod and b_side labels
tg_nyse_bside_prod = ["nyse", "b_side", "prod"]
tagged_pfxs = nb.ipam.prefixes.filter(tag=tg_nyse_bside_prod)

print("Found {} prefix(es).".format(len(tagged_pfxs)))
print()
print("Prefix: {0}, tags: {1}".format(tagged_pfxs[0].prefix, tagged_pfxs[0].tags))
