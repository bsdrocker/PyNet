import sys

if len(sys.argv) != 2:
    sys.exit("Usage: python week3.py <ip_address>")
    
ip_addr = sys.argv.pop()

invalid_ip = False

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
    invalid_ip = True
elif first > 223:
    invalid_ip = True
elif first == 127:
    invalid_ip = True

if (first == 169) and (second == 254):
    invalid_ip = True

for octet in (second, third, fourth):
    if (octet < 0) or (octet > 255):
        invalid_ip = True

while invalid_ip:
    print "\n\nYou have entered an invalid IP address"
    ip_addr = raw_input("Please re-enter IP: ")
    invalid_ip = False
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
        invalid_ip = True
    elif first > 223:
        invalid_ip = True
    elif first == 127:
        invalid_ip = True

    if (first == 169) and (second == 254):
        invalid_ip = True

    for octet in (second, third, fourth):
        if (octet < 0) or (octet > 255):
            invalid_ip = True

if invalid_ip:
    print "\n\nInvalid IP Address: %s\n" % ip_addr
else:
    print "\n\nThe IP Address is valid: %s\n" % ip_addr