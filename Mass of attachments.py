import numpy as np
import math
from buckling import *

mass_tank = 888.4
flat_distance = 0.04
height_lower_curtain = 0.66
height_upper_curtain = 0.34
radius_curtain = 0.56
materials = [['Ti6AI4V STA', 4500, 828000000, 760000000, 0.342, 110000000000],
             ['Al 2024', 2780, 324000000, 283000000, 0.33, 73100000000],
             ['Fe 4130', 7850, 435000000, 427500000, 0.29, 205000000000]]


# [material_name,material_density,material_poisson_ratio,material_axial_stress,material_shear_stress,young_modulus]

def stress_shear_crosssection(thickness_curtain, radius_curtain):
    V = (1.5 * 9.81 * mass_tank) / 2
    I = (math.pi * thickness_curtain * (radius_curtain / 2) ** 3) / 8
    Q = 2 * radius_curtain ** 2 * thickness_curtain
    shear_stress = (V * Q) / (I * thickness_curtain)
    return shear_stress


def bending_stress_curtain(radius_curtain, thickness_curtain, height_curtain):
    lateral_load = 1.5 * 9.81 * mass_tank
    I = math.pi * thickness_curtain * (radius_curtain) ** 3
    bending_stress = (lateral_load * height_curtain * radius_curtain) / (2 * I)
    return bending_stress


def shear_stress_connection(radius_curtain):
    V = 4 * 9.81 * mass_tank
    I = 2 * math.pi * radius_curtain * (flat_distance ** 2)
    Q = ((flat_distance ** 2) * radius_curtain * math.pi) / 2
    t = 2 * math.pi * radius_curtain
    shear_stress = (V * Q) / (I * t)
    return shear_stress


def axial_stresses(thickness_curtain, radius_curtain):
    F = 4 * 9.81 * mass_tank
    A = thickness_curtain * 2 * math.pi * radius_curtain
    axial_stress = F / A
    return axial_stress


def shell_buckling(thickness_curtain, radius_curtain, height_curtain, material):
    Buckles = False
    buckling_stress = find_stress_shell_buckling(0, material[5], radius_curtain, thickness_curtain, material[4], height_curtain)
    if buckling_stress > axial_stresses(thickness_curtain, radius_curtain):
        Buckles = True
    return Buckles


def configuration_loop(height_curtain):
    for thickness_curtain in np.arange(0.001, 0.1, 0.001):
        for material in materials:
            if (shell_buckling(thickness_curtain, radius_curtain, height_curtain, material) == False) and (
                    axial_stresses(thickness_curtain, radius_curtain) <= material[3]) and (
                    bending_stress_curtain(radius_curtain, thickness_curtain, height_curtain) <= material[3]) and (
                    shear_stress_connection(radius_curtain) <= material[4]) and (
                    stress_shear_crosssection(thickness_curtain, radius_curtain) <= material[4]):
                print(
                    f"Material: {material[0]} \n Thickness:{thickness_curtain} \n Mass: {(height_curtain * 2 * math.pi * radius_curtain * thickness_curtain)}")
                break


print(' -- Lower curtain configuration --')
configuration_loop(height_lower_curtain)
print(' -- Upper curtain configuration --')
configuration_loop(height_upper_curtain)
