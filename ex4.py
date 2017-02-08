
# number of cars
cars = 100
# number of spaces in a car
space_in_a_car = 4
# number of drivers available
drivers = 30
# number of total passengers
passengers = 90
# number of not driven cars
cars_not_driven = cars - drivers
# number of driven cars
cars_driven = drivers
# number of total carpool capacity
carpool_capacity = cars_driven * space_in_a_car
# average of passengers per each car
average_passengers_per_car = passengers/cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
