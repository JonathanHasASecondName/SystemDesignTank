import math
from buckling import *

mass_tank_structure = 200
mass_fuel = 884
mass_spacecraft = 425.1-31.7
#425.1-31.7
flat_distance = 0.04
height_lower_curtain = 0.66
height_upper_curtain = 0.34
radius_curtain = 0.56
materials = [['Ti6AI4V STA', 4500, 828000000, 760000000, 0.342, 110000000000],
             ['Al 2024', 2780, 324000000, 283000000, 0.33, 73100000000],
             ['Fe 4130', 7850, 435000000, 427500000, 0.29, 205000000000],
             ['Carbon Fibre', 1600, 600000000, 90000000, 0.77, 70000000000]]


# [material_name,material_density,material_axial_stress,material_shear_stress,material_poisson_ratio,young_modulus]

def stress_shear_crosssection(thickness_curtain,radius_curtain,mass_tank_structure,mass_fuel):
    V = (1.5 * 9.81 * (mass_tank_structure+mass_fuel+mass_spacecraft)) / 2
    I = (math.pi * thickness_curtain * (radius_curtain / 2) ** 3) / 8
    Q = 2 * radius_curtain ** 2 * thickness_curtain
    shear_stress = (V * Q) / (I * thickness_curtain)
    return shear_stress


def bending_stress_curtain(radius_curtain, thickness_curtain, height_curtain, mass_tank_structure, mass_fuel):
    lateral_load = 1.5 * 9.81 * (mass_tank_structure+mass_fuel+mass_spacecraft)
    I = math.pi * thickness_curtain * (radius_curtain) ** 3
    bending_stress = (lateral_load * height_curtain * radius_curtain) / (2 * I)
    return bending_stress


def shear_stress_connection(radius_curtain, mass_tank_structure, mass_fuel):
    V = 4 * 9.81 * (mass_tank_structure+mass_fuel+mass_spacecraft)
    I = 2 * math.pi * radius_curtain * (flat_distance ** 2)
    Q = ((flat_distance ** 2) * radius_curtain * math.pi) / 2
    t = 2 * math.pi * radius_curtain
    shear_stress = (V * Q) / (I * t)
    return shear_stress


def axial_stresses(thickness_curtain, radius_curtain, mass_tank_structure, mass_fuel):
    F = 4 * 9.81 * (mass_tank_structure+mass_fuel+mass_spacecraft)
    A = thickness_curtain * 2 * math.pi * radius_curtain
    axial_stress = F / A
    return axial_stress


def shell_buckling(thickness_curtain, radius_curtain, height_curtain, material):
    Buckles = False
    buckling_stress = find_stress_shell_buckling(0, material[5], radius_curtain, thickness_curtain, material[4], height_curtain)
    if buckling_stress < axial_stresses(thickness_curtain, radius_curtain, mass_tank_structure, mass_fuel):
        Buckles = True
    return Buckles

def configuration_loop(height_curtain, mass_tank_structure, mass_fuel, radius_curtain=0.56):
    Running=True
    for thickness_curtain in np.arange(0.0001, 0.003, 0.0001):
        if Running:
            for material in materials:
                #print(stress_shear_crosssection(thickness_curtain,radius_curtain,mass_tank_structure,mass_fuel),material[3])
                if (shell_buckling(thickness_curtain, radius_curtain, height_curtain, material) == False) and (
                        axial_stresses(thickness_curtain, radius_curtain, mass_tank_structure, mass_fuel) <= material[2]) and (
                        bending_stress_curtain(radius_curtain, thickness_curtain, height_curtain, mass_tank_structure, mass_fuel) <= material[2]) and (
                        shear_stress_connection(radius_curtain, mass_tank_structure, mass_fuel) <= material[3]) and (
                        stress_shear_crosssection(thickness_curtain,radius_curtain,mass_tank_structure,mass_fuel) <= material[3]):
                    #print(f"Material: {material[0]} \n Thickness:{thickness_curtain} \n Mass: {(height_curtain * 2 * math.pi * radius_curtain * thickness_curtain * material[1])}")
                    return (material[0], thickness_curtain, height_curtain * 2 * math.pi * radius_curtain * thickness_curtain * material[1])
                    Running = False

#print(' -- Lower curtain configuration --')
#configuration_loop(height_lower_curtain, mass_tank_structure, mass_fuel, radius_curtain=0.56)
#print(' -- Upper curtain configuration --')
#configuration_loop(height_upper_curtain, mass_tank_structure, mass_fuel, radius_curtain=0.56)
