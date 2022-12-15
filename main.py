import numpy as np
import buckling
import pressure
import materials_list

# Tank parameters
r_cyl = 0.56
l_cyl = 0.04
A_cap = 1 # Aspect ratio for the endcap height-radius. 1 is spherical.
h_cap = r_cyl*A_cap
h_tot = l_cyl+(2*h_cap)
V_cyl = (np.pi*r_cyl**2)*l_cyl
V_cap = (1/6)*np.pi*h_cap*(3*r_cyl**2 + h_cap**2)




min_thickness = 0.0001
max_thickness = 0.01
thickness_step = 0.0001



