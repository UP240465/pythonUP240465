### Exercises: Level 3

  # 1. Here we have a person dictionary. Feel free to modify it!

#```py
    #    person={
    #'first_name': 'Asabeneh',
    #'last_name': 'Yetayeh',
    #'age': 250,
    #'country': 'Finland',
    #'is_marred': True,
    #'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    #'address': {
        #'street': 'Space street',
        #'zipcode': '02210'
   # }
   # }
#```

    # * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
    # * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
    # * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
    # * If the person is married and if he lives in Finland, print the information in the following format:

#```py
#    Asabeneh Yetayeh lives in Finland. He is married.
#```

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
print (person)
mskills=len(person.get('skills'))//2
print('the middle skills is', person['skills'][mskills])
print('the word python is in person', ('Python' in person['skills']))

frontdeveloper='JavaScript' and 'React' in person['skills']
backned_developer='Node', 'Python', 'MongoDB' in person ['skills']
fullstackdeveloper='React' and 'None' and 'MongoDB' in person ['skills']
unknown= 'unknown title'

if frontdeveloper==True and len(person['skills'])==2:
    print('He is a front end developer')
elif backned_developer==True:
    print('He is a backend developer')
elif fullstackdeveloper==True:
    print('He is a fullstack developer')
elif unknown==True:
    print('unknow title')

if person['is_marred']==True and person['country']=='Finland':
    print('Asabeneh Yetayeh lives in Finland. He is married')
else:
    print('it does not match')

print("revisado")