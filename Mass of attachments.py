import numpy as np
import math
mass_tank = 0
material
def stress_shear_crosssection(mass_tank,thickness_curtain,radius_curtain):
    V_y = (2*9.81*mass_tank)/2
    I_x = (math.pi * thickness_curtain * (radius_curtain/2)**3)/8
    Q_x = 2*radius_curtain**2 * thickness_curtain
    shear_stress = (V_y*Q_x)/(I_x*thickness_curtain)
    return shear_stress

def bending_stress_bottom_curtain(diameter, thickness, lateral_load, height, mass_tank):
    lateral_load = 2 * 9.81 * mass_tank
    I_xx = (math.pi * thickness * diameter ** 3)/8
    bending_stress = (0.5 * lateral_load * height * diameter)/(2 * I_xx)



    return bending_stress


def shear_stress_connection():
    return

def axial_stresses(mass_tank,thickness_curtain,radius_curtain,height_curtain):
    F_lateral = (2*9.81*mass_tank)/2
    F_axial = 6*9.81*mass_tank
    A_lateral = height_curtain*thickness_curtain*2
    A_axial = thickness_curtain*2*math.pi*radius_curtain
    axial_stress_lateral = F_lateral/A_lateral
    axial_stress_axial = F_axial/A_axial
    return max(axial_stress_lateral,axial_stress_axial)
