import pprint

show_ip_int_brief = '''
Interface            IP-Address      OK?     Method      Status     Protocol
FastEthernet0   unassigned      YES     unset          up          up
FastEthernet1   unassigned      YES     unset          up          up
FastEthernet2   unassigned      YES     unset          down      down
FastEthernet3   unassigned      YES     unset          up          up
FastEthernet4    6.9.4.10         YES     NVRAM       up          up
NVI0                  6.9.4.10        YES     unset           up          up
Tunnel1            16.25.253.2     YES     NVRAM       up          down
Tunnel2            16.25.253.6     YES     NVRAM       up          down
Vlan1                unassigned      YES    NVRAM       down      down
Vlan10              10.220.88.1     YES     NVRAM       up          up
Vlan20              192.168.0.1     YES     NVRAM       down      down
Vlan100            10.220.84.1     YES     NVRAM       up          up
'''

show_ip_lines = show_ip_int_brief.split("\n")

show_ip_list = []

for line in show_ip_lines:
    if 'Interface' in line:
        continue
    line_split = line.split()
    if len(line_split) == 6:
        if_name, ip_addr, discard1, discard2, line_status, line_proto = line_split
        if (line_status == 'up') and (line_proto == 'up'):
            show_ip_list.append( (if_name, ip_addr, line_status, line_proto) )
print "\n"

pprint.pprint(show_ip_list)
print "\n"