#/usr/bin/python

from ciscoconfparse import CiscoConfParse

cisco_config = CiscoConfParse("cisco_ipsec.txt")

crypto = cisco_config.find_objects(r"^crypto map CRYPTO")

for child in crypto:
    print child.text
    for newchildren in child.children:
        print newchildren.text



print crypto