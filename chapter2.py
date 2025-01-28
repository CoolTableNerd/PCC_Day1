message = "Hello World"
print(message)

# 2-1: Assign a message to a variable, and then print that message.
nfc_championship24 = "Commanders vs Eagles"
print(nfc_championship24)

# 2-2: Assign a message to a variable, and print that message. Then change the value of the variable to a new message, and print the new message.
currentScore = "14-3 Eagles"
print(currentScore)

currentScore = "14-12 Eagles"
print(currentScore)

# 2-3:  Use a variable to represent a person’s name, and print a message to that person. Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”
name = 'Diego'
print(f"greetings, {name}! let's learn Python today!")

#2-4: Use a variable to represent a person’s name, and then print that person’s name in lowercase, uppercase, and title case.
name = 'Daryl'
print(name.lower())
print(name.upper())
print(name.title())

#2-5: Find a quote from a famous person you admire. Print the quote and the name of its author.
print(f'During a press conference, Jalen Hurts once said "keep the main thing the main thing')

#2-6: Repeat Exercise 2-5, but this time, represent the famous person’s name using a variable called famous_person. Then compose your message and represent it with a new variable called message. Print your message.
speaker = "Jalen Hurts"
message = "keep the main thing the main thing"
print(f'During a press conference, {speaker} once said, {message}')

'''
2-7: 
Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name. Make sure you use each character combination, "\t" and "\n", at least once.
Print the name once, so the whitespace around the name is displayed. Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().

'''

cousin = '\t Demetrius \n'
print(cousin)
print(cousin.lstrip())
print(cousin.rstrip())
print(cousin.strip())

'''
2-8: Python has a removesuffix() method that works exactly like removeprefix(). 
Assign the value 'python_notes.txt' to a variable called filename. 
Then use the removesuffix() method to display the filename without the file extension, like some file browsers do.

'''
filename = 'python_notes.txt'
print(filename.removesuffix)

'''
2-9: Write addition, subtraction, multiplication, and division operations that each result in the number 8. 
Be sure to enclose your operations in print() calls to see the results.

'''
print(5+3)
print(10-2)
print(4*2)
print(16/2)

'''
2-10. Favorite Number: Use a variable to represent your favorite number. 
Then, using that variable, create a message that reveals your favorite number. 
Print that message.

'''

favoriteNumber = 4
print(f'{favoriteNumber} is my favorite number.')