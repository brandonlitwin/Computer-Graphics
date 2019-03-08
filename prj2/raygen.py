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
    #s = e + u*U + v*V + w*W 
    #d = s - e
    #d = (0,0,-1)
    #direction = u*U + v*V + w*W
		#         = (u,0,0) + (0,v,0) + (0,0,w)
		#         = (u,v,w)
    #d = direction - e
    d = (u,v,w)
    #print("first d")
    #print(d)
    #d = u*U + v*V + w*W
    #print("second d")
    #print(d)
    return d

def find_intersection(ray,object):
    # Computing ray-sphere intersection
    d = ray.distance
    #print(objects[0].center, objects[1].center)
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

    #c2 = spihere2.center
    #r2 = sphere2.radius
    #hit_objects = []
    #print(objects)
    """for i in range(0,len(objects)):
        #print(objects[i].center, objects[i].radius)
        c = objects[i].center
        r = objects[i].radius
        is_hit = False
        #print(c,r)
        discriminant = np.square(np.dot(d, e-c)) - (np.dot(d,d) * (np.dot(e-c, e-c) - (r * r)))
        if (discriminant >= 0):
            is_hit = True
            hit_object_info = []
            #hit_objects.append(object)
            t = (np.dot(np.multiply(-1,d), e-c) + np.sqrt(discriminant)) / np.dot(d,d)
            t2 = (np.dot(np.multiply(-1,d), e-c) - np.sqrt(discriminant)) / np.dot(d,d)
            if (t < t2):
                p = e + np.multiply(t,d)
            else:
                t = t2
                p = e + np.multiply(t,d)
            #n = 2 * p-c
            hit_object_info.append(object)
            hit_object_info.append(t)
            #hit_object_info.append(n)
            hit_object_info.append(p)
            hit_objects.append(hit_object_info)
        else:
            if is_hit == False:
                #print("none")
                return None
            
    #if len(hit_objects) == 1:
        #print(hit_objects)
    closest_t = hit_objects[0][1]
    closest_p = hit_objects[0][2]
    closest_object = hit_objects[0][0]
    n = 0
    for object in hit_objects:
        if object[1] < closest_t:
            closest_object = object[0]
            closest_t = object[1]
            closest_p = object[2]
            n = 2 * (closest_p - closest_object.center)

    return closest_t, closest_p, n, closest_object"""
        


    #discriminant = np.square(np.dot(d, e-c)) - (np.dot(d,d) * (np.dot(e-c, e-c) - (r * r)))
    #discriminant2 = np.square(np.dot(d, e-c2)) - (np.dot(d,d) * (np.dot(e-c2, e-c2) - (r2 * r2)))
    #print("discr")
    # A negative discriminant means no intersections
    """if discriminant >= 0 or discriminant2 >= 0:
        #print(np.multiply(-1,d))
        t = None
        t_2 = None
        p = None
        p2 = None
        if discriminant >= 0:
            t = (np.dot(np.multiply(-1,d), e-c) + np.sqrt(discriminant)) / np.dot(d,d)
            t2 = (np.dot(np.multiply(-1,d), e-c) - np.sqrt(discriminant)) / np.dot(d,d)
        if discriminant2 >= 0:
            t_2 = (np.dot(np.multiply(-1,d), e-c2) + np.sqrt(discriminant2)) / np.dot(d,d)
            t2_2 = (np.dot(np.multiply(-1,d), e-c2) - np.sqrt(discriminant2)) / np.dot(d,d)
        if t is not None:
            if t < t2:
                p = e + (np.multiply(t,d))
            else:
                p = e + (np.multiply(t2,d))

        if t_2 is not None:
            if t_2 < t2_2:
                p2 = e + (np.multiply(t_2,d))
            else:
                p2 = e + (np.multiply(t2_2,d))

        # p is the point of intersection, we only care about the one that is closer to the eye
        if p is not None:
            if p2 is not None:
                if p[0] <= p2[0]:
		    #print(p)
                 # Compute the normal vector
		    n = 2 * (p-c)
                else:
		    #print(p2)
                    n = 2 * (p2-c2)
                    t = t2
            else:
                n = 2 * (p-c)
                if t2 < t:
                    t = t2
            return t, n, sphere
        elif p2 is not None:
            #print(p2)
            n = 2 * (p2-c2)
            if t2_2 < t_2:
                t_2 = t2_2
            return t_2, n, sphere2"""


