import numpy as np
import math
mass_tank = 0

def stress_shear_force_curtain(mass_tank,thickness_curtain,radius_curtain):
    V_y = (2*9.81*mass_tank)/2
    I_x = (math.pi * thickness_curtain * (radius_curtain/2)**3)/8
    Q_x = 4 * radius_curtain**2 * thickness_curtain
    shear_stress = (V_y*Q_x)/(I_x*thickness_curtain)
    return shear_stress

def bending_stress_bottom_curtain(diameter, thickness, lateral_load, height, mass_tank):
    lateral_load = 2 * 9.81 * mass_tank
    I_xx = (math.pi * thickness * diameter ** 3)/8


    return (0.5 * lateral_load * height * diameter)/(2 * I_xx)

