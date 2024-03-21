#!/usr/bin/python
import sys
Args = len(sys.argv) -1
if  Args >= 1:
    print("{} arguement:".format(Args))
    print("{}: {}".format(sys.argv))
else:
    print("{} arguement.".format(Args))
