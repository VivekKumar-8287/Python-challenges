# Dictionaries

# dct = {'key1':'value1','key2':'value2','key3':'value3','key4':'value4'}
# print(len(dct))

# print(dct['key1'])

person = {
    'first_name':'Vivek',
    'last_name':'Kumar',
    'age':250,
    'country':'India',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'state':'Haryana',
        'zipcode':'122001'
    }
    }

# print(person['first_name'])
# print(person['address']['state'])

# print(person.get('country'))

# person['job_title']='Unemployed'
# person['skills'].append('HTML')
# print(person)

# person['age'] = 125
# print(person)
""" 
dct = {'key1':'value1','key2':'value2','key3':'value3','key4':'value4'}
print('key1' in dct)
# print('value3' in dct)
 """

""" 
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.pop('key1') # removes key1 item
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.popitem() # removes the last item
del dct['key2'] # removes key2 item
 """

""" 
The items() method changes dictionary to a list of tuples.
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items()) # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])
 """

# print(dct.clear()) # None

# We can copy a dictionary using a copy() method. Using copy we can avoid mutation of the original dictionary.

# The keys() method gives us all the keys of a a dictionary as a list.

# The values method gives us all the values of a a dictionary as a list.

dog = {}
# print(type(dog))

dog['name'] = 'DOG'
# print(dog)

student = {
    'first_name':'Ashoka',
    'last name' :'Pathak',
    'gender':'male',
    'age':28,
    'marital_status':'unmarried',
    'skills':['JS','Python','Rust','C++'],
    'country':'india'
}

# print(len(student))
# print(student['skills'])
# print(type(student['skills']))

# student['skills'].append('HTML')
# print(student['skills'])

# print(student.keys())
# print(student.values())

studentList = student.items()

# print(studentList)

# del student['marital_status']
del student
print(student)