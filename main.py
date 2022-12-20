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

# TODO: state assumption that thickness is neglected when considering height constraint of tank
# TODO: state assumption that radius is same for spherical and cyl section

#TODO: take material parameters from materials_list.py
E = 200E9
sigma_y = 350E6
rho = 7750

def evaluate_mass(r,t,l,rho):
    # Returns (mass cylindrical shell, mass spherical endcaps x2)
    return (mass_calculation.cylindrical_shell(r,t,l,rho), 2*mass_calculation.semi_spherical_shell(r,t,rho))
def evaluate_tank_thickness(p,r,sigma_y):
    # Returns (thickness cylindrical shell, thickness spherical endcaps x2)
    return (pressure.find_min_thickness_cylinder(p,r,sigma_y), pressure.find_min_thickness_sphere(p,r,sigma_y))



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

    t = evaluate_tank_thickness(p=p, r=r_cyl, sigma_y=sigma_y)
    m = evaluate_mass(r=r_cyl,t=t[0],l=l_cyl,rho=rho)
    # IN -> p, r_cyl,
    # 1. Evaluate tank thickness for internal pressure and evaluate mass
    # OUT -> t_sphere, t_cyl, m_tank

    # IN -> m_attach, m_sc, m_tank, m_fuel
    # 2. Use masses to find loads.
    # OUT -> loads

    # IN -> loads + geometry
    # 3. Evaluate failure stress, and check if failure occurs. Update t_cyl until no failure.
    # (With a final t_cyl, check if t_sphere < t_cyl. If so, t_sphere = t_cyl)
    # OUT -> t_sphere and t_cyl

    # 4. Calculate mass of attachments, calculate mass of fuel tank, calculate total mass
    # OUT -> m_attach, m_tank, m_tot

    # 5. Repeat 2. - 4. with new m_attach, m_tank, m_tot

