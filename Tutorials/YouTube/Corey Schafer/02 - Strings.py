#  "by convention our variables are usually all lowercase"

message = "Hello World"

# "if it's multiple words then we separate those with underscore"
my_message = "Hello, Nick!"

# also these variable names should be as descriptive as possible. As to what values they're meant to hold so message is a good variable name here because it's holding our message

print(message)

print(my_message)

# print('Bobby's World!) SyntaxError: invalid syntax.
print('Bobby\'s World!')

print('Bobby\'s World!')

print("Bobby's World!")


# we needed to create a multi-line string and one way we can do this is by using three quotes at the beginning and end of our string and These can also be Single(''') or double(""") quotes

print("""Bobby's World 
was a popular animated television show 
that aired from 1990 to 1998. """)

#test  not in video but I wanted to see if I could do this and it worked.
print("""Bobby's World, \
was a popular animated television show\
that aired from 1990 to 1998. """)

print(len(message))
print(message[0])
print(message[10])
# print(message[11]) IndexError: string index out of range

print(message[0:5])

print(message[:5])
print(message[6:])

