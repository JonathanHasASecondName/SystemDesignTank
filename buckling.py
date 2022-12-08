import numpy as np


def find_stress_column_buckling(a=2, b):
    pass

def find_stress_shell_buckling(p, E, R, t_1, labda, v, L):
    Q = p/E * (R/t_1)**2
    k = labda + 12/np.pi**4 * L**4/(R**2*t_1**2) * (1-v**2)/labda

    part_a = 1.983 - 0.983*np.exp(-23.14*Q)
    part_b = k*np.pi**2 * E/(12*(1-v**2))
    part_c = t_1**2/(L**2)
    return part_a*part_b*part_c
