#!/usr/bin/python3
import sys
Args = len(sys.argv) - 1
if Args == 1:
    print("{} argument:".format(Args))
    print("{}: {}".format(Args, sys.argv[1]))
elif Args > 1:
    print("{} arguments:".format(Args))
    for i in range(1, Args + 1):
        print("{}: {}".format(i, sys.argv[i]))
else:
    print("{} argument.".format(Args))
