import numpy as np

def find_cylinder_cross_section_area(r,t_1): #VALIDATED
    A=np.pi*r**2-np.pi*(r-t_1)**2
    return A
def find_cylinder_moment_of_inertia(r,t_1): #VALIDATED
    I=0.25*np.pi*(r**4-(r-t_1)**4)
    return I
def find_stress_column_buckling(A,L,I,E):
    column_buckling_critical_stress= np.pi**2*E*I/(A*L**2)
    return column_buckling_critical_stress

def find_stress_shell_buckling(p, E, R, t_1, labda, v, L):
    Q = p/E * (R/t_1)**2
    k = labda + 12/np.pi**4 * L**4/(R**2*t_1**2) * (1-v**2)/labda

    part_a = 1.983 - 0.983*np.exp(-23.14*Q)
    part_b = k*np.pi**2 * E/(12*(1-v**2))
    part_c = t_1**2/(L**2)
    return part_a*part_b*part_c


#print(find_cylinder_moment_of_inertia(1,0.01),find_cylinder_cross_section_area(1,0.01),find_stress_column_buckling(find_cylinder_cross_section_area(1,0.01),10,find_cylinder_moment_of_inertia(1,0.01),500*10**6))