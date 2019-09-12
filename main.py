from car import Car, red, blue

my_car = Car('Nissan', 'Altima', red)
my_car.show_info()

your_car = Car('Honda', 'Accord', 'beautiful')
your_car.show_info()

another_car = Car('Chevy', 'Bolt')
another_car.show_info()

# Data Types: integer, float, string, boolean (true/false)
indoor_temp = 72
outdoor_temp = 94
best_ice_cream_flavor = 'chocolate'
print("integer:", indoor_temp, type(indoor_temp))
print("floating point:", indoor_temp / 10, type(indoor_temp / 8))
print("string:", best_ice_cream_flavor, type(best_ice_cream_flavor))
print("boolean:", indoor_temp == outdoor_temp, type(indoor_temp == outdoor_temp))
print("car:", my_car, type(my_car))
