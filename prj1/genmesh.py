#!/usr/bin/python3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-g", help="generate a sphere or cylinder", action="store_true")
parser.add_argument("geometry", help="sphere | cylinder")
#parser.add_argument("-o", help="output to a file")
args = parser.parse_args()
if args.g:
    print("Selected geometry")
    if args.geometry == "sphere":
        print("Generating sphere")
    elif args.geometry == "cylinder":
        print("Generating cylinder")
    else:
        print("Invalid gemoetry (sphere | cylinder)")
else:
    print("G not found")
