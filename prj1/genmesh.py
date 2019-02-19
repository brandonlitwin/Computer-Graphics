#!/usr/bin/python3
# Brandon Litwin, Project 1, Computer Graphics
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
    if args.g == "sphere":
        # r = 1
        # longitude = -pi to pi
        # latitude = -pi/2 to pi/2
        # x = r * sin(m) * cos(n)
        # y = r * cos(m)
        # z = r * sin(m) * sin(n)
        #longitude_radian = (2 * math.pi) / args.n
        #latitude_radian = (2 * math.pi) / args.m
        f.write("v " + "0.0 " + "1.0 " + "0.0\n")
        for a in range(0, args.m):
            latitude_radian = (math.pi * (a+1)) / args.m
            for b in range(0, args.n):
                longitude_radian = (2.0 * math.pi * b) / args.n
                f.write("v " + str(math.sin(latitude_radian)*math.cos(longitude_radian)) + " " + str(math.cos(latitude_radian)) + " " + str(math.sin(latitude_radian)*math.sin(longitude_radian)) +"\n")

        f.write("v " + "0.0 " + "-1.0 " + "0.0\n")
        # Top triangle fan
        for num in range(2, args.n+1):
            f.write("f " + "1 " + str(num) + " " + str(num+1) + "\n")
            if num is args.n: 
                f.write("f " + "1 " + str(num+1) + " " + "2" + "\n")
        # Compute number of triangles
        total_triangles = (2*args.n) + ((2*args.n)*(args.m-1))
        #(((total - 2*args.n)/2)+2)
        # Generate the triangle strips
        # Range is total - 2n because we do not need to calculate the top and bottom fans again
        for num in range(2, (((total_triangles - 2*args.n)/2)+2)):
            if ((num-(args.n+1)) % args.n) == 0:
                f.write("f " + str(num) + " " + str(args.n+num) + " " + str((num+1)-args.n) + "\n")
                f.write("f " + str((num+1)-args.n) + " " + str(args.n+num) + " " + str(num+1) + "\n")
            else:
                f.write("f " + str(num) + " " + str(args.n+num) + " " + str(num+1) + "\n")
                f.write("f " + str(num+1) + " " + str(args.n+num) + " " + str(args.n+num+1) + "\n")


        total_vertices = ((args.n*args.m)+2)
        # Bottom triangle fan
        #for num in range(total_vertices-args.n, total_vertices):
        for num in range(total_vertices-args.n, total_vertices):
            if num < total_vertices-1:
                f.write("f " + str(total_vertices) + " " + str(num) + " " + str(num+1) + "\n")
            else:
                f.write("f " + str(total_vertices) + " " + str(total_vertices-1) + " " + str(total_vertices-args.n) + "\n")

    elif args.g == "cylinder":
        numVertices = 2*args.n + 2
        numFaces = 4*args.n
        # Radian divisions = 2pi / n
        # Z coordinate = sin (angle)
        # X coordinate = cos (angle)
        # Half the y's are -1, half are 1
        # Start at (0,1,0)
        # Add 2pi / n and do sin and cos to get z and x
        radian = (2 * math.pi) / args.n
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
        # The top 32 faces
        for num in range(2, args.n+1):
            f.write("f " + "1 " + str(num) + " " + str(num+1) + "\n")
            if num is args.n: 
                f.write("f " + "1 " + "2 " + str(num+1) + "\n")
        # 64 more faces for triangle strip
        for num in range(2, args.n+1):
            f.write("f " + str(num) + " " + str(args.n+num+1) + " " + str(num+1) + "\n")
            f.write("f " + str(num+1) + " " + str(args.n+num+1) + " " + str(args.n+num+2) + "\n")

        f.write("f " + str(args.n+1) + " " + str(args.n*2+2) + " " + str(2) + "\n")
        f.write("f " + str(2) + " " + str(args.n*2+2) + " " + str(args.n+3) + "\n")
        # The 32 bottom faces
        for num in range(args.n+3, ((args.n*2)+2)):
            f.write("f " + str(args.n+2) + " " + str(num) + " " + str(num+1) + "\n")
            if num is ((args.n*2)+1):
                f.write("f " + str(args.n+2) + " " + str(args.n+3) + " " + str(num+1) + "\n")
    else:
        print("Invalid geometry (sphere | cylinder)")
else:
    print("Missing arguments -g or -o")
