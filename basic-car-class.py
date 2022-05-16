import random

class Car:
    def __init__(self, fabricant, brand, year, engine, fuel):
        self._fabricant = fabricant
        self._brand = brand
        self._year = str(year)
        self._engine = engine
        self._fuel = fuel
    def carMilage(self):
        self._milage = str(random.randrange(10000, 100000))
    def carPaint(self):
        self._color = random.choice(['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'black', 'white', 'silver', 'cow print'])
    def toString(self):
        state = "\n\tFabricant: " + self._fabricant + "\n\tBrand: " + self._brand + "\n\tYear: " + self._year + "\n\tEngine: " + self._engine + "\n\tFuel: " + self._fuel + "\n\tColor: " + self._color + "\n\tMilage: " + self._milage
        return state

def main():
    myCurrentCar = Car("Civic", "honda", 2009, "regular type", "87 regular")
    myCurrentCar.carPaint()
    myCurrentCar.carMilage()
    print("Here is my current car: " + myCurrentCar.toString())

    myRealisticDreamCar = Car("hatchback", "Volvo", 2023, "regular type", "87 regular")
    myRealisticDreamCar.carPaint()
    myRealisticDreamCar.carMilage()
    print("Here is my realistic dream car: " + myRealisticDreamCar.toString())

    myDreamCar = Car("Model Y", "Tesla", 2033, "regular type", "electric")
    myDreamCar.carPaint()
    myDreamCar.carMilage()
    print("Here is my dream car: " + myDreamCar.toString())

main()
