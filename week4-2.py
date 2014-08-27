import pprint

file = open('router1_show-ver.txt', 'r')

show_version = file.read()

show_lines = show_version.split("\n")

router_dict = {}

for lines in show_lines:
    if "Cisco IOS Software" in lines:
        router_dict['vendor'] = 'Cisco'
        os_version = lines.split(',')[2]
        router_dict['os_version'] = os_version.split('Version ')[1]
    if 'bytes of memory' in lines:
        router_dict['model'] = lines.split()[1]
    if 'Processor board ID' in lines:
        router_dict['serial_number'] = lines.split('Processor board ID ')[1]
    if ' uptime is' in lines:
        uptime = lines.split(' uptime is')[1]
        uptime = uptime.strip()
        router_dict['uptime'] = uptime

print
pprint.pprint(router_dict)
print