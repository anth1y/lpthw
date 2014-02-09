# Setting up variables 
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

# printing variables
print x
print y
# prining a variable inside of a variable
print "I said: %r." % x
print "I also said: '%s'." % y

# Setting up  more variables note the second variable has format char.
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
# printing the two variables one inside the other
print joke_evaluation % hilarious
# setting up variables
w = "This is the left side of..."
e = "a string with a right side."
# concatening variables
print w + e

