import numpy as np

def find_cylinder_cross_section_area(r,t_1): #VALIDATED
    A=np.pi*r**2-np.pi*(r-t_1)**2
    return A
def find_cylinder_moment_of_inertia(r,t_1): #VALIDATED
    I=0.25*np.pi*(r**4-(r-t_1)**4)
    return I
def find_stress_euler_column_buckling(A,L,I,E):
    # This is for Euler column buckling - not applicable to our tanks.
    column_buckling_critical_stress= np.pi**2*E*I/(A*L**2)
    return column_buckling_critical_stress
def find_stress_short_column_buckling(K,L,r,sigma_y,E): #VALIDATED
    # Parabolic formula from p.534 Roark's Formulas for Stress
    lambda_ = ((K*L)/(r*np.pi))*((sigma_y/E)**(1/2))
    sigma_allow = sigma_y*(1-(lambda_**2)/4)
    return sigma_allow

def find_axial_stress(F_axial,A): #VALIDATED
    axial_stress=F_axial/A
    return axial_stress
def find_stress_shell_buckling(p, E, r, t_1, v, L): #VALIDATED
    k_values = []
    for lambda_ in range(1,100):
        Q = p/E * (r/t_1)**2
        k_values.append(lambda_ + (12/np.pi**4) * (L**4/(r**2*t_1**2)) * ((1-v**2)/lambda_))
    k = min(k_values)
    part_a = 1.983 - 0.983*np.exp(-23.14*Q)
    part_b = (k*np.pi**2 * E)/(12*(1-v**2))
    part_c = t_1**2/(L**2)
    return part_a * part_b * part_c

#print(find_stress_shell_buckling(1.6E6,200E9,0.56,0.001,0.28,0.04))