from sys import argv

script, input_file = argv
# I create three functions with only one argument each that must be a file

def print_all(f):
    print f.read() # this read the file and print it all

def rewind(f):
    print f.seek(0) #  this allows to go to the start of the file
    
def print_a_line(line_count, f):
    print line_count, f.readline() # this takes a line in the file
    
current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines: "

# a = a + b can be written as a += b

current_line = 1
print_a_line(current_line, current_file) # current_line = 1

current_line += 1
print_a_line(current_line, current_file) # current_line = 2

current_line += 1
print_a_line(current_line, current_file)
