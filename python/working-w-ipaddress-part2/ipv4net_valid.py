import ipaddress
from typing import Tuple


def validate_ipv4_net(network: str) -> Tuple[bool, str]:
    """
    Checks if string is a valid IPv4 network

    :param network: string representation of IPv4 network
    :return: tuple of (bool, str). (True, msg) if valid; (False, msg) if invalid
    """
    try:
        ipaddress.IPv4Network(network)
    except (ipaddress.AddressValueError, ipaddress.NetmaskValueError, ValueError) as e:
        valid = False
        msg = "Provided string is not a valid network: {}.".format(e)
    else:
        valid = True
        msg = "String is a network."

    return valid, msg


nets = ["192.0.2.0/255.254.254.255", "256.0.0.0/24", "10.0.0.1/30", "172.23.1.0/33"]

for n in nets:
    print(validate_ipv4_net(n))
