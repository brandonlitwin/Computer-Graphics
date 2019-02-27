#!/usr/bin/python3
# Brandon Litwin, Project 2, Computer Graphics
import numpy as np
import png
import time

c = np.array([0.0,0.0,2.0])
radius = 1.0
# Create a sphere as an array with coordinates x, y, z as 0,0,2 and radius 1.0
sp = np.array([0.0,0.0,2.0,1.0])
e = np.array([0.0, 0.0, 0.0])
resolution = 720*1280
width = 1280
height = 720

class HitRecord:
    def __init__(self, t, n):
        self.time = t
        self.normal = n
        #self.surface = s

class Light:
    def __init__(self, p, c):
        self.position = p
        self.color = c

"""class Scene:

class Group:
    
class Surface:"""

class Material:
    def __init__(self, c, s):
        self.color = c
        self.shininess = s

class Ray:
    def __init__(self, o, d):
        self.origin = o
        self.distance = d

def compute_ray(i,j):
    intersects_sphere = True
    l = -1
    r = 1
    t = 1
    b = -1
    u = l + (r-l) * ((i+0.5)/width)
    v = b + (t-b) * ((j+0.5)/height)
    w = -1 # point behind the eye
    s = e + u + v + w # s = e + uU + vV + wW?
    d = s - e
    return d

def find_intersection(ray):
    # Computing ray-sphere intersection
    d = ray.distance
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
        else:
            n = 2 * (p2-c)
        return n
    
for i in range(1,height+1):
    for j in range(1, width+1):
        # Create a ray object with origin e and distance that is computed from the compute_ray function
        ray = Ray(e,compute_ray(i,j))
        ray_intersection_normal = find_intersection(ray)
        if (ray_intersection_normal is not None):
            ray.normal = ray_intersection_normal
            localtime = time.localtime(time.time())
            hit_record = HitRecord(localtime, ray.normal)
        


