import ipaddress

from pprint import pprint
from random import randint

print("Sorting Address objects")
print()
iparand = [ipaddress.ip_address(f"10.3.10.{randint(0,254)}") for _ in range(10)]
print("Pseudo-random addresses:")
pprint(iparand)
print()
print("Sorted addresses:")
pprint(sorted(iparand))


print()
print("Sorting Network objects")
print()
ipnrand = [ipaddress.ip_network(f"10.3.{randint(0,254)}.0/24") for _ in range(10)]
print("Pseudo-random networks:")
pprint(ipnrand)
print()
print("Sorted networks:")
pprint(sorted(ipnrand))


print()
print("Sorting Interface objects composed from above Address and Networks objects")
print()
ipifrand = [ipaddress.ip_interface(i) for i in iparand[0:5] + ipnrand[5:]]
print("Pseudo-random Interface objects:")
pprint(ipifrand)
print()
print("Sorted Interface objects:")
pprint(sorted(ipifrand))


print()
print("Sorting collection with mixed Address and Network objects")
ipmixrand = iparand[5:] + ipnrand[5:]
print("Attempting sorting:")
try:
    sorted(ipmixrand)
except TypeError as e:
    print("Execption:", str(e))

print()
print("Attempt sorting using 'get_mixed_type_key':")
pprint(sorted(ipmixrand, key=ipaddress.get_mixed_type_key))
