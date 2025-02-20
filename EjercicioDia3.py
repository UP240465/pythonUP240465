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