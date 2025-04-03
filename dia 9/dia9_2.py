### Exercises: Level 2

##1. Write a code which gives grade to students according to theirs scores:

'''sh
80-100, A
70-89, B
60-69, C
50-59, D
0-49, F
 '''

puntuacion =int(input("pon tu puntuacion"))
if 80<=puntuacion and puntuacion<=100:
    print('tu nivel es A')
elif 70<=puntuacion and puntuacion<89:
    print('tu grado es B')
elif 60<=puntuacion and puntuacion<=69:
    print('tu grado es C')
elif 50<=puntuacion and puntuacion<=59:
    print('tu grado es D')
elif 0<=puntuacion and puntuacion<=49:
    print('tu grado es F')

#1. Check if the season is Autumn, Winter, Spring or Summer. If the user input is:
''' September, October or November, the season is Autumn.
    December, January or February, the season is Winter.
    March, April or May, the season is Spring
   June, July or August, the season is Summer '''
 
mes=str(input('pon el mes'))
if mes=='September' or mes=='October' or mes=='November':
    print('the season is Autumn')
elif mes=='December' or mes=='January' or mes=='February':
    print('the season is Winter')
elif mes=='March' or mes=='April' or mes=='May':
    print('the season is Spring')
elif mes=='June' or mes=='July' or mes=='August':
    print('the season is Summer')

 # 2. The following list contains some fruits:

   # ```sh
   # fruits = ['banana', 'orange', 'mango', 'lemon']
   # ```

   # If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')

fruits = ['banana', 'orange', 'mango', 'lemon']
frutas=(str(input('add a fruit to the list')))
if frutas in fruits:
    print('That fruit the already exist in the list')
    print(fruits)
else:
    fruits.append(frutas)
    print(fruits)
 
print("revisado")