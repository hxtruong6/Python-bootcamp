from weakref import WeakKeyDictionary

class Positive:
    
    def __init__(self):
        self._instance_data =  WeakKeyDictionary()
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self._instance_data[instance]
    
    def __set__(self, instance, value):
        if value <=0 :
            raise ValueError("Value {} is not positive!".format(value))
        self._instance_data[instance] = value
    
    def __delete__(self, instance):
        raise AttributeError("Cannot delete the attribute.")
    
class Planet:
    def __init__(self, name, radius_metres, mass_kilograms, orbital_period_seconds, surface_temperature_kelvin):
        self.name = name
        self.radius_metres = radius_metres
        self.mass_kilograms = mass_kilograms
        self.orbital_period_seconds = orbital_period_seconds
        self.surface_temperature_kelvin = surface_temperature_kelvin
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Cannot set empty Planet.name")
        self._name = value
    
    radius_metres = Positive()
    mass_kilograms = Positive()
    orbital_period_seconds = Positive()
    surface_temperature_kelvin = Positive()

def main():
    mercury = Planet("Mercury", 
    radius_metres = 2439.7e3,
    mass_kilograms= 3.3e23,
    orbital_period_seconds= 7.6e6,
    surface_temperature_kelvin= 340)

if __name__ = '__main__':
    main()
