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

## 7
radio = float(input("ingresa el radio: "))
pi = 3.1416
area = pi*radio*radio
print ("El area es de: ", area)
circunferencia = 2 * pi * radio
print ("La circunferencia es de: ", circunferencia)

##8
m = 2
b = -2
x_intercept = -b / m
print("Pendiente (m): ", m)
print("Interseccion en Y (b): ", b)
print("Interseccion en X (m): ", m)

##9
import math
x_1 = 2
y_1 = 2
x_2 = 6
y_2 = 10
pendiente = ((y_2)-(y_1)/(x_2)-(x_1))
euclides = math.sqrt((x_2 - x_1) **2 + (y_2 - y_1) **2)
print("La pendiente es de: ", pendiente)
print("La euclides es de: ", euclides)

##10
if m == pendiente:
  print("Las pendientes son iguales")
elif m>pendiente:
    print("Las primera pendiente es mayor")
else:
    print("La segunda pendiente es mayor")

##11
a = 1
b = 6
c = 9
x = ( -b +-((b * b) - 4*(a * c))**.5)/2 * a
print (x)
print ("coloque el valor de x", x)
y = (x*x + 6*x + 9)
print ("El valor de y es: ", y)

##12
print("Largo de 'python' y 'dragon' y falsa comparacion")
len_python = len('python')
len_dragon = len('dragon')
falsy_comparision = len_python == len_dragon
print(f"Legth of 'python': {len_python}")
print(f"Legth of 'dragon': {len_dragon}")
print(f"falsy comparison (length of 'python' == length of 'dragon'): {falsy_comparision}")

##13
print("checar si 'on' esta en 'python' y 'dragon'")
on_in_both = 'on' in'python' and 'on' in 'dragon'
print("'on' in both 'python' and 'dragon': ", on_in_both)

##14
print("checar si 'jargon' esta en la frase")
frase = "I hope this course is not full of jargon"
jargon_in_frase = 'jargon' in frase
print("el 'jargon' esta en la frase:", jargon_in_frase)

##15
print("checar si 'on' no esta en 'python' y 'dragon'")
on_in_both = 'on' in'python' and 'on' in 'dragon'
if on_in_both == False :
  print("las dos palabras tienen 'on'")
else:
  print("las dos palabras no tienen 'on'")

##16
print("largo de python ")
len_python=len('python')
print("el largo de la palabra ", len_python)
len_python=float(len_python)
print("se convirtio el valor ", type (len_python))
len_python=str(len_python)
print("se convirtio el valor ", type (len_python))

##17
print("checar si el numero es par")
numero= int(input("ingresa un numero: "))
es_par= numero % 2 == 0
print(f"el numero {numero} es par: {es_par}")


