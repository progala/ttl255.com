import ipaddress

print("Creating Interface object (default mask):")
ipifa = ipaddress.ip_interface("10.0.0.133")
print(repr(ipifa))

print()
print("Creating Interface object (explicit mask):")
ipifb = ipaddress.ip_interface("10.2.0.164/24")
print(repr(ipifb))

print()
print("Generate source network from Interface:")
src = "{}".format(ipifb.network.with_hostmask.replace("/", " "))
print(src)

print()
print("Get Address object from Interface object:")
print(repr(ipifb.ip))

print()
print("Getting different string representations:")
print(ipifb.with_hostmask)
print(ipifb.with_prefixlen)
print(ipifb.with_netmask)
