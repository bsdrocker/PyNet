#a = 'whatever'
#b = a
#a = 'newstring'
#print a + b

address = 'FE80:0000:0000:0000:0101:A3EF:EE1E:1719'
address_list = address.split(':')
print address_list
":"
address_join = ":".join(address_list)
print address_join