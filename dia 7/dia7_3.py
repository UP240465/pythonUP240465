### Exercises: Level 3

#1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age = [22, 19, 24, 25, 26, 24, 25, 24]
ageset= set(age)
print('len age is: ', len(age))
print('len ageset is: ', len (ageset))
if len (age) > len(ageset):
    print('el mas largo es: ', len(age))
else:
    print('el mas largo es: ', len(ageset))

#1. Explain the difference between the following data types: string, list, tuple and set
#2. _I am a teacher and I love to inspire and teach people._ How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
