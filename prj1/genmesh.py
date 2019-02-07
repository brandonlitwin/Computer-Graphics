#!/usr/bin/python3
import argparse
import math

parser = argparse.ArgumentParser(prog="genmesh")
parser.add_argument("-g", help="generate a sphere or cylinder", metavar="<sphere|cylinder>")
parser.add_argument("-n", help="divisionsU", type=int, default=32, nargs="?", metavar="divisionsU")
parser.add_argument("-m", help="divisionsV", type=int, default=16, nargs="?", metavar="divisionsV")
#parser.add_argument("-i", help="input a file", action="store_true")
parser.add_argument("-o", help="output to a file", metavar="Output")
args = parser.parse_args()
if args.g and args.o:
    f = open(args.o, "w")
    print("Selected geometry")
    if args.g == "sphere":
        print("Generating sphere")
    elif args.g == "cylinder":
        print("Generating cylinder")
        numVertices = 2*args.n + 2
        numFaces = 4*args.n
        # Radian divisions = 2pi / n
        # Z coordinate = sin (angle)
        # X coordinate = cos (angle)
        # Half the y's are -1, half are 1
        # Start at (0,1,0)
        # Add 2pi / n and do sin and cos to get z and x
        radian = (2 * math.pi) / args.n
        print(numVertices)
        print(numFaces)
        # The center vertex
        f.write("v " + "0.0 " + "1.0 " + "0.0\n")
        
        f.write("v " + str(math.cos(radian)) + " 1.0 " + str(math.sin(radian)) + "\n")
        for num in range(1, args.n):
            radian = radian + ((2 * math.pi) / args.n)
            f.write("v " + str(math.cos(radian)) + " 1.0 " + str(math.sin(radian)) + "\n")
      
        # The center vertex
        f.write("v " + "0.0 " + "-1.0 " + "0.0\n")
        f.write("v " + str(math.cos(radian)) + " -1.0 " + str(math.sin(radian)) + "\n")
        for num in range(1, args.n):
            radian = radian + ((2 * math.pi) / args.n)
            f.write("v " + str(math.cos(radian)) + " -1.0 " + str(math.sin(radian)) + "\n")

        # Faces: first center is v1, second center is v34
        # 1 2 3, 1 3 4 ... 1 32 33, 1 2 33 
        # 34 35 36, 34 36 37 ... 34 65 66, 35 35 66
        for num in range(2, args.n+1):
            f.write("f " + "1 " + str(num) + " " + str(num+1) + "\n")
            if num is args.n: 
                f.write("f " + "1 " + "2 " + str(num+1) + "\n")
        # 64 more faces for triangle strip
        # 2 37 3, 3 38 4 ... 31 66 32, 33 35 2?  
        for num in range(args.n+3, ((args.n*2)+2)):
            f.write("f " + str(args.n+2) + " " + str(num) + " " + str(num+1) + "\n")
            if num is ((args.n*2)+1):
                f.write("f " + str(args.n+2) + " " + str(args.n+3) + " " + str(num+1) + "\n")
    else:
        print("Invalid geometry (sphere | cylinder)")
else:
    print("Missing arguments -g or -o")
