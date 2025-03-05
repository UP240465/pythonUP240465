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
##12. Insert an IT company in the middle of the companies list
##13. Change one of the it_companies names to uppercase (IBM excluded!)
##14. Join the it_companies with a string '#;&nbsp; '
##15. Check if a certain company exists in the it_companies list.
##16. Sort the list using sort() method
##17. Reverse the list in descending order using reverse() method
##18. Slice out the first 3 companies from the list
##19. Slice out the last 3 companies from the list
##20. Slice out the middle IT company or companies from the list
##21. Remove the first IT company from the list
##22. Remove the middle IT company or companies from the list
##23. Remove the last IT company from the list
##24. Remove all IT companies from the list
##25. Destroy the IT companies list
##26. Join the following lists:
##27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
