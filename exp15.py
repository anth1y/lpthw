# using the sys module and the argv fucntion
from sys import argv
# the arguments that argv will be taking
script, filename = argv
# setting the variable txt to use the "open" function to open the variable "filename"
txt = open(filename)
# Using the print function printing out the filename variable
print "Here's your file %r" % filename
# printing out the variable "txt" and using the read function to read the text file contents.
print txt.read()
# print statement to stdout
print "Type the filename again:"
#setting up the variable to store input of the filename from the user
file_again = raw_input("> ")
# using the open function to open the previous variable.
txt_again = open(file_again)
#using the print function to print out the variable and read it to stdout.
print txt_again.read()
txt_again.close()
txt.close()
