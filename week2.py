ip_addr = raw_input("Please enter a subnet: ")
octets = ip_addr.split('.')
if len(octets) == 3:
    octets.append('0')
elif len(octets) == 4:
    octets[3] = '0'
"."
ip_addr_fin = ".".join(octets)
first_octet = int(octets[0])
first_octet_bin = bin(first_octet)
first_octet_hex = hex(first_octet)

print "NETWORK_NUMBER \t FIRST_OCTET_BINARY \t FIRST_OCTET_HEX"
print "%s \t %s \t \t %s" % (ip_addr_fin, first_octet_bin, first_octet_hex)
print "\n"

ip_addr_convert = raw_input("Please enter an IP: ")
octets_convert = ip_addr_convert.split('.')
first_octet_convert = int(octets_convert[0])
second_octet_convert = int(octets_convert[1])
third_octet_convert = int(octets_convert[2])
fourth_octet_convert = int(octets_convert[3])
first_octet_convert_bin = bin(first_octet_convert)
second_octet_convert_bin = bin(second_octet_convert)
third_octet_convert_bin = bin(third_octet_convert)
fourth_octet_convert_bin = bin(fourth_octet_convert)

print "first_octet \t second_octet \t third_octet \t fourth_octet"
print "%s \t %s \t %s \t %s" % (first_octet_convert_bin, second_octet_convert_bin, third_octet_convert_bin, fourth_octet_convert_bin)
print "\n"

entry1 = "*  1.0.192.0/18   157.130.10.233        0 701 38040 9737 i"
entry2 = "*  1.1.1.0/24      157.130.10.233         0 701 1299 15169 i"
entry3 = "*  1.1.42.0/24     157.130.10.233        0 701 9505 17408 2.1465 i"
entry4 = "*  1.0.192.0/19   157.130.10.233        0 701 6762 6762 6762 6762 38040 9737 i"
entry1_list = entry1.split()
entry2_list = entry2.split()
entry3_list = entry3.split()
entry4_list = entry4.split()
ip_prefix1 = entry1_list[1]
ip_prefix2 = entry2_list[1]
ip_prefix3 = entry3_list[1]
ip_prefix4 = entry4_list[1]
as_path1 = entry1_list[4:]
as_path2 = entry2_list[4:]
as_path3 = entry3_list[4:]
as_path4 = entry4_list[4:]
as_path1.pop()
as_path2.pop()
as_path3.pop()
as_path4.pop()

print "ip_prefix \t as_path"
print "%s \t %s" % (ip_prefix1, as_path1)
print "%s \t %s" % (ip_prefix2, as_path2)
print "%s \t %s" % (ip_prefix3, as_path3)
print "%s \t %s" % (ip_prefix4, as_path4)
print "\n"

cisco_ios = "Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)"
cisco_ios_list = cisco_ios.split(',')
ios_version = cisco_ios_list[2]

print "ios_version = %s" % (ios_version)
