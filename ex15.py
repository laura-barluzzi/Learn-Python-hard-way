from sys import argv 

# you need a file .txt to open
script, filename = argv 

#open file
txt = open(filename) 

# here we state the name of the file which was typed already in the argument of the command line
print "Here's your file %r:" % filename
 
# print the whole text in the txt file opened
print txt.read() 

"""print "Type the filename again:" 
file_again = raw_input("> ")"""

# study drill 5:
file_again = raw_input("Type the filename again \n") 

# open file again - it is possible to open multiple times
txt_again = open(file_again)

# close opened file
txt.close()
txt_again.close()
