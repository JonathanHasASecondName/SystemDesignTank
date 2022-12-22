import numpy as np
import buckling
import mass_calculation
import pressure

import Mass_of_attachments

# Tank parameters
p = 1620000
r_cyl = 0.56
l_cyl = 100 #0.04
A_cap = 1 # Aspect ratio for the endcap height-radius. 1 is spherical.
h_cap = r_cyl*A_cap
h_tot = l_cyl+(2*h_cap)
V_cyl = (np.pi*r_cyl**2)*l_cyl
V_cap = (1/6)*np.pi*h_cap*(3*r_cyl**2 + h_cap**2)
V_tot = V_cyl + 2*V_cap
V_req = 0.747

materials = [['Ti6AI4V STA', 4500, 828000000, 760000000, 0.342, 110000000000],
             ['Al 2024', 2780, 324000000, 283000000, 0.33, 73100000000],
             ['Fe 4130', 7850, 435000000, 427500000, 0.29, 205000000000],
             ['Carbon Fibre', 1600, 600000000, 90000000, 0.77, 70000000000]]
# [material_name,material_density,material_axial_stress,material_shear_stress,material_poisson_ratio,young_modulus]
material = materials[0]
v = material[4]
E = material[5]
sigma_y = material[2]
rho = material[1]

#Original Mass values
m_fuel = 888.4
m_sc = 425.1-31.7 #VALUES FROM WP2 NOT INCLUDING ORIGINAL PREDICTED MASS OF FUEL TANK

# Launch G-Forces MUST CHANGE IF SPACECRAFT IS HEAVIER THAN 1814 kg
g_axial = 4
g_lateral = 1.5

#DEFAULT M_ATTACH FOR FIRST ITERATION
m_attach=0

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

    # IN -> p, r_cyl,
    # 1. Evaluate tank thickness for internal pressure and evaluate mass
    # OUT -> t_sphere, t_cyl, m_tank

    #CODE FOR STEP 1

    t_sphere = pressure.find_min_thickness_sphere(p=p,r=r_cyl,sigma_y=sigma_y)
    t_cyl = pressure.find_min_thickness_cylinder(p=p,r=r_cyl,sigma_y=sigma_y)

    m_tank= mass_calculation.cylindrical_shell(r=r_cyl,t=t_cyl,l=l_cyl,rho=rho)\
            +2*mass_calculation.semi_spherical_shell(r=r_cyl,t=t_sphere,rho=rho)

    # IN -> m_attach, m_sc, m_tank, m_fuel
    # 2. Use masses to find loads.
    # OUT -> loads

    #CODE FOR STEP 2
    m_prev = None
    for count in range(0,100):
       print(f"Running iteration {count}")
       load_axial = (m_attach+m_sc+m_tank+m_fuel)*9.81*g_axial
       load_lateral = (m_attach+m_sc+m_tank+m_fuel)*9.81*g_lateral

       # IN -> loads + geometry
       # 3. Evaluate failure stress, and check if failure occurs. Update t_cyl until no failure.
       # (With a final t_cyl, check if t_sphere < t_cyl. If so, t_sphere = t_cyl)
       # OUT -> t_sphere and t_cyl

       #CODE FOR STEP 3


       A=buckling.find_sectional_area_cylindrical_shell(r=r_cyl,t=t_cyl)
       I=buckling.find_cylinder_moment_of_inertia(r=r_cyl,t_1=t_cyl)
       axial_stress = buckling.find_axial_stress(F_axial=load_axial,A=A)

       column_buckling_critical_stress = buckling.find_stress_euler_column_buckling(A=A,L=h_tot,I=I,E=E)
       shell_buckling_critical_stress = buckling.find_stress_shell_buckling(p=p,E=E,r=r_cyl,t_1=t_cyl,v=v,L=h_tot)

       while axial_stress>column_buckling_critical_stress or axial_stress>shell_buckling_critical_stress:
           t_cyl=t_cyl*1.01

           A = buckling.find_sectional_area_cylindrical_shell(r=r_cyl, t=t_cyl)
           I = buckling.find_cylinder_moment_of_inertia(r=r_cyl, t_1=t_cyl)
           axial_stress = buckling.find_axial_stress(F_axial=load_axial, A=A)

           column_buckling_critical_stress = buckling.find_stress_euler_column_buckling(A=A, L=h_tot, I=I,
                                                                                        E=E)
           shell_buckling_critical_stress = buckling.find_stress_shell_buckling(p=p, E=E, r=r_cyl, t_1=t_cyl, v=v,
                                                                                L=h_tot)
           print("I am iterating")
           if t_cyl>t_sphere:
               t_sphere=t_cyl

       m_tank = mass_calculation.cylindrical_shell(r=r_cyl, t=t_cyl, l=l_cyl, rho=rho) \
                + 2 * mass_calculation.semi_spherical_shell(r=r_cyl, t=t_sphere, rho=rho)
       # IN m_tank, m_tot
       # 4. Calculate mass of attachments, calculate mass of fuel tank, calculate total mass
       # OUT -> m_attach, m_tot

       m_attach = Mass_of_attachments.configuration_loop(height_curtain=1,mass_tank_structure=m_tank,mass_fuel=m_fuel,radius_curtain=0.56)[2]

       m_tot=m_attach+m_tank+m_fuel+m_sc

       print(f'''Total SC Mass = {m_tot}
Mass Tank = {m_tank}
Mass Attachment = {m_attach}
Cylinder Thickness = {t_cyl}
Spherical Thickness = {t_sphere}
       ''')
       if m_prev == m_tot:
           break
       else:
           m_prev = m_tot
    

    # 5. Repeat 2. - 4. with new m_attach, m_tank, m_tot

print(f'''\n-----------------------
Total SC Mass = {m_tot}
Mass Tank = {m_tank}
Mass Attachment = {m_attach}
Cylinder Thickness = {t_cyl}
Spherical Thickness = {t_sphere}
-----------------------''')
