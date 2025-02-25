# Problem 2: Space Encyclopedia
# Given a dictionary planets that maps planet names to a dictionary containing the 
# planet's number of moons and orbital period, write a function planet_lookup() that 
# accepts a string planet_name and returns a string in the form Planet <planet_name> 
# has an orbital period of <orbital period> Earth days and has <number of moons> moons. 
# If planet_name is not a key in planets, return "Sorry, I have no data on that planet.".

def planet_lookup(planet_name):
    message = "Sorry, I have no data on that planet."
    
    planetary_info = {
    "Mercury": {
        "Moons": 0,
        "Orbital Period": 88
    },
    "Earth": {
        "Moons": 1,
        "Orbital Period": 365.25
    },
    "Mars": {
        "Moons": 2,
        "Orbital Period": 687
    },
    "Jupiter": {
        "Moons": 79,
        "Orbital Period": 10592
    }
    }
    
    planet_info = planetary_info.get(planet_name, None)
    
    if planet_info:
        return f'Planet {planet_name} has an orbital period of {planet_info["Orbital Period"]} Earth days and has {planet_info["Moons"]} moons.'
    
    return message


print(planet_lookup("Jupiter"))
print(planet_lookup("Pluto"))