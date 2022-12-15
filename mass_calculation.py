import numpy as np
def semi_spherical_shell(r,t,rho):
    V = (4/3)*np.pi*(r**3) - (4/3)*np.pi*((r-t)**3)
    return rho*V

def cylindrical_shell(r,t,l,rho):
    V = l*(np.pi*(r**2) - np.pi*((r-t)**2))
    return rho*V
