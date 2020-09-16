import json
import socket
from pathlib import Path


def main():
    port_to_name = {}
    
    for port in range(0, 65535):
        try:
            port_to_name[port] = socket.getservbyport(port)
        except OSError:
            pass

    with Path("port_to_name.json").open(mode="w") as fout:
        json.dump(port_to_name, fout, indent=2)


if __name__ == "__main__":
    main()