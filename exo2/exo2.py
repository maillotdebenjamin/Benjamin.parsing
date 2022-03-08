#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## Benjamin.parsing
## File description:
## exo.py
##
import re
file = open("exo2.txt", "r")
string = file.read()
#p = re.compile('.*')
#a = re.compile('(.*\n)')
a = re.compile('.*\n')
#test = p.findall(file.read())
test2 = a.findall(string)
#print(test)
if (test2.__len__() == 0):
    print("ok")
print(test2)
file.close()