'''
Python Tutorial for Beginners 2: Strings - Working with Textual Data a video by Corey Schafer on YouTube.
This is more of a scratchpad of snippets from the video.
See 02-Strings.md for my notes.
'''
hr = "----------------------"

print(hr)
print('Variable Naming Conventions')
print(hr)

# "by convention our variables are usually all lowercase"

message = "Hello World"

# "if it's multiple words then we separate those with underscore"
my_message = "Hello, Nick!"

# also these variable names should be as descriptive as possible. As to what values they're meant to hold so message is a good variable name here because it's holding our message

print(message)

print(my_message)


print(hr)
print('String Quotes and Escaping')
print(hr)


# print('Bobby's World!) SyntaxError: invalid syntax.
print('Bobby\'s World!')

# test  not in video but I wanted to see if I could do this and it worked.
print("He said, \"Hello World\" ")

print("Bobby's World!")

# test  not in video but I wanted to see if I could do this and it worked.
print("That's Nick's computer")
print('Nick said, "Python is fun"')


# we needed to create a multi-line string and one way we can do this is by using three quotes at the beginning and end of our string and These can also be Single(''') or double(""") quotes

print("""Bobby's World 
was a popular animated television show 
that aired from 1990 to 1998. """)

# test  not in video but I wanted to see if I could do this and it worked.
print("""
1,
2,
3,
""")

print('''Bobby's World, \
was a popular animated television show\
that aired from 1990 to 1998. ''')

print("""
1,\
2,\
3,
""")

print(hr)
print('String Length and Indexing')
print(hr)

print(len(message))
print(message[0])
print(message[10])
# print(message[11]) IndexError: string index out of range

print(message[0:5])

print(message[:5])
print(message[6:])

print(message.lower())
print(message.upper())

print(message.count('Hello'))
print(message.count('l'))


print(message)
print(message.find('World'))

print(message.find('Universe'))


# test  not in video but I wanted to see if I could do this and it worked.
new_message = message.replace('World', 'Universe')

print(message.replace('World', 'Universe'))

print(new_message)

greeting = "Hello"
name = "Michael"

greeting_message = greeting + ", " + name
print (greeting)
print (name)
print (greeting_message)
print (greeting + ", " + name)
print (greeting + ", " + name + ". Welcome!")

format_greeting = "{}, {}. Welcome!".format(greeting, name)
print(format_greeting)

f_string_greeting = f"{greeting}, {name}. Welcome!"
print(f_string_greeting)

print(f"{greeting}, {name.upper()}. Welcome!")



print(dir(name))

print(help(str))

print(help(str.lower))