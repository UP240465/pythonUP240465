##1. Iterate 0 to 10 using for loop, do the same using while loop.
contar=0
while contar<11:
    print(contar)
    contar=contar+1


##2. Iterate 10 to 0 using for loop, do the same using while loop.
i = 0
contar=10
while contar>0:
    print(contar)
    contar=contar-1

#3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:

  # ```py
     #
     ##
     ###
     ####
     #####
     ######
     #######
   #```
car = '#'
for i in range (7):
    print(car*i)

#4. Use nested loops to create the following:

   #```sh
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   #```
for i in range(8):
    print('#'*8)


##5. Print the following pattern:

   #```sh
   #0 x 0 = 0
   #1 x 1 = 1
   #2 x 2 = 4
   #3 x 3 = 9
   #4 x 4 = 16
   #5 x 5 = 25
   #6 x 6 = 36
   #7 x 7 = 49
   #8 x 8 = 64
   #9 x 9 = 81
   #10 x 10 = 100
   #```
for i in range(11):
    print(i, 'x', i, '=', (i+i))

##6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
tec=['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for item in tec:
    print(item)

#7. Use for loop to iterate from 0 to 100 and print only even numbers
for i in range(101):
    if i%2 ==0:
        print(i)

#8. Use for loop to iterate from 0 to 100 and print only odd numbers
for i in range(101):
    if i%2 != 0:
        print(i)