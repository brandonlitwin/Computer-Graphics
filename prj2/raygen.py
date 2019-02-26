#!/usr/bin/python3
# Brandon Litwin, Project 2, Computer Graphics
import numpy as np
import png

c = np.array([0.0,0.0,2.0])
radius = 1.0
# Create a sphere as an array with coordinates x, y, z as 0,0,2 and radius 1.0
sp = np.array([0.0,0.0,2.0,2.0])
e = np.array([0.0, 0.0, 0.0])
resolution = 720*1280
width = 1280
height = 720

def compute_ray(i,j):
    intersects_sphere = True
    l = -1
    r = 1
    t = 1
    b = -1
    u = l + (r-l) * ((i+0.5)/width)
    v = b + (t-b) * ((j+0.5)/height)
    #n = 2*(p-c)
    w = 1 # near point between the eye and sphere
    s = e + u + v + w
    d = s - e
    return d

def find_intersection(d):
    # Computing ray-sphere intersection
    discriminant = np.square(np.dot(d, e-c)) - (np.dot(d,d) * (np.dot(e-c, e-c)) - (radius * radius))
    # A negative discriminant means no intersections
    if discriminant >= 0:
        t = (np.dot(-d, e-c) + np.sqrt(discriminant)) / np.dot(d,d)
        t2 = (np.dot(-d, e-c) - np.sqrt(discriminant)) / np.dot(d,d)
        p = e + (t * d)
        p2 = e + (t2 * d)
        # p is the point of intersection, we only care about the one that is closer to the eye
        if (p[0] <= p2[0]):
            # Compute the normal vector
            n = 2 * (p-c)
            return (p,n)
        else:
            n = 2 * (p2-c)
            return (p2,n)
    else:
        return False
    

count = 0
for i in range(1,height+1):
    for j in range(1, width+1):
        ray = compute_ray(i,j)
        ray_intersection = find_intersection(ray)
        if (ray_intersection):
            count = count + 1
        
print(count)
# for each pixel in 720x1280, compute viewing ray
# p(t) = e + t(s-e)
# e is the eye location, s is the point on the screen


