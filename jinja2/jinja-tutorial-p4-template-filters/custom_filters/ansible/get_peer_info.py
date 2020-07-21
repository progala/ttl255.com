# get_peer_info.py
import ipaddress


def get_peer_info(our_port_info, hostvars):
    peer_info = {"name": our_port_info["peer"]}
    our_net = ipaddress.IPv4Interface(our_port_info["ip"]).network
    peer_vars = hostvars[peer_info["name"]]

    for _, peer_port_info in peer_vars["ports"].items():
        if not peer_port_info["ip"]:
            continue
        peer_net_obj = ipaddress.IPv4Interface(peer_port_info["ip"])
        if our_net == peer_net_obj.network:
            peer_info["ip"] = peer_net_obj.ip
            break
    return peer_info


class FilterModule(object):

    def filters(self):
        return {
            'get_peer_info': get_peer_info
        } 