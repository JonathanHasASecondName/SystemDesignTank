import numpy as np

#INPUT TO FUNCTION IN SI UNITS
def find_penetration_depth_1layer(mass_p,velocity_p,density_micrometeoroid):
    t=0.7*((mass_p*10**3)**0.352)*((velocity_p*10**-3)**0.875)*((density_micrometeoroid*10**-3)**0.167)
    return t

#NASA keeps a database of the large debris objects that should be avoided during the
# mission, but most of the debris is of medium (1 mm-10 cm) or small scale (<1mm) and
# cannot be easily avoided or tracked.
# The approximate velocity of the orbital debris can be considered 8km/s.

#WORST CASE ORBITAL DEBRIS ----> 10cm , 8km/s (MASS?) (DENSITY?) IS THERE ORBITAL DEBRIS AROUND VENUS

#WORST CASE MicroMeteorioid ----> m=10^-4 g , 17km/s (MASS?) (DENSITY?) WORST CASE NICKEL 8900 kg/m^3
#https://www.science.org/doi/10.1126/science.262.5133.550

#print(find_penetration_depth_1layer(mass_p=2,velocity_p=8000,density_micrometeoroid=2700))


def find_bumper_thickness(projectile_diameter,bumper_density,density_micrometeoroid):
    t_bumper=0.25*projectile_diameter*density_micrometeoroid/bumper_density
    return t_bumper
def find_penetration_depth_2layer(mass_p,
                                  velocity_p,
                                  density_micrometeoroid,
                                  bumper_density,
                                  spacing,
                                  yield_stress):
    # FROM SI UNITS TO FUNKY FORMULA UNITS (SEE SOURCE)
    mass_p=mass_p*1000
    velocity_p = velocity_p*0.001
    density_micrometeoroid=density_micrometeoroid*0.001
    bumper_density=bumper_density*0.001
    spacing=spacing*100
    yield_stress=yield_stress*1.4038e-7
    print(yield_stress)

    t_rear_wall=0.055*(density_micrometeoroid*bumper_density)**(1/6)*mass_p**(1/3)*velocity_p/np.sqrt(spacing)*np.sqrt(70/yield_stress)
    return t_rear_wall

print(find_penetration_depth_2layer(mass_p=0.001,
                                 velocity_p=17000,
                                 density_micrometeoroid=1600,
                                 bumper_density=2700,
                                 spacing=0.05,
                                 yield_stress=276e6))
print(find_penetration_depth_1layer(
    mass_p=0.001,velocity_p=17000,density_micrometeoroid=1600
))
