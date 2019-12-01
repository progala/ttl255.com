import ipaddress
from pprint import pprint

net_pfx_len = "192.0.2.0/24"
net_mask = "192.0.2.0/255.255.255.0"
net_wcard = "192.0.2.0/0.0.0.255"

net_o_pfx_len = ipaddress.ip_network(net_pfx_len)
net_o_mask = ipaddress.ip_network(net_mask)
net_o_wcard = ipaddress.ip_network(net_wcard)

print("Different network formats end in the same object:")
print(repr(net_o_pfx_len))
print(repr(net_o_mask))
print(repr(net_o_wcard))

print(net_o_pfx_len == net_o_mask == net_o_wcard)

print()
print("Getting string representations back:")

ipn = ipaddress.ip_network("10.0.0.0/16")
print(ipn.with_prefixlen)
print(ipn.with_hostmask)
print(ipn.with_netmask)


print()
print("Getting address, prefix length, hostmasks and netmask separately:")

print(repr(ipn.network_address))
print(ipn.prefixlen)
print(repr(ipn.hostmask))
print(repr(ipn.netmask))

print()
print("Generate some Cisco ACLs:")

ace_fmt = "permit ip {} {} {} {}"
src_net = ipaddress.ip_network("10.2.0.0/24")
dst_nets = [ipaddress.ip_network("10.1.{}.0/24".format(n)) for n in range(0, 11, 2)]
aces = "\n".join(
    [
        ace_fmt.format(
            src_net.network_address, src_net.hostmask, d.network_address, d.hostmask
        )
        for d in dst_nets
    ]
)
print(aces)

print()
print("Get hosts contained in the network:")

ipn192 = ipaddress.ip_network("192.168.0.0/16")
print(ipn192.hosts())

print()
print("First 3 usable hosts:")

ipn192h = ipn192.hosts()
print(repr(next(ipn192h)))
print(repr(next(ipn192h)))
print(repr(next(ipn192h)))

print()
print("Get some hosts from the middle:")

from itertools import islice

for hip in islice(ipn192.hosts(), 19, 25):
    print(hip)


print()
print("Access hosts by index:")

print(repr(ipn192[3]))
print(repr(ipn192[60]))


print()
print("Slice of all hosts IP, not just usable ones:")

for hip in islice(ipn192, 0, 5):
    print(hip)

print()
print("Broadcast address", repr(ipn192.broadcast_address))

print()
print("Check for overlap.")
print("N1: 10.10.1.32/28")
print("N2: 10.10.1.32/27")
print("N3: 10.10.1.48/29")
ipn1 = ipaddress.ip_network("10.10.1.32/28")
ipn2 = ipaddress.ip_network("10.10.1.32/27")
ipn3 = ipaddress.ip_network("10.10.1.48/29")
print("N1 overlaps N2?", ipn1.overlaps(ipn2))
print("N1 overlaps N3?", ipn1.overlaps(ipn3))
print("N2 overlaps N3?", ipn2.overlaps(ipn3))
print("N3 overlaps N2?", ipn3.overlaps(ipn2))


print()
print("Test supernet relationship:")
print("N2 supernet of N3?", ipn2.supernet_of(ipn3))
print("N3 supernet of N2?", ipn3.supernet_of(ipn2))
print("N3 subnet of N2?", ipn3.subnet_of(ipn2))


print()
print("Getting supernet of the network")
nchild = ipaddress.ip_network("172.20.15.160/29")
print("Child net:", nchild)
print("Supernet with pfxlen diff of 3", repr(nchild.supernet(prefixlen_diff=3)))
print("Supernet with pfxlen set to 23", repr(nchild.supernet(new_prefix=23)))

print()
print("Getting subnets of network.")
nparent = ipaddress.ip_network("10.25.2.0/23")
print("Network:", nparent)
print("Subnets (default):", list(nparent.subnets()))

print()
print("Subnets with pfxlen diff of 2:")
pprint(list(nparent.subnets(prefixlen_diff=2)))

print()
print("Subnets with pfxlen set to 27:")
pprint(list(nparent.subnets(new_prefix=27)))

print()
print("Get networks left after exclusion of given subnet:")
ipn10 = ipaddress.ip_network("10.2.0.0/23")
print("N10:", ipn10)
print("Exclude 10.2.1.0/25:")
print([n for n in ipn10.address_exclude(ipaddress.ip_network("10.2.1.0/25"))])

print()
print("Check if IP address belongs to network:")
print("10.2.1.2 in N10?", ipaddress.ip_address("10.2.1.2") in ipn10)
print("10.5.1.2 in N10?", ipaddress.ip_address("10.5.1.2") in ipn10)
