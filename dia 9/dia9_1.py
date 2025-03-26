### Exercises: Level 1

#1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:

    #```sh
    #Enter your age: 30
    #You are old enough to learn to drive.
    #Output:
    #Enter your age: 15
    #You need 3 more years to learn to drive.
    #```
edad= int(input('pon tu edad:'))
if edad >=18:
    print('puedes manejar')
else:
    edad<18
    print('no pedes manejar no tienes la eadad')

#2. Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:

   # ```sh
    #Enter your age: 30
    #You are 5 years older than me.
   # ```
my_age=(int(input('put your age')))
your_age=(int(input('put the other age')))
diff=int(my_age-your_age)
if my_age == your_age:
    print('they are the same age', my_age)

elif diff==-1 or diff==1:
    diff=1
    print('the difference is', diff, 'year')

else:
    print('the difference is', diff, 'years')

#3. Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:

#```sh
#Enter number one: 4
#Enter number two: 3
#4 is greater than 3
#```

a=int(input('pon un numero'))
b=int(input('pon otro numero'))
if a>b:
    print(a, 'is greater than', b)
elif a<b:
    print(a,'is smaller tan', b)
else:
    print(a, 'is equal to', b)