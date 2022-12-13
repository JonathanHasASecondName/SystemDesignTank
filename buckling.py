import numpy

def find_cylinder_cross_section_area(r,t_1): #VALIDATED
    A=numpy.pi*r**2-numpy.pi*(r-t_1)**2
    return A
def find_cylinder_moment_of_inertia(r,t_1): #VALIDATED
    I=0.25*numpy.pi*(r**4-(r-t_1)**4)
    return I
def find_stress_column_buckling(A,L,I,E):
    column_buckling_critical_stress= numpy.pi**2*E*I/(A*L**2)
    return column_buckling_critical_stress

def find_stress_shell_buckling():
    pass


#print(find_cylinder_moment_of_inertia(1,0.01),find_cylinder_cross_section_area(1,0.01),find_stress_column_buckling(find_cylinder_cross_section_area(1,0.01),10,find_cylinder_moment_of_inertia(1,0.01),500*10**6))