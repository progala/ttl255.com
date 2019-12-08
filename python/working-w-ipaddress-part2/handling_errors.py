import ipaddress


print("# Exception messages, 'ip_address' factory vs 'IPv4Address' class")
print()
print('Executing: ipaddress.ip_address("192.10.1.267")')
try:
    ipaddress.ip_address("192.10.1.267")
except Exception as e:
    print(repr(e))

print()
print('Executing: ipaddress.IPv4Address("192.10.1.267")')
try:
    ipaddress.IPv4Address("192.10.1.267")
except Exception as e:
    print(repr(e))

print()
print("# Detailed exception messages dependent on the type of error")
print()
print('Executing: ipaddress.IPv4Address("192.10.257.254")')
try:
    ipaddress.IPv4Address("192.10.257.254")
except Exception as e:
    print(repr(e))
print()
print('Executing: ipaddress.IPv4Address("192.10.1.254/33")')
try:
    ipaddress.IPv4Address("192.10.1.254/33")
except Exception as e:
    print(repr(e))

print()
print("Capturing exception message and returning it:")
try:
    ipaddress.IPv4Address("192.10.1.254/32")
except ipaddress.AddressValueError as e:
    print("Error:", e)
