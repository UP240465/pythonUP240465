### Exercises: Level 1

#1. Find the length of the set it_companies
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print (len(it_companies))

#2. Add 'Twitter' to it_companies
it_companies.add ('Twitter')
print (it_companies)

#3. Insert multiple IT companies at once to the set it_companies
it_companies.update ({'SAP', 'Telemex', 'Wipro', 'Alestra'})
print(it_companies)

#4. Remove one of the companies from the set it_companies
it_companies.remove ('Google')
print(it_companies)

#5. What is the difference between remove and discard
print ('El remove nos sirve paras eliminar un elemento pero si no se encuentra marca erros y el discard en cambio hace lo mismo pero no marca errores ')