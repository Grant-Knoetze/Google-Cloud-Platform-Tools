#!/usr/bin/env python3

# Put netaddr classes and functions into namespace

from netaddr import *
import pprint

ip = IPAddress('192.0.2.1')  # Takes IP address as argument
ip_version = ip.version  # Returns the IP address version (IPV4 or IPV6)
print(ip_version)
