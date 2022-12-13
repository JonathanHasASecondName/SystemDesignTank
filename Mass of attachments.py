from math import pi
def stress_shear_force_curtain():
    return

def bending_stress_bottom_curtain(diameter, thickness, lateral_load, height):
    I_xx = (pi * thickness * diameter ** 3)/8

    return (lateral_load * height * diameter)/(2 * I_xx)