import ipaddress

print("Creating IP address:")
ipa = ipaddress.ip_address("10.0.0.133")
print(repr(ipa))

print()
print("10.0.0.133, Global or private?")

print("Private?", ipa.is_private)
print("Global?", ipa.is_global)

print()
print("Are we special?")

print("127.0.0.1, Loopback?", ipaddress.ip_address("127.0.0.1").is_loopback)
print("229.100.0.23, Multicast?", ipaddress.ip_address("229.100.0.23").is_multicast)
print("169.254.0.100, Link local?", ipaddress.ip_address("169.254.0.100").is_link_local)
print("240.10.0.1, Reserved?", ipaddress.ip_address("240.10.0.1").is_reserved)


print()
print("10.0.0.133 PTR:")
print(ipa.reverse_pointer)

print()
print("IP address arithmetic")

print("10.0.0.133 + 1", repr(ipa + 1))
print("10.0.0.133 -5", repr(ipa - 5))

ipb = ipaddress.ip_address("10.0.0.136")
print(int(ipb))


print()
print("Feed int to ip_address")
ipc = ipaddress.ip_address(3794067923)
print("3794067923", repr(ipc))

ipd = ipaddress.ip_address(105253214244521019198275021855725010304)
print("105253214244521019198275021855725010304", repr(ipd))
