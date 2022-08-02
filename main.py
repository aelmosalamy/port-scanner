#!/usr/bin/env python
import plac
import socket

DEBUG = False


def scan_tcp(host: str, port: int) -> int:
    """
    Attempts a TCP connection, if successful (AKA port is open) returns 0
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # connect uses exceptions, connect_ex is similar to C connect.
        result = sock.connect_ex((host, port))

        if result != 0 and DEBUG:
            print("socket connect error:", result)

        return result


def parse_ports(ports_string) -> list[int]:
    # Two ways of setting ports: comma separated e.g. `80,443` and ranges e.g. `1-1000`
    excluded_ports = {0}

    ports = set()
    comma_split = ports_string.split(',')

    for token in comma_split:
        range_split = token.split('-')
        if len(range_split) == 1:  # A single port
            if range_split[0]:
                ports.add(int(range_split[0]))

        elif len(range_split) == 2:  # A range of ports
            a, z = range_split
            start = int(a) if a != '' else 1
            stop = int(z) if z != '' else 65535
            ports.update(list(range(start, stop + 1, 1)))

    # Remove invalid ports using set difference
    ports -= excluded_ports

    return sorted(ports)


@plac.opt("ports", "Comma separated list of ports; accepts ranges as well e.g. 20-22,80,84-112", type=str)
def main(host, ports):
    ports = parse_ports(ports)
    socket.setdefaulttimeout(1/100)  # 10ms timeout frame

    print(ports)

    for port in ports:
        print(f"TCP scanning port {port}: ", end="")
        if scan_tcp(host, port) == 0:
            print("OPEN")
        else:
            print("CLOSED")


if __name__ == "__main__":
    plac.call(main)
