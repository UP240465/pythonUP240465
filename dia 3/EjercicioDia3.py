##1
age = 19

##2
altura = 1.70
print(type(altura))

##3
complejo = 3+8j
print(type(complejo))

## 4. Write a script that prompts the user to enter base and 
# height of the triangle and calculate an area of this 
# triangle (area = 0.5 x b x h).

base = float(input("Ingresa la base del triangulo: "))
altura = float(input("Ingresa la altura del triangulo: "))
area = 0.5 * base * altura
print ("La area del triangulo es de ", area)

## 5.Write a script that prompts the user to enter side a, side b, and side c of 
# the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).

sideA = float(input("Ingresa la medida del lado A: "))
sideB = float(input("Ingresa la medida del lado B: "))
sideC = float(input("Ingresa la medida del lado C: "))
perimetro = sideA + sideB + sideC
print ("El perimetro del triangulo es de ", perimetro)

## 6.Get length and width of a rectangle using prompt. Calculate its area 
# (area = length x width) and perimeter (perimeter = 2 x (length + width))

length = float(input("Ingresa el largo del rectangulo: "))
width = float(input("Ingresa el ancho del rectangulo: "))
area = length * width
print ("El area del rectangulo es de ", area)
perimetro = 2 * (length + width)
print ("El perimetro del rectangulo es de ", perimetro)

## 7.Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radio = float(input("ingresa el radio: "))
pi = 3.1416
area = pi*radio*radio
print ("El area es de: ", area)
circunferencia = 2 * pi * radio
print ("La circunferencia es de: ", circunferencia)

##8.Calculate the slope, x-intercept and y-intercept of y = 2x -2
m = 2
b = -2
x_intercept = -b / m
print("Pendiente (m): ", m)
print("Interseccion en Y (b): ", b)
print("Interseccion en X (m): ", m)

##9. Slope is (m = y2-y1/x2-x1). Find the slope and [Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance#:~:text=In%20mathematics%2C%20the%20Euclidean%20distance,being%20called%20the%20Pythagorean%20distance.) between point (2, 2) and point (6,10) 
import math
x_1 = 2
y_1 = 2
x_2 = 6
y_2 = 10
pendiente = ((y_2)-(y_1)/(x_2)-(x_1))
euclides = math.sqrt((x_2 - x_1) **2 + (y_2 - y_1) **2)
print("La pendiente es de: ", pendiente)
print("La euclides es de: ", euclides)

##10.Compare the slopes in tasks 8 and 9.
if m == pendiente:
  print("Las pendientes son iguales")
elif m>pendiente:
    print("Las primera pendiente es mayor")
else:
    print("La segunda pendiente es mayor")

##11.Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
a = 1
b = 6
c = 9
x = ( -b +-((b * b) - 4*(a * c))**.5)/2 * a
print (x)
print ("coloque el valor de x", x)
y = (x*x + 6*x + 9)
print ("El valor de y es: ", y)

##12.Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print("Largo de 'python' y 'dragon' y falsa comparacion")
len_python = len('python')
len_dragon = len('dragon')
falsy_comparision = len_python == len_dragon
print(f"Legth of 'python': {len_python}")
print(f"Legth of 'dragon': {len_dragon}")
print(f"falsy comparison (length of 'python' == length of 'dragon'): {falsy_comparision}")

##13.Use _and_ operator to check if 'on' is found in both 'python' and 'dragon'
print("checar si 'on' esta en 'python' y 'dragon'")
on_in_both = 'on' in'python' and 'on' in 'dragon'
print("'on' in both 'python' and 'dragon': ", on_in_both)

##14._I hope this course is not full of jargon_. Use _in_ operator to check if _jargon_ is in the sentence.
print("checar si 'jargon' esta en la frase")
frase = "I hope this course is not full of jargon"
jargon_in_frase = 'jargon' in frase
print("el 'jargon' esta en la frase:", jargon_in_frase)

##15.There is no 'on' in both dragon and python
print("checar si 'on' no esta en 'python' y 'dragon'")
on_in_both = 'on' in'python' and 'on' in 'dragon'
if on_in_both == False :
  print("las dos palabras tienen 'on'")
else:
  print("las dos palabras no tienen 'on'")

##16.Find the length of the text _python_ and convert the value to float and convert it to string
print("largo de python ")
len_python=len('python')
print("el largo de la palabra ", len_python)
len_python=float(len_python)
print("se convirtio el valor ", type (len_python))
len_python=str(len_python)
print("se convirtio el valor ", type (len_python))

##17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
print("checar si el numero es par")
numero= int(input("ingresa un numero: "))
es_par= numero % 2 == 0
print(f"el numero {numero} es par: {es_par}")

##18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
division = 7/3
d = float (7/3)
equal = d == division
print("eñ numero es igual: ", equal)

##19. Check if type of '10' is equal to type of 10
typ = int('10')
t=(10)
c=typ==t
print("tipo'10' es igual a 10: ",c)

##20.Check if int('9.8') is equal to 10
ch = float('9.8')
c= int(ch)
d=10
comparo=c==d
print("int('9.8') es igual a 10: ",comparo)

##21. Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
horas=int(input("ingresa las horas que trabajaste: "))
pago=float(input("cuanto te pagan por hora: "))
r=horas*pago
print("tu paga es de:", r)

##22.Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
años=int(input("ingresa tu edad: "))
s_a= 365*24*60*60
s_v=años *s_a
print(f"una persona puede vivir{s_v} segundos")

##23.Write a Python script that displays the following table
print("a a^0 a^1 a^2 a^3")
for a in range(1, 6): 
   print(f"{a} {a**0} {a**1} {a**2} {a**3}")

print("revisado")