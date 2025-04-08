### Exercises: Level 3

#1. Write a function called is_prime, which checks if a number is prime.
def is_prime (number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5)+ 1):
        if number % i == 0:
            return False
    return True
print("¿El numero 5 es primo?", is_prime (5))


#1. Write a functions which checks if all items are unique in the list.
def all_unique_items (lista):
    all_unique = len (lista) == len(set(lista))
    return all_unique
print("¿Todos los elementos son unicos en la lista?", all_unique_items([1,2,3,4,5]))

#1. Write a function which checks if all the items of the list are of the same data type.
def same_data_type (lista):
    same_type = all(isinstance(lista[0],type(item))for item in lista)
    return same_type
print("¿Todos los elementos de la lista son del mismo tipo?",same_data_type([1,2,3,4,5]))

#1. Write a function which check if provided variable is a valid python variable
def is_python_variable (variable):
    if variable.isidentifier():
        return True
    else:
        return False
print("¿la variable proporcionada es una variable de python valida?", is_python_variable('formula-1'))

#1. Go to the data folder and access the countries-data.py file.
from paisdata import paises
def the_most_spoken_languages():
    countrylanguage = []
    for pais in paises:
        for language in pais['languages']:
            countrylanguage.append (language )
            ordenatedlanguage=set(countrylanguage)
    dictionary_languages= {

    }
    for language in ordenatedlanguage:
        dictionary_languages[language]=0
    for idiom in dictionary_languages:
        for pais in paises:
            if idiom in pais['languages']:
                dictionary_languages[idiom]=pais['population'] + dictionary_languages[idiom]
                sortedthingspopulation = sorted(dictionary_languages.values(), reverse=True)
                sorfkeyslanguagespopulation = sorted(dictionary_languages, key= dictionary_languages.get, reverse=True)
    for i in range(0,21):
        
        print(i+1, sorfkeyslanguagespopulation[i] , sortedthingspopulation[i])
    return
print(the_most_spoken_languages())

from paisdata import paises

def the_most_populous_countries():
    country_population = {}
    for pais in paises:
        country_population[pais['name']] = pais['population']
    sorted_population = sorted(country_population.items(), key=lambda item: item[1], reverse=True)#queremos ordenar la population NO EL PAIS, lamda es una funcio compacta como def 
    for i in range(0,20):
        print(i+1,  sorted_population[i])
    return
    
the_most_populous_countries()

print("revisado")