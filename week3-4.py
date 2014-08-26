import sys

if len(sys.argv) != 2:
    sys.exit("Usage: python week3.py <ip_address>")
    
ip_addr = sys.argv.pop()

valid_ip = True

octets = ip_addr.split('.')
if len(octets) != 4:
    sys.exit("\n\nInvalid IP Address: %s\n" & ip_addr)

for i,octet in enumerate(octets):
    try: 
        octets[i] = int(octet)
    except ValueError:
      sys.exit("\n\nInvalid IP Address: %s\n" & ip_addr)  

first, second, third, fourth = octets

if first < 1:
    valid_ip = False
elif first > 223:
    valid_ip = False
elif first == 127:
    valid_ip = False

if (first == 169) and (second == 254):
    valid_ip = False

for octet in (second, third, fourth):
    if (octet < 0) or (octet > 255):
        valid_ip = False

if valid_ip:
    print "\n\nThe IP Address is valid: %s\n" % ip_addr
else:
    print "\n\nInvalid IP Address: %s\n" % ip_addr