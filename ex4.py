cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


#this line tells us how many cars are available
print "There are", cars, "cars available."
#this line tells us how many drivers are available
print "There are only", drivers, "drivers available."
#this line tells how many cars aren't driven
print "There will be", cars_not_driven, "empty cars today."
#this line tells us how many passengers we can move
print "We can transport", carpool_capacity, "people today."
#this line tells us how many passengers are waiting
print "We have", passengers, "to carpool today."
#this line tells us how many passengers we need to put in each car
print "We need to put about", average_passengers_per_car, "in each car"