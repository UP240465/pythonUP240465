##1.Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
print ( 'thirty' ' days' ' of' ' python')

##2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
print ('coding' ' for' ' all')

##3. Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

##4. Print the variable company using _print()_.
print(company)

##5. Print the length of the company string using _len()_ method and _print()_.
len_compamy=len(company)
print(len_compamy)

##6. Change all the characters to uppercase letters using _upper()_ method.
print(company.upper())

##7. Change all the characters to lowercase letters using _lower()_ method.
print(company.lower())

##8. Use capitalize(), title(), swapcase() methods to format the value of the string _Coding For All_.
print(company.capitalize())
print(company.title())
print(company.swapcase())

##9. Cut(slice) out the first word of _Coding For All_ string.
print(company[0:6])

##10. Check if _Coding For All_ string contains a word Coding using the method index, find or other methods.
print(company.index("Coding"))

##11. Replace the word coding in the string 'Coding For All' to Python.
print(company.replace("Coding", "Python"))

##12. Change Python for Everyone to Python for All using the replace method or other methods.
com="Python for Everyone"
print(com.replace('Everyone', 'All'))

##13. Split the string 'Coding For All' using space as the separator (split()) .
print(company.split())

##14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
t=("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon")
print(t.split(","))

##15. What is the character at index 0 in the string _Coding For All_.
print(company[0])

##16. What is the last index of the string _Coding For All_.
print(company[-1])

##17. What character is at index 10 in "Coding For All" string.
print(company[10])

##18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
com= "Python For Everyone"
acronym= com[0] + com[7] + com[11]
print (acronym)

##19. Create an acronym or an abbreviation for the name 'Coding For All'.
acr=company[0] + company[-7] + company[-3]
print (acr)

##20. Use index to determine the position of the first occurrence of C in Coding For All.
print (company.index ("C"))

##21. Use index to determine the position of the first occurrence of F in Coding For All.
print (company.index ("F"))

##22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
print (company.rfind ("l"))

##23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
oracion = 'You cannot end a sentence with because because because is a conjunction'
print (oracion.index ("because"))

##24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print (oracion.rindex ("because"))

##25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
palabra = "because"
primerapalabra= oracion.index (palabra)
ultimapalbra= oracion.rindex(palabra) + len(palabra)+1
print (oracion)
print(oracion[primerapalabra:ultimapalbra])

##26. Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
palabra = "because"
print (oracion.index(palabra))

##27.Slice out the phrase 'because because because' in the following sentence: ' You cannot end a sentence with because because because is a conjunction'
palabra = "because"
primerapalabra= oracion.index (palabra)
ultimapalbra= oracion.rindex(palabra) + len(palabra)+1
print (oracion)
print(oracion[primerapalabra:ultimapalbra])

##28. Does '\'Coding For All' start with a substring _Coding_?
print(company.startswith("Coding"))

##29. Does 'Coding For All' end with a substring _coding_?
print(company.endswith ("coding"))

##30. '&nbsp;&nbsp; Coding For All &nbsp;&nbsp;&nbsp; &nbsp;' &nbsp;, remove the left and right trailing spaces in the given string.
remove= "'&nbsp;&nbsp; Coding For All &nbsp;&nbsp;&nbsp; &nbsp;' &nbsp;"
print (remove.strip(" &nbsp; "))

##31.Which one of the following variables return True when we use the method isidentifier():
print ("30DaysOfPython".isidentifier())
print ("thity_days_of_python".isidentifier())

##32.The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
names = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
resu= " #".join(names)
print(resu)

##33.Use the new line escape sequence to separate the following sentences.
print('I am enjoying this challenge. \nI just wonder what is next')

##34. Use a tab escape sequence to write the following lines.
print ('Name\tAge\tCountry\tCity ')
print("Asabeneh\t250\tFinland\tHelsinki ")

##35.Use the string formatting method to display the following:
radio= 10
area= 3.14 * radio ** 2
f_s='The area of a circle with radius %d is %.2f meters square. '%(radio, area)
print (f_s)

##36.Make the following using string formatting methods:
a=8
b=6
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) 
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

print("revisado")