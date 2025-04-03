### Exercises: Level 1

#1. Declare a function _add_two_numbers_. It takes two parameters and it returns a sum.
def addtwoNumbers():
    primernumero=float(input('Ingresa un numero: '))
    segundonumero=float(input('Ingresa otro numero: '))
    suma= primernumero + segundonumero
    return ' la suma es ', suma

#2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates _area_of_circle_.
def areaDeUnCirculo():
    radio=float(input('Cuales el radio del circulo: '))
    pi=3.1416
    area=pi*radio*radio
    return 'el area de un circulo es: ', area

#3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums():
    rnum=input('Introduce el numero que tu quieras: ')
    if "." in rnum:
        rnum =float(rnum)
        print (f"El tipo de numero '{rnum}' que ingresaste es: '{type(rnum)}'")
    elif "." in rnum == False:
        rnum= int (rnum)
        print(f"El tipo de numero '{rnum}' que ingresaste es: '{type(rnum)}'")
    else:
        print(f"Error el numero '{rnum}' no es valido.")
    return""

#4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, _convert_celsius_to-fahrenheit_.
def con_C_to_F():
    C=float(input('ingresa la temperatura que quieres convertir de Celsius a fahrenheint: '))
    F = (C*9/5)+32
    return 'En fahrenheint son', F

#5. Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season():
    Autumn={'September','Septiembre', 'October', 'Octubre', 'November', 'Noviembre' }
    Winter={'Dicember', 'Diciembre', 'January', 'Enero', 'February','Febrero' }
    Spring={'March', 'Marzo', 'April', 'Abril', 'May', 'Mayo'}
    Sumer={'June', 'Junio', 'July', 'Julio', 'Agust', 'Agosto'}

    month = input ('Ingresa un mes para decirte la estacion del año: ')

    if month in Autumn:
        print('La estacion del año es Otoño')
    elif month in Winter:
        print('La estacion del año es Invierno')
    elif month in Spring:
        print('La estacion del año es Primavera')
    elif month in Sumer:
        print('La estacion del año es Verano')
    else:
        print ('Error: el mes que ingreso no es valido porfavor ingrese la primera con mayuscula y lo demas con minuscula')
        return""

#6. Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope():
    x1 = float(input ('Ingresa el dato x1 de la pendiente: '))
    y1 = float(input ('Ingresa el dato y1 de la pendiente: '))
    x2 = float(input ('Ingresa el dato x2 de la pendiente: '))
    y2 = float(input ('Ingresa el dato y2 de la pendiente: '))
    M = (y2 - y1)/(x2 - x1)
    return 'La pendiente es de: ', M

#7. Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, _solve_quadratic_eqn_.
def solve_quadratic_eqn():

    A = float(input('Ingresa el numero A de tu ecuacion cuadratica: '))
    B = float(input('Ingresa al numero B de tu ecuacion cuadratica: '))
    C = float(input('Ingresa el numero C de tu ecuacion cuadratica: '))
    x1 = (-B/2*A)
    x2 = ((B**2 - 4*A*C)**.5/(2*A))
    return f"El valor de x es igual a {x1} +- {x2}"

#8. Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list():
    it_companies=['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
    return ""

#9. Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).

#```py
#print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
#print(reverse_list1(["A", "B", "C"]))
# ["C", "B", "A"]
#```
def reserve_list(*elementos):
    list_whatever=[]
    for n in elementos[::-1]:
        list_whatever.append(n)
    return list_whatever

#10. Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items():
    phrase = input('Ingresa una frase que quieras que pase sus letras a mayusculas: ')
    phrase = str(phrase)
    print(phrase.upper())
    return""

#11. Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.

#```py
#food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
#print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat']
#numbers = [2, 3, 7, 9]
#print(add_item(numbers, 5))      [2, 3, 7, 9, 5]
#```
def add_item():
    item_list = []
    itemToAdd = str(input('Ingresa un elemento para agregar a la lista: '))
    item_list.append(itemToAdd)
    print(item_list)
    return""

#12. Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.

#```py
#food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
#print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
#numbers = [2, 3, 7, 9]
#print(remove_item(numbers, 3))  # [2, 7, 9]
#```



#13. Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.

#```py
#print(sum_of_numbers(5))  # 15
#print(sum_of_numbers(10)) # 55
#print(sum_of_numbers(100)) # 5050
#```
def sum0fNumbers(rang):
    rang= int (rang)
    num = 0
    for i in range(rang):
        num=num + i
        print(num)
    return ""

#14. Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum0f0dds(rang):
    parnum=[]
    impnum=[]
    for i in range(rang):
        if i % 2 == 0:
            parnum.append(i)
        else:
            impnum.append(i)
    
    return f"La suma de los numeros impares del 1 al {rang} es igual a ", sum(impnum)

print(sum0f0dds(50))


#15. Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.

def sum0feven(rang):
    parnum = []
    impnum=[]
    for i in range(rang):
        if i % 2 == 0:
            parnum.append(i)
        else:
            impnum.append(i)
    
    return f"La suma de los numeros impares del 1 al {rang} es igual a ", sum(parnum)

print(sum0feven(50))
