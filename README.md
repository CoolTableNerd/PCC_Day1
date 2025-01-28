# Python Crash Course: Day 1

### Sunday January 26, 2025

I haven't practiced coding or python in....lets just say a long time. Today im starting out with remembering the basics - printing, user inputs, github commits - for a refresher.

I was shocked to see Repl.it rebranded to an ai coding website as that's where i used to go to practice my Python (that should tell you how long it's been), so im using trust worthy VS Code.

I am studying from Python Crash Course by Eric Matthes -- it's broken up in 2 parts (Basics and Projects) -- of course i'm starting with the basics, but i may skip over some topics like instillation, variables, data types as i still remain comfortable with those. 

I will commit every practice and program to my github for transparency, a metric to witness growth with the opportunity to re-visit to make the program better, more efficient and evidence of my abilities for employment purposes. 

thank you for joining me. 

# Chapter 2: Notes

for day 1 i jumped over Chapter 1 since that went over Python installation and i already have that running on my machine. 

Chapter 2 focused on working with variables, displaying strings, using string methods, organizing whitespace and numerical data. 

### Variables - boxes you store data in
variables was pretty much a refresher as im already aware of the do's and don'ts for using them. 
* no spaces (`full name = 'Daryl Corbin`)
* can't start variable with a number (`24KobeBryantTeam = 'Lakers'`)
* avoid using Python keywords (class, break, if, else etc) [full list here](https://www.w3schools.com/python/python_ref_keywords.asp)
* standard practice to start variable with a lowercase letter (`losAngeles`) 
* using camel case (`losAngeles`) where the start of the second word is capitalized or underscores (`los_angeles`) to breakup words for readability

### Strings - holds characters in a sequence 
anything inside quotes is considered a string. 
* strings can start with single quotations (`' '`) or double quotations (`" "`)
    - when using singles quotes, the compiler would throw an error with the use of an apostrophe inside. (`'that is Tom's coat'`) (error)
    - when using double quotes, the compiler would throw an error with the use of another set of double quotes (`"this morning Tom asked, "how's the coffee?"`) <br/>
[!TIP] 
use singular quotations when quoting something is necessary / use double quotations when using apostrophes are necessary (or a possibility)

### String Methods - allows text manipulation (line 21-23)
* methods are attached to the end of variables with parentheses
* Python returns a new string and doesn't change the value of the variable

some common methods:
nothing being included inside the parentheses:
* .title() - title case: makes the start of ever word capitalized. (Good Will Hunting)
* .uppercase() - capitalizes every letter (GOOD WILL HUNTING)
* .lowercase() - lowercase: makes all letters lowercase (good will hunting)
* .strip() - removes whitespace from left and the right of entry

methods that require data inside the parentheses: <br>
`.removeprefix('https://')` - removes the prefix if it exists at the start of the string.
* to clean up or modify strings by removing a specific beginning.
* to ensure that a string no longer starts with a particular substring.
* working with structured data like file paths, URLs, or identifiers where prefixes are common.<br/></br>
`.removesuffix(".txt")` -  removes the suffix if it exists at the end of the string. 
* to clean up or modify strings by removing a specific ending.
* to ensure that a string no longer ends with a particular substring.
* working with file extensions, URLs, or other structured data where suffixes are common.

[more string methods](https://www.w3schools.com/python/python_ref_string.asp)

### WhiteSpace - non printing characters (spaces/tabs/end-lines)
`\t` - tab character: indentation or spacing in strings. <br/>
`\n` - new line: creates a line break in strings, making the text continue on the next line.

### Numbers (lines 60-73)
* i skipped over integers because it's the basic addition/subtraction/multiplying and dividing, but i did go over floats and some math expressions again since they can get tricky when it complies and i want to make sure my logic remains sound all around. <br/>

Floats: numbers with a decimal point. decimal can appear in any position of the number. `0.1`
* when adding/dividing an integer with a float the result will always be a float `1 + 2.0 = 3.0`

Constants: variable where the value remains the same throughout the entire program. `MINIMUM_WAGE = 7.50`
* Python does not have constants built in, Python programmers use all caps to indicate a value should be treated as a constant


Python supports order or operation (PEMDAS) `(2+3)*5` | `2+3*4`

`**` - two asterisks represent exponents `3**2 = 9`
 
underscoring numbers can help with readability when creating a value `population = 8_000_000_000`
* Python only prints the digits in the compiler

multiple assignments can be assigned on one line: `x,y,z = 2,4,2`
* each variable and value needs to be separated by commas

# Reflections

It feels good getting back into the excitement of what programming can become once you lock down the fundamentals. Sill plenty of foundation to build, but i like where i stand. 
