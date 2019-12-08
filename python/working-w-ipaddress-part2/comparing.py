import ipaddress

print("Comparing Address objects")
ipa = ipaddress.ip_address("10.0.0.134")
ipb = ipaddress.ip_address("10.0.0.128")
ipc = ipaddress.ip_address("10.0.0.128")
print("{} > {}? : {}".format(ipa, ipb, ipa > ipb))
print("{} < {}? : {}".format(ipa, ipb, ipa < ipb))
print("{} == {}? : {}".format(ipb, ipc, ipb == ipc))

print()
print("Comparing network objects")
ipn1 = ipaddress.ip_network("10.10.1.32/28")
ipn2 = ipaddress.ip_network("10.10.1.32/27")
ipn3 = ipaddress.ip_network("10.10.1.48/29")
print("{} < {}? : {}".format(ipn1, ipn3, ipn1 < ipn3))
print("{} == {}? : {}".format(ipn1, ipn2, ipn1 == ipn2))
print("{} > {}? : {}".format(ipn1, ipn2, ipn1 > ipn2))

print()
print("Try comparing Address and Network objects")
try:
    print(ipa > ipn1)
except TypeError as e:
    print("Exception:", e)

print()
print("Comparing Interface objects")
ipif1 = ipaddress.ip_interface(ipa)
ipif2 = ipaddress.ip_interface(ipn1)
print("{} > {}? : {}".format(ipif1, ipif2, ipif1 > ipif2))
print("{} < {}? : {}".format(ipif1, ipif2, ipif1 < ipif2))
