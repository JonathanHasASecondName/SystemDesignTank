import numpy as np
import math
mass_tank = 0
material_poisson_ratio =
material_shear_stress =
material_axial_stress =
flat_distance = 0.04
bottom_margin = 0.1
height_curtain = #needs to be found
radius_curtain =
materials =

#[MaterialName,density,material_axial_stress,material_axial_stress,material_shear_stress]

def stress_shear_crosssection(thickness_curtain,radius_curtain):
    V = (1.5*9.81*mass_tank)/2
    I = (math.pi * thickness_curtain * (radius_curtain/2)**3)/8
    Q = 2*radius_curtain**2 * thickness_curtain
    shear_stress = (V*Q)/(I*thickness_curtain)
    return shear_stress

def bending_stress_curtain(radius_curtain,thickness_curtain,height_curtain):
    lateral_load = 1.5 * 9.81 * mass_tank
    I = math.pi * thickness_curtain*(radius_curtain)**3
    bending_stress = (lateral_load * height_curtain * radius_curtain)/(2 * I)
    return bending_stress

def shear_stress_connection(radius_curtain):
    V = 4 * 9.81 * mass_tank
    I = 2*math.pi*radius_curtain*(flat_distance**2)
    Q = ((flat_distance**2)*radius_curtain*math.pi)/2
    t = 2*math.pi*radius_curtain
    shear_stress = (V*Q)/(I*t)
    return shear_stress

def axial_stresses(thickness_curtain,radius_curtain):
    F= 6*9.81*mass_tank2
    A= thickness_curtain*2*math.pi*radius_curtain
    axial_stress = F/A
    return axial_stress

def shell_buckling(thickness_curtain,radius_curtain,height_curtain,poisson_ratio):
    Buckles = False
    #get buckling stress
    if buckling_stress > maxial_stresses(thickness_curtain,radius_curtain):
        Buckles = True
    return Buckles

def configuration_loop(height_curtain):
    for material in materials:
        for thickness_curtain in range(0,0.1,0.001):
            if (shell_buckling(thickness_curtain,radius_curtain,height_curtain,poisson_ratio) == False) and (axial_stresses(thickness_curtain,radius_curtain)<= material_axial_stress) and (bending_stress_curtain(radius_curtain,thickness_curtain,height_curtain)<= material_axial_stress) and (shear_stress_connection(radius_curtain)<= material_shear_stress) and (stress_shear_crosssection(thickness_curtain,radius_curtain) <= material_shear_stress):
                print(thickness_curtain, material)
                break

print('First')
configuration_loop()




