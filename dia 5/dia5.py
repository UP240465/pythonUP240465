##1. Declare an empty list
empity_list =list ()
print (empity_list)

##2. Declare a list with more than 5 items
jugadores= ['messi', 'lamine', 'neymar', 'pedri', 'santi']
print(jugadores)

##3. Find the length of your list
print (len(jugadores))

##4. Get the first item, the middle item and the last item of the list
print (jugadores[0])
print(jugadores [len(jugadores)//2])
print(jugadores[-1])

##5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types=('Juan Pablo', '19', '1.76', 'single', 'San Juan'.split(','))
print (mixed_data_types)

##6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ('Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon' .split(','))

##7. Print the list using _print()_
print (it_companies)

##8. Print the number of companies in the list
print(len(it_companies))

##9. Print the first, middle and last company
first_company=(it_companies[0])
middle_company=(it_companies[3])
last_company=(it_companies[-1])
print('''
      first company of the list{}
      middle company of the list{}
      last company of the lis {}
      '''.format(first_company, middle_company, last_company))

##10. Print the list after modifying one of the companies
del it_companies[4]
print (it_companies)

##11. Add an IT company to it_companies
it_companies.append ('Tesla')
print(it_companies)

##12. Insert an IT company in the middle of the companies list
getmid = len(it_companies)//2
it_companies.insert(getmid, 'Intel')
print (it_companies)

##13. Change one of the it_companies names to uppercase (IBM excluded!)
del it_companies[0]
it_companies.insert (0, "FACEBOOK")
print (it_companies)

##14. Join the it_companies with a string '#;&nbsp; '
it_companies.append ('#;')
print(it_companies)

##15. Check if a certain company exists in the it_companies list.
checar= 'Tesla' in it_companies
print ('La empresa esta en la lista? :', checar)

##16. Sort the list using sort() method
print(sorted(it_companies))

##17. Reverse the list in descending order using reverse() method
print(sorted(it_companies, reverse=True))

##18. Slice out the first 3 companies from the list
print(it_companies[0:3])

##19. Slice out the last 3 companies from the list
print(it_companies[-4:-1])

##20. Slice out the middle IT company or companies from the list
m= int(len(it_companies)/2)
print ('Empresa que esta en el medio es: ',it_companies[m])

##21. Remove the first IT company from the list
empresa= str (it_companies[0])
print(it_companies)

##22. Remove the middle IT company or companies from the list
it_companies.remove (str(it_companies[m]))
print(it_companies)

##23. Remove the last IT company from the list
it_companies.remove(str(it_companies[-2]))
print(it_companies)

##24. Remove all IT companies from the list
it_companies.clear()
print(it_companies)

##25. Destroy the IT companies list
del it_companies

##26. Join the following lists:
front_end=['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end=['Node', 'Express', 'MongoDB']
integrar = front_end + back_end
print(integrar)

##27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack = integrar
(full_stack.index ('Redux'))
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print (full_stack)

