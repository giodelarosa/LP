from ciscoconfparse import CiscoConfParse

cisco_config = CiscoConfParse("cisco_ipsec.txt")

crypto = cisco_config.find_objects_w_child(parentspec=r"^crypto map CRYPTO", childspec=r"pfs group2")



print "\nCrypto Maps using PFS group2:"
for entry in crypto:
    print "  {0}".format(entry.text)
print


