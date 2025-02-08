# Python Crash Course: Day 1

### Sunday January 26, 2025

I haven't practiced coding or python in....lets just say a long time. Today im starting out with remembering the basics - printing, user inputs, github commits - for a refresher.

I was shocked to see Repl.it rebrand to an ai coding website as that's where i used to go to practice my Python (that should tell you how long it's been), so im using trust worthy VS Code.

I am studying from Python Crash Course by Eric Matthes -- it's broken up in 2 parts (Basics and Projects) -- of course i'm starting with the basics, but i may skip over some topics like instillation, variables, data types as i still remain comfortable with those. 

I will commit every practice and program to my github for transparency, a metric to witness growth with the opportunity to re-visit to make the program better, more efficient and evidence of my abilities for employment purposes. 

thank you for joining me. 

# Chapter 2: Notes

### Organized Notes: Python Basics (Variables, Strings, Whitespace, Numbers)

---

#### **1. Variables**
- **Purpose**: Containers for storing data.
- **Naming Rules**:
  - No spaces (e.g., `full_name`, not `full name`).
  - Cannot start with numbers (e.g., `kobe24Team`, not `24KobeTeam`).
  - Avoid Python keywords (e.g., `list`, `class`, `if`).
- **Conventions**:
  - Use lowercase for variable names (e.g., `los_angeles`).
  - Camel case (`losAngeles`) or underscores (`los_angeles`) for readability.

---

#### **2. Strings**
- **Definition**: A sequence of characters enclosed in quotes (`' '` or `" "`).
- **Quotes Best Practices**:
  - Use double quotes for apostrophes: `"That's Tom's coat."`
  - Use single quotes for internal quotes: `'Tom asked, "How are you?"'`
- **String Methods**:
  - **Common Methods**:
    - `.title()`: `"good will hunting"` → `"Good Will Hunting"`
    - `.upper()`: `"hello"` → `"HELLO"`
    - `.lower()`: `"HELLO"` → `"hello"`
    - `.strip()`: Removes leading/trailing whitespace.
  - **Prefix/Suffix Removal**:
    - `.removeprefix("https://")`: `"https://google.com"` → `"google.com"`
    - `.removesuffix(".txt")`: `"report.txt"` → `"report"`.

---

#### **3. Whitespace**
- **Non-Printing Characters**:
  - `\t`: Adds a tab (e.g., `print("Name:\tDaryl")` → `Name:    Daryl`).
  - `\n`: Creates a new line (e.g., `print("Line 1\nLine 2")`).

---

#### **4. Numbers**
- **Floats**: Decimal numbers (e.g., `3.14`). Mixing integers/floats in operations results in floats.
- **Constants**: Use all caps (e.g., `TAX_RATE = 0.07`). Not enforced by Python but treated as convention.
- **Math Operations**:
  - Follows PEMDAS: `(2 + 3) * 4 = 20`.
  - Exponents: `3 ** 2 = 9`.
- **Readability**: Use underscores for large numbers (e.g., `population = 8_000_000_000`).
- **Multiple Assignments**: Assign values in one line (e.g., `x, y, z = 1, 2, 3`).

### Small Project: User Profile Generator (project.py)

#### **Objective**  
Create a program that collects user details and prints a formatted profile.

#### **Requirements**
1. Use variables to store:
   - Name (title case)
   - Age (integer)
   - Email (lowercase, strip whitespace)
   - Website URL (remove `"https://"` if present)
   - Salary (formatted with underscores, e.g., `50_000`).
2. Print the profile using `\t` and `\n` for readability.

#### **Steps**
1. Collect input for name, age, email, website, and salary.
2. Apply string methods to clean/format data.
3. Use constants for fixed values (e.g., `CURRENCY = "$"`).
4. Print the formatted profile.

# Reflections

It feels good getting back into the excitement of what programming can become once you lock down the fundamentals. Sill plenty of foundation to build, but i like where i stand. 
