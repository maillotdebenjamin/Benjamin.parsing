#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## Benjamin.parsing
## File description:
## exo.py
##
import re
p = re.compile('[A-Z ]')
print(p)
c = re.compile('ab*', re.IGNORECASE)
#print(p.match("ab*"))
print(p.findall("=#kskt8&d*L8kajbc1zjcEg+4rj82m^fSiqp@ql!%si *!rnv#nelb%$%3vk_R*!rnv#nelb%$%3vk_E^vz@zz5t3p*n_il0vGp9nn+29#8s%y4o*ulE!8x4X C'E!lfmtyt@zk9ad5iaxrs@ST G5is*_-@4y_9vwpt=tocxENI!lfmtyt@zk9ad5iaxrs@AL"))
test = p.findall("=#kskt8&d*L8kajbc1zjcEg+4rj82m^fSiqp@ql!%si *!rnv#nelb%$%3vk_R*!rnv#nelb%$%3vk_E^vz@zz5t3p*n_il0vGp9nn+29#8s%y4o*ulE!8x4X C'E!lfmtyt@zk9ad5iaxrs@ST G5is*_-@4y_9vwpt=tocxENI!lfmtyt@zk9ad5iaxrs@AL")
for i in test:
    print(i, end= '')