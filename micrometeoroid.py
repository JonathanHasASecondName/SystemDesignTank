

#INPUT TO FUNCTION IN SI UNITS
def find_penetration_depth(mass_p,velocity_p,density_micrometeoroid):
    t=0.7*((mass_p*10**3)**0.352)*((velocity_p*10**-3)**0.875)*((density_micrometeoroid*10**-3)**0.167)
    return t

#NASA keeps a database of the large debris objects that should be avoided during the
# mission, but most of the debris is of medium (1 mm-10 cm) or small scale (<1mm) and
# cannot be easily avoided or tracked.
# The approximate velocity of the orbital debris can be considered 8km/s.

#WORST CASE ORBITAL DEBRIS ----> 10cm , 8km/s (MASS?) (DENSITY?) IS THERE ORBITAL DEBRIS AROUND VENUS

#WORST CASE MicroMeteorioid ----> m=10^-4 g , 17km/s (MASS?) (DENSITY?) WORST CASE NICKEL 8900 kg/m^3
#https://www.science.org/doi/10.1126/science.262.5133.550

print(find_penetration_depth(10**-7,17000,8900))