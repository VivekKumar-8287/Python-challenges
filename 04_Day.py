# print("why are you sad!")
    
# letter = 'P'
# print(len(letter))


# Strings  and numbers
""" radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a circle with a radius {} is {:.2f}.'.format(radius, area) # 2 digits after decimal
print(formated_string)
 """

""" a = 4
b = 3
print(f'{a} + {b} = {a +b}') """

# Reverse a string
# greeting = "Hello, World!"
# print(greeting[::-1])

# Skipping Character
"""
 language = "Pythonisgreat"
pto = language[0:15:2]
print(pto) """

# challenge = 'thirty days of python'
# print(challenge.capitalize())
# print(challenge.count("t"))
# print(challenge.endswith("hon"))
challenge2 = 'thirty\tdays\tof\tpython'
# print(challenge.expandtabs())

# print(challenge.find('d'))
# print(challenge.rfind('y'))
""" 
first_name = 'Vivek'
last_name = 'kumar'
age = 250
sentence = 'I am {}. I am {}. I am {} years old.'
print(sentence.format(first_name,last_name,age)) """

""" 
radius = 10
pi = 3.14
area = pi * radius ** 2
result = 'The area of a circle with radius {} is {}'.format(str(radius), str(area))
print(result) """

challenge = 'thirty days of python'
sub_string = 'da'
# print(challenge.index(sub_string))
# print(challenge.index(sub_string,9))

# print(challenge.rindex(sub_string))

# isalnum(): Checks alphanumeric character
# isalpha(): Checks if all string elements are alphabet characters (a-z and A-Z)
# isdecimal(): Checks if all characters in a string are decimal (0-9)
decimal = "123"
# print(decimal.isdecimal())
# isdigit(): Checks if all characters in a string are numbers (0-9 and some other unicode characters for numbers)
# isnumeric(): Checks if all characters in a string are numbers or number related (just like isdigit(), just accepts more symbols, like ½)
num = '\u00BD'
# print(num.isnumeric())

# isidentifier(): Checks for a valid identifier - it checks if a string is a valid variable name

# islower(): Checks if all alphabet characters in the string are lowercase

# isupper(): Checks if all alphabet characters in the string are uppercase

# join(): Returns a concatenated string

# strip(): Removes all given characters starting from the beginning and end of the string

# replace(): Replaces substring with a given string

# split(): Splits the string, using given string or space as a separator

# title(): Returns a title cased string

# swapcase(): Converts all uppercase characters to lowercase and all lowercase characters to uppercase characters

# startswith(): Checks if String Starts with the Specified String
""" 
firt_word = 'Thirty'
second_word = 'Days'
third_word = 'of'
fourth_word = 'python'
print(firt_word +" "+ second_word+" " + third_word +" "+ fourth_word) """

# company = 'Coding For All'
# print(company)
# print(len(company))
# print(company.upper())
# print(company.lower())
# print(company.capitalize())
# print(company.title())
# print(company.swapcase())

# print(company[:6])

# print(company.index('Coding'))
# print(company.find('Coding'))
# print(company.replace("Coding For All","Python"))

# print(company.split())

company = 'Coding For All'
# print(company.index('C'))
# print(company.rindex('C'))
# print(company.index('F'))

sentence = 'You cannot end a sentence with because because because is a conjunction'
# print(sentence.find('because'))
# print(sentence.index('because'))

# print(sentence.rindex('because'))

# print(sentence[31:54])

# print(company.startswith('Coding'))
# print(company.endswith('coding'))

company2 = '   Coding For All      '
# print(company2)
# print(company.strip())

# sentence1 = '30DaysOfPython'  
# sentence2 =  'thirty_days_of_python'   
# print(sentence1.isidentifier())
# print(sentence2.isidentifier())

# python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
# final = '-'.join(python_libraries)
# print(final)

# sentence1 = "I am enjoying \nthis challenge."

# sentence2 = "I just wonder what \nis next."
# print(sentence1)
# print(sentence2)

row1 = 'Name\t\tAge\tCountry\tCity'
row2 = 'Asabeneh\t250\tFinland\tHelsinki'

print(row1)
print(row2)