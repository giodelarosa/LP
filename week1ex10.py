from ciscoconfparse import CiscoConfParse

cisco_config = CiscoConfParse("cisco_ipsec.txt")

crypto = cisco_config.find_objects_w_child(parentspec=r"^crypto map CRYPTO", childspec=r"AES")



print "\nCrypto Maps using AES:"
for entry in crypto:
    print "  {0}".format(entry.text)
print