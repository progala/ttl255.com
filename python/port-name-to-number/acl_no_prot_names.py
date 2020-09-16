from pathlib import Path
from socket import getservbyname


def main():
    with Path("arista-sh-acl.txt").open() as fin:
        aces = [line for line in fin.read().split("\n") if line]

    aces_clean = []
    for ace in aces:
        units = ace.strip().split(" ")
        prot = units[2]
        port = units[-1]
        if not port.isdigit():
            try:
                port_no = getservbyname(port)
                aces_clean.append(" ".join(units[:-1] + [str(port_no)]))
            except OSError:
                print(f"Couldn't translate port name '{port}' for protocol {prot}")

    print("\n".join(aces_clean))


if __name__ == "__main__":
    main()