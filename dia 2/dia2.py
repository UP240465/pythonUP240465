
##1

r=30
pi=3.1416
areaOfCircle=pi*r**2
circumOfCircle=2*pi*r
print( 'El area del circulo es de:', areaOfCircle)
print('La circunferencia del', circumOfCircle)

##2

r=int(input('Inserte el radio del circulo:'))
areaOfCircle=pi*r**2
circumOfCircle=2*pi*r
print( 'El area del circulo es de:', areaOfCircle)
print('La circunferencia del', circumOfCircle)

N=input('Ingresa su nombre:')
A=input('Ingresa sus apellidos:')
P=input('ingresa su país de origen:')
E=int(input('Ingresa su edad:'))


print('Tu nombre es: ' + N ,A,
      'Eres de :' + P,
      'Tu edad es de :',E)
print(type(N))
print(type(A))
print(type(P))
print(type(E))