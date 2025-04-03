### Exercises: Level 2
    
1.  #Use for loop to iterate from 0 to 100 and print the sum of all numbers.

'''sh
   The sum of all numbers is 5050.
   '''
n=0
for i in range (101):
    n += i
    print(n)


1. #Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
'''sh
    The sum of all evens is 2550. And the sum of all odds is 2500.
    '''
sumapar=0
sumaimpar=0
for i in range (101):
    if i % 2 ==0:
        sumapar+=i
    else:
        sumaimpar+=i
print('la suma par es de ', sumapar)
print('la suma impar es de ',sumaimpar)

print("revisado")