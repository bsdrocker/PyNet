import sys

if len(sys.argv) != 2:
    sys.exit("Usage: python week3.py <ip_address>")

ip_addr = sys.argv.pop()

octets = ip_addr.split('.')

ip_addr_bin = []

if len(octets) == 4:
    for octet in octets:
        bin_octet = bin(int(octet))
        bin_octet = bin_octet[2:]
        
        while True:
            if len(bin_octet) >= 8:
                    break
            bin_octet = '0' + bin_octet
        ip_addr_bin.append(bin_octet)
    ip_addr_bin = ".".join(ip_addr_bin)
    
    print "\n%-15s %-15s" % ("IP address", "Binary")
    print "%-15s %-15s" % (ip_addr, ip_addr_bin)

else:
        sys.exit("Invalid IP address entered")