import numpy as np
import buckling
import mass_calculation
import pressure
import materials_list

# Tank parameters
p = 1620000
r_cyl = 0.56
l_cyl = 0.04
A_cap = 1 # Aspect ratio for the endcap height-radius. 1 is spherical.
h_cap = r_cyl*A_cap
h_tot = l_cyl+(2*h_cap)
V_cyl = (np.pi*r_cyl**2)*l_cyl
V_cap = (1/6)*np.pi*h_cap*(3*r_cyl**2 + h_cap**2)
V_tot = V_cyl + 2*V_cap
V_req = 0.747

#TODO: take material parameters from materials_list.py
E = 200E9
sigma_y = 350E6
rho = 7750

def evaluate_mass(r,t,l,rho):
    return mass_calculation.semi_spherical_shell(r,t,rho) + mass_calculation.cylindrical_shell(r,t,l,rho)
def evaluate_bulkhead():
    t_min_bulkhead = pressure.find_min_thickness_hoop_stress(p=p,r=r_cyl,sigma_y=sigma_y)


if __name__ in '__main__':
    print(f'''----TANK PARAMETERS----
    r_cyl = {r_cyl}
    l_cyl = {l_cyl}
    A_cap = {A_cap}
    h_cap = {h_cap}
    h_tot = {h_tot}
    V_cyl = {V_cyl}
    V_cap = {V_cap}
    V_tot = {V_tot}
    V_req = {V_req}
    -----------------------''')


