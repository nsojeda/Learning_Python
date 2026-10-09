print("Hello World")
# classic first program for all programs
# "print" is function that can display a programs output on the screen.
#  Strings are a data type used for words. they can identified by " " or ' '. The can all add a blank line between lines
print('Hello World')
print("")
print('')

# You may need to alternate "" and '' to use the other so python doesn't get confuse
print('Nick said "Python is fun"')
print("That's Nick's computer")

# \ or brake can stop python from thinking the string has ended.
print('That\'s Nick\'s computer')

# \ can also, brake a code line and let it continue on the next line.
print('A,\
B, \
and C')

# \n = line brake print to on the next lines or to add a space between lines.
print ('\n\nHello\nWorld')

print('\n\nHello \n')
print('World\n\n')

# variables are a way to store info or data to be used latter
name=("Nick")
hello=("Hello")
print (name)

# Concatenation
print ('\n\nConcatenation\n')
# The combining of strings/variables with a "+" or a ",".
# "+" will not put in a space between a strings/variables.
# "," will put a space between variables
print (hello + name)
print (hello,name)
print (hello + ", " + name)
print (name,"is the man")
print (name+" is the man\n\n")

# A number inside "[ ]" after a string variables will give you that letters.
print (name[1])
print("the fist letter in",name, "is",name[0])
print("")

# to get a range of letters. enter the number of the fist letter then a ":" and the number of the last letter plus 1
print (name[1:3])
print (hello[1:4])
print("")

# to find the length of a strings/variables, type "len()" entering a strings/variables
print (len(name))
print("")

# method work on an objected by uses a "."
# ".find(" ") to see if a strings/variables contains a string. what you are looking for.# if it contains what you are looking for you'll get a 0. if not you'll get -1
print (name.find("Nick"))
print (name.find("z"))
print (name.find("1"))
print ("z = zero".find("z"))
print ("1,2,3".find("1"))
print("")

print (name.lower())
print (name.upper())
print("")

print (name.count("Nick"))
print (name.count('Zero'))
print (name.count('i'))
print("")

print ("I am iron man")
print ("I am Tony")
print ("I am whoever I say I am")
print("")

print ("""1
2
3""")
print("")

print("4 \n" + "5 \n" + "6")
print('')

print('''7
8
9''')
print('')

print('''10 \
11 \
12''')