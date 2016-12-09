print "Welcome to Mad Libs! Tell me the story about your trip to Disney World!"

print "Enter a friend's name."
name = raw_input("> ")

print "Enter a number."
number = raw_input("> ")

print "Enter a type of vehicle."
vehicle = raw_input("> ")

print "Enter an adjective."
adjective = raw_input("> ")

print "Enter another adjective."
adjective2 = raw_input("> ")

print "Enter a verb that ends in 'ing'."
verb = raw_input("> ")

print "Enter an animal."
animal = raw_input("> ")

print "Enter an adjective."
adjective3 = raw_input("> ")

print "Enter a past tense verb."
verb2 = raw_input("> ")

print "Enter an adjective."
adjective4 = raw_input("> ")

print "Enter a wacky name."
wacky_name = raw_input("> ")

print "Enter an emotion."
verb3 = raw_input("> ")

print "Enter another past tense verb."
verb4 = raw_input("> ")

print "Enter a place."
place = raw_input("> ")

print "Just one more!"
print "Enter a verb."
verb5 = raw_input("> ")
 
print """
Last month, I went to Disney World with %s. We traveled for %s hours by %s.\n\nFinally, we got there and it was very %s. There were %s people %s everywhere. There were also people dressed up in %s costumes. \n\nI wish it had been more %s, but we %s anyway. We also went on some %s rides. One of them was called the %s ride. %s nearly fell off a ride and felt so %s. \n\n Later we went to the hotel and %s. Next year, I want to go to %s, where we can %s.""" % (name, number, vehicle, adjective, adjective2, verb, animal, adjective3, verb2, adjective4, wacky_name, name, verb3, verb4, place, verb5)