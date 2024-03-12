#!/usr/bin/python3
for i in range (ord('a'), ord('z') +1):
    if i == 'e':
        continue
    if i == 'q':
        continue
    print("{:c}".format(i), end= '')
