import numpy as np

def find_hoop_stress(p,r,t):
    return (p*r)/t

def find_longitudinal_stress(p,r,t):
    return (p*r)/(2*t)

def find_min_thickness_cylinder(p,r,sigma_y):
    return (p*r)/sigma_y

def find_min_thickness_sphere(p,r,sigma_y):
    return (p*r)/(2*sigma_y) # reference paper on launcher sizing DARE

