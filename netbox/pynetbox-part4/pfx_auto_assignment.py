import pynetbox

from config import NETBOX_URL, NETBOX_TOKEN

# Instantiate pynetbox.api class with URL of your NETBOX and your API TOKEN
nb = pynetbox.api(url=NETBOX_URL, token=NETBOX_TOKEN)

# Parent prefix we want retrieved from Netbox
pnt_pfx = "10.0.4.0/22"
nb_pnt_pfx = nb.ipam.prefixes.get(prefix=pnt_pfx)

# Show available prefixes
print("Free prefixes within {}:".format(pnt_pfx))
for p in nb_pnt_pfx.available_prefixes.list():
    print("* {prefix}".format(**p))

# Ask Netbox to assign a new prefix, of length /25, from the parent prefix
new_pfx = nb_pnt_pfx.available_prefixes.create({"prefix_length": 25})

# Show results
field_fmt = "{:>15}: {}"
print("Attributes of newly created prefix (excluding non-set attributes):")
for k, v in new_pfx.items():
    if not v:
        continue
    print(field_fmt.format(k, v))

#
# Creating multiple prefixes in a single Netbox call
#

# Prefix lengths for prefixes we want to create
pfx_lengths = [28, 29]

# Create multiple prefixes at once
new_pfxs = nb_pnt_pfx.available_prefixes.create([{'prefix_length': i} for i in pfx_lengths])

print("Attributes of newly created prefixes (excluding non-set attributes):")
for p in new_pfxs:
    print("Prefix {}:".format(p["prefix"]))
    for k, v in new_pfx.items():
        if not v:
            continue
        print(field_fmt.format(k, v))
    print()
