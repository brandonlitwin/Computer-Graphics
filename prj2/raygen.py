#!/usr/bin/python3
# Brandon Litwin, Project 2, Computer Graphics
import numpy as np
import png

e = np.array([0.0, 0.0, 0.0])
width = 426
height = 240
resolution = width*height

# The class definitions
class HitRecord:
    def __init__(self, t, n, s):
        self.time = t
        self.normal = n
        self.surface = s

class Light:
    def __init__(self, p, c):
        self.position = p
        self.color = c

class Scene:
    def __init__(self, g, l, c):
        self.object_list = g
        self.light_source = l
        self.background_color = c

class Group:
    def __init__(self, s):
        self.surface = s

class Sphere:
    def __init__(self, s, c, r):
        self.surface = s
        self.center = c
        self.radius = r
    
class Surface:
    def __init__(self, m):
        self.material = m

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
    u = l + (((r-l) * (i+0.5)) / width)
    v = b + (((t-b) * (j+0.5)) / height)
    w = -1 # point behind the eye
    U = 1
    V = 1
    W = 1
    # The 2's come from the distances x and y (l,r) and (t,b)
    s = e + u*U + v*V + w*W 
    d = s - e
    #direction = u*U + v*V + w*W
    #d = direction - e
    #print("first d")
    #print(d)
    #d = u*U + v*V + w*W
    #print("second d")
    #print(d)
    return d

def find_intersection(ray):
    # Computing ray-sphere intersection
    d = ray.distance
    c = sphere.center
    r = sphere.radius

    discriminant = np.square(np.dot(d, e-c)) - (np.dot(d,d) * (np.dot(e-c, e-c)) - (r * r))
    #print("discr")
    #print(discriminant)
    # A negative discriminant means no intersections
    if discriminant >= 0:
        t = (np.dot(-1*d, e-c) + np.sqrt(discriminant)) / np.dot(d,d)
        t2 = (np.dot(-1*d, e-c) - np.sqrt(discriminant)) / np.dot(d,d)
        #print(t)
        p = e + (t * d)
        p2 = e + (t2 * d)
        # p is the point of intersection, we only care about the one that is closer to the eye
        if (p[0] <= p2[0]):
            # Compute the normal vector
            n = 2 * (p-c)
        else:
            n = 2 * (p2-c)
            t = t2
        return t, n

def evaluate_shading(n):
    i = light_source.color
    k = sphere.surface.material.color 
    # l is the vector pointing from p to the light
    p = (n/2) + sphere.center
    l = p - light_source.position
    #zero_vector = np.array([0.0,0.0,0.0])
    pixel_color = k#np.array([255,0,0]) #k*i*max(0, np.dot(n,l)))
    return pixel_color

# Instantiate all classes needed for scene
light_source = Light(np.array([1.0,5.0,1.0]), np.array([255,255,255]))
sphere_material = Material(np.array([255, 0, 0]), 1)
sphere_surface = Surface(sphere_material)
sphere = Sphere(sphere_surface, np.array([0.0,0.0,-2.0]), 1.0)
scene = Scene(sphere, light_source, [0,0,0]) 
# Create array for pixel colors
#pixel_colors = np.empty([resolution])
#np.append(pixel_colors, np.array([0,0,0]))
pixel_colors = []
for i in range(1,height+1):
    #pixel_row = []
    for j in range(1, width+1):
        # Create a ray object with origin e and distance that is computed from the compute_ray function
        ray = Ray(e,compute_ray(i,j))
        ray_intersection = find_intersection(ray)
        if (ray_intersection is not None):
            intersection_time = ray_intersection[0]
            intersection_normal = ray_intersection[1]
            hit_record = HitRecord(intersection_time, intersection_normal, sphere_surface)
            #pixel_colors = np.append(pixel_colors, evaluate_shading(intersection_normal)) 
            #np.insert(pixel_colors, count, evaluate_shading(intersection_normal))
            pixel_colors.append(evaluate_shading(intersection_normal)[0])
            pixel_colors.append(evaluate_shading(intersection_normal)[1])
            pixel_colors.append(evaluate_shading(intersection_normal)[2])

        else:
            #pixel_colors = np.append(pixel_colors, scene.background_color)
            pixel_colors.append(scene.background_color[0])
            pixel_colors.append(scene.background_color[1])
            pixel_colors.append(scene.background_color[2])
    #print(pixel_row)        
    #pixel_colors.append(pixel_row)
            #np.insert(pixel_colors, count, scene.background_color)
        #count = count + 1
        #print(pixel_colors[count])
    #print(i)
    #print(pixel_colors)
    #print(pixel_colors.shape)

#print(pixel_colors)
f = open('scene.png', 'wb')      # binary mode is important
w = png.Writer(width = width, height = height, alpha = 'RGBA')
w.write_array(f, pixel_colors)
f.close()
