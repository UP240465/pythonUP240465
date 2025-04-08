#1. Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_and_zero=[i for i in numbers if i<=0]
print(negative_and_zero)

#2. Flatten the following list of lists of lists to a one dimensional list :
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flatten_list=[number for i in list_of_lists for a in i for number in a]
print(flatten_list)

#3. Using list comprehension create the following list of tuples:
'''[(0, 1, 0, 0, 0, 0, 0),
(1, 1, 1, 1, 1, 1, 1),
(2, 1, 2, 4, 8, 16, 32),
(3, 1, 3, 9, 27, 81, 243),
(4, 1, 4, 16, 64, 256, 1024),
(5, 1, 5, 25, 125, 625, 3125),
(6, 1, 6, 36, 216, 1296, 7776),
(7, 1, 7, 49, 343, 2401, 16807),
(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),
(10, 1, 10, 100, 1000, 10000, 100000)]'''

result = [(n, 1, n, n**2, n**3, n**4, n**5) for n in range(11)]
for item in result:
    print(item)

#4. Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
list =  [[country.upper(),country[:3].upper(), city.upper()] for sublist in countries for country, city in sublist]
print(list)

#5. Change the following list to a list of dictionaries:
countries_dict = [{'country':country.upper(), 'city':city.upper()} for [(country, city)] in countries]
print(countries_dict)

#6. Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
list_name_c=[[name + ' ' + last_name] for [(name,last_name)] in names]
print(list_name_c)

#7. Write a lambda function which can solve a slope or y-intercept of linear functions.
slope= lambda x1,y1,x2,y2: (y2 - y1)/(x2 - x1)
print("La pendiente es de: ", slope(1,2,3,6))
y_intercept = lambda x,y,m: y - m * x
print("La intercepcion en Y es en: ", y_intercept(1,2,2))

print("revisado")