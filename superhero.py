# base class
class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        # power is protected and shouldn't be accessed directly outside the class (encapsulation)
        self._power = power
        self.city = city 

        #an introduce method to print superhero's name and city
    def introduce(self):
        print (f"My name is {self.name}, protector of {self.city}")

        #a use_power method to show the superhero is using their power
    def use_power(self):
        print(f"{self.name} uses their special power which is {self._power}")



        #encapsulation, getter and setter
    def get_power(self):
        return self._power
    
    def set_power(self, new_power):
        print(f"{self.name}'s power has changed to {new_power}")


        #subclass called FlyingSuperhero. It inherits all attributes and methods from Superhero class
class FlyingSuperhero(Superhero):

        #subclass constructor with an additional attribute flyin_speed
    def __init__(self, name, power, city, flying_speed):
        super().__init__(name, power,city)
        self.flying_speed = flying_speed


        #overriding the use_power method
    def use_power(self):
        print(f"{self.name} soars through the sky at {self.flying_speed}km/h and unleashes {self._power}!")

        #adding a unique method
    def fly(self):
        print(f"{self.name} is flying over {self.city} at {self.flying_speed}km/h!")

        #creating and using an object from the base class
    hero1 = Superhero("Superman", "Superspeed", "Africa")
        #creating and using an object from the subclass
    hero2 = Superhero("Shadow Ninja", "Invisibility", "Neo-Tokyo")

    hero1.introduce()
    hero1.use_power()