def evaluate_shading(p, n, intersecting_sphere):
    ki = intersecting_sphere.surface.material.color 
    #print(ki)
    ks = [211,211,211] # light gray
    # l is the vector pointing from p to the light
    #p = (n/2) + intersecting_sphere.center
    n = (p-intersecting_sphere.center) / intersecting_sphere.radius
    l = np.array(light_source.position - p)
    phong = intersecting_sphere.surface.material.shininess
    v = np.array(e)
    #normalized_v = v / np.sqrt(np.sum(v**2)) 
    normalized_l_v = np.sqrt(np.sum(np.square(l+v)))

    h = (v + l) / (normalized_l_v)
    intensity = 40
    """shaded_color = [] 
    shaded_color.append(k[0] * i[0])
    shaded_color.append(k[1] * i[1])
    shaded_color.append(k[2] * i[2])
    print(shaded_color)"""
    #print(np.dot(n,h))
    #pixel_color = ki#*i*max(0, np.dot(n,l)) #+ ks * i * np.power(max(0, np.dot(n,h))),phong)
    pixel_red = int((ki[0]/255) * intensity * max(0, np.dot(n,l))) + int((ks[0]/255)*intensity*np.power(max(0, np.dot(n,h)),phong))
    pixel_green = int((ki[1]/255) * intensity * max(0, np.dot(n,l))) + int((ks[1]/255)*intensity*np.power(max(0, np.dot(n,h)),phong))
    pixel_blue = int((ki[2]/255) * intensity * max(0, np.dot(n,l))) + int((ks[2]/255)*intensity*np.power(max(0, np.dot(n,h)),phong))
    pixel_color = [pixel_red, pixel_green, pixel_blue]
    #KdId = (rk x rI, gK x gI, bk x bI)
    #print(pixel_color)
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
scene = Scene(group, light_source, [255,255,255])
#print(scene.object_list.objects)
#print(group.objects[1].center)
#print(scene.object_list)
# Create array for pixel colors
#pixel_colors = np.empty([resolution])
#np.append(pixel_colors, np.array([0,0,0]))
pixel_colors = []
for i in range(0,height):
    pixel_row = []
    for j in range(0, width):
        # Create a ray object with origin e and distance that is computed from the compute_ray function
        ray = Ray(e,compute_ray(i,j))
        #smallest_t = 1000
        #for scene_object in scene.object_list.objects:
            #print(scene_object.surface.material.color)
        ray_intersection = find_intersection(ray,sphere)
        ray_intersection2 = find_intersection(ray,sphere2)

        if (ray_intersection is not None):
                #if ray_intersection[0] < smallest_t:
            intersection_time = ray_intersection[0]
            intersection_point = ray_intersection[1]
            intersection_normal = ray_intersection[2]
            intersecting_sphere = ray_intersection[3]
            #print(intersection_time, intersection_point, inter
            hit_record = HitRecord(intersection_time, intersection_normal, intersecting_sphere.surface)
            #pixel_colors = np.append(pixel_colors, evaluate_shading(intersection_normal)) 
            #np.insert(pixel_colors, count, evaluate_shading(intersection_normal))
            #pixel.append(evaluate_shading(intersection_normal)[0], evaluate_shading(intersection_normal)[1], evaluate_shading(intersection_normal)[2])
            pixel_colors.append(evaluate_shading(intersection_point, intersection_normal, intersecting_sphere)[0])
            pixel_colors.append(evaluate_shading(intersection_point, intersection_normal, intersecting_sphere)[1])
            pixel_colors.append(evaluate_shading(intersection_point, intersection_normal, intersecting_sphere)[2])
        elif (ray_intersection2 is not None):
                #if ray_intersection[0] < smallest_t:
            intersection_time = ray_intersection2[0]
            intersection_point = ray_intersection2[1]
            intersection_normal = ray_intersection2[2]
            intersecting_sphere = ray_intersection2[3]
            #print(intersection_time, intersection_point, inter
            hit_record = HitRecord(intersection_time, intersection_normal, intersecting_sphere.surface)
            #pixel_colors = np.append(pixel_colors, evaluate_shading(intersection_normal)) 
            #np.insert(pixel_colors, count, evaluate_shading(intersection_normal))
            #pixel.append(evaluate_shading(intersection_normal)[0], evaluate_shading(intersection_normal)[1], evaluate_shading(intersection_normal)[2])
            pixel_colors.append(evaluate_shading(intersection_point, intersection_normal, intersecting_sphere)[0])
            pixel_colors.append(evaluate_shading(intersection_point, intersection_normal, intersecting_sphere)[1])
            pixel_colors.append(evaluate_shading(intersection_point, intersection_normal, intersecting_sphere)[2])
        else:
            #pixel_colors = np.append(pixel_colors, scene.background_color)
            #pixel.append(scene.background_color[0],scene.background_color[1],scene.background_color[2])
            pixel_colors.append(scene.background_color[0])
            pixel_colors.append(scene.background_color[1]) 
            pixel_colors.append(scene.background_color[2]) 
        #pixel_row.append(pixel)
    #print(pixel_row)        
    #pixel_colors.append(pixel_row)

#print(len(pixel_colors))
#print(pixel_colors)
#print(len(pixel_colors[0][0]))

#png.from_array(pixel_colors, 'RGB').save('scene.png')
f = open('scene.png', 'wb')      # binary mode is important
w = png.Writer(width = width, height = height, greyscale = False)
w.write_array(f, pixel_colors)
f.close()
