#!/usr/bin/python3
# Brandon Litwin, Project 2, Computer Graphics
import numpy as np
import png

e = np.array([0.0, 0.0, 0.0])
width = 1280
height = 720
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
    def __init__(self, o):
        self.objects = o

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
    l = -1.778
    r = 1.778
    t = 1
    b = -1
    u = l + (((r-l) * (i+0.5)) / width)
    v = b + (((t-b) * (j+0.5)) / height)
    w = -1 # point behind the eye
    U = (1,0,0)
    V = (0,1,0)
    W = (0,0,1)
    
    d = (u,v,w)
    
    return d

def find_intersection(ray,object):
    # Computing ray-sphere intersection
    d = ray.distance
    c = object.center
    r = object.radius

    discriminant = np.square(np.dot(d, e-c)) - (np.dot(d,d) * (np.dot(e-c, e-c) - (r * r)))
    if discriminant >= 0:
        t = (np.dot(np.multiply(-1,d), e-c) + np.sqrt(discriminant)) / np.dot(d,d)
        t2 = (np.dot(np.multiply(-1,d), e-c) - np.sqrt(discriminant)) / np.dot(d,d)
        if (t < t2):
            p = e + np.multiply(t,d)
        else:
            t = t2
            p = e + np.multiply(t,d)
        n = 2 * p-c
        return t, p, n, object
    else:
        return None

def evaluate_shading(p, n, intersecting_sphere):
    ki = intersecting_sphere.surface.material.color 
    ks = [255,255,255] 
    
    n = (p-intersecting_sphere.center) / intersecting_sphere.radius
    l = np.array(light_source.position - p)
    phong = intersecting_sphere.surface.material.shininess
    v = np.array(e)
    
    normalized_l_v = np.sqrt(np.sum(np.square(l+v)))

    h = (v + l) / (normalized_l_v)
    intensity = 40

    pixel_red = int((ki[0]/255) * intensity * max(0, np.dot(n,l))) + int((ks[0]/255)*intensity*np.power(max(0, np.dot(n,h)),phong))
    pixel_green = int((ki[1]/255) * intensity * max(0, np.dot(n,l))) + int((ks[1]/255)*intensity*np.power(max(0, np.dot(n,h)),phong))
    pixel_blue = int((ki[2]/255) * intensity * max(0, np.dot(n,l))) + int((ks[2]/255)*intensity*np.power(max(0, np.dot(n,h)),phong))
    pixel_color = [pixel_red, pixel_green, pixel_blue]
    return pixel_color

# Instantiate all classes needed for scene
light_source = Light(np.array([1.0,2.0,1.0]), np.array([255,255,255]))
sphere_material = Material([255, 0, 0], 1000)
sphere2_material = Material([0, 0, 255], 1000)
sphere_surface = Surface(sphere_material)
sphere2_surface = Surface(sphere2_material)
sphere = Sphere(sphere_surface, np.array([-1.0,0.0,-3.0]), 1.0)
sphere2 = Sphere(sphere2_surface, np.array([-1.0,1.0,-5.0]), 1.0)
group = Group([sphere2])
scene = Scene(group, light_source, [0,0,0])
pixel_colors = []
for i in range(0,height):
    for j in range(0, width):
        # Create a ray object with origin e and distance that is computed from the compute_ray function
        ray = Ray(e,compute_ray(i,j))
        ray_intersection = find_intersection(ray,sphere)
        ray_intersection2 = find_intersection(ray,sphere2)

        if (ray_intersection is not None):
            intersection_time = ray_intersection[0]
            intersection_point = ray_intersection[1]
            intersection_normal = ray_intersection[2]
            intersecting_sphere = ray_intersection[3]
            
            hit_record = HitRecord(intersection_time, intersection_normal, intersecting_sphere.surface)
            # Adding the shaded colors to the pixel coloes array
            pixel_colors.append(evaluate_shading(intersection_point, intersection_normal, intersecting_sphere)[0])
            pixel_colors.append(evaluate_shading(intersection_point, intersection_normal, intersecting_sphere)[1])
            pixel_colors.append(evaluate_shading(intersection_point, intersection_normal, intersecting_sphere)[2])
        elif (ray_intersection2 is not None):
            intersection_time = ray_intersection2[0]
            intersection_point = ray_intersection2[1]
            intersection_normal = ray_intersection2[2]
            intersecting_sphere = ray_intersection2[3]
        
            hit_record = HitRecord(intersection_time, intersection_normal, intersecting_sphere.surface)
            pixel_colors.append(evaluate_shading(intersection_point, intersection_normal, intersecting_sphere)[0])
            pixel_colors.append(evaluate_shading(intersection_point, intersection_normal, intersecting_sphere)[1])
            pixel_colors.append(evaluate_shading(intersection_point, intersection_normal, intersecting_sphere)[2])
        else:
            # No intersections so just make it the background color
            pixel_colors.append(scene.background_color[0])
            pixel_colors.append(scene.background_color[1]) 
            pixel_colors.append(scene.background_color[2]) 
f = open('scene.png', 'wb')      
w = png.Writer(width = width, height = height, greyscale = False)
w.write_array(f, pixel_colors)
f.close()
