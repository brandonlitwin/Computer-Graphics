#!/usr/bin/python3
import argparse

parser = argparse.ArgumentParser(prog="genmesh")
parser.add_argument("-g", help="generate a sphere or cylinder", metavar="<sphere|cylinder>")
parser.add_argument("-n", help="divisionsU", type=int, default=32, nargs="?", metavar="divisionsU")
parser.add_argument("-m", help="divisionsV", type=int, default=16, nargs="?", metavar="divisionsV")
parser.add_argument("-i", help="input a file", action="store_true")
#parser.add_argument("-o", help="output to a file")
args = parser.parse_args()
if args.g:
    print("Selected geometry")
    if args.g == "sphere":
        print("Generating sphere")
    elif args.g == "cylinder":
        print("Generating cylinder")
    else:
        print("Invalid gemoetry (sphere | cylinder)")
    if args.n and args.m:
      print("Selected n and m")
      print(args.n)
      print(args.m)
    elif args.n:
        print("Selected n:")
        print(args.n)
    elif args.m:
        print("Selected m:")
        print(args.m)
    else:
        print("n and m not selected")
elif args.i:
    print("Selected input")
else:
    print("Missing arguments -g or -i")
