#1. Create  an empty dictionary called dog
dog= {}

#2. Add name, color, breed, legs, age to the dog dictionary
dog= {'Scot', 'Blanco', 'Labrador', 'cuatro patas', '9 de edad' }
print(dog)

#3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
person = {
    'first_name':'Juan Pablo',
    'last_name':'Muñoz de la torre',
    'age':19,
    'country':'mexico',
    'is_marred':False,
    'skills':['Inteligente', 'Estudioso', 'Responsable', 'Feliz', 'Python'],
    'address':{
        'street':'Av Juarez',
        'zipcode':'47010'
    }
    }
print(person)
#4. Get the length of the student dictionary
print(len(person))

#5. Get the value of skills and check the data type, it should be a list
print(person['skills'])
print(type(person['skills']))

#6. Modify the skills values by adding one or two skills
person['skills'].append ('Python')
print(person['skills'])

#7. Get the dictionary keys as a list
print(list(person.keys()))

#8. Get the dictionary values as a list
print(list(person.values()))

#9. Change the dictionary to a list of tuples using _items()_ method
print(tuple(person.items()))

#10. Delete one of the items in the dictionary
del(person['skills'])
print(person)

#11. Delete one of the dictionaries
del dog