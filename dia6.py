### Exercises: Level 1

##1. Create an empty tuple
print(tuple())

##2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
hermanos=('Kevin', 'Paulo', 'Yazid'. split())
hermanas=('Yajaira', 'Frida', 'Gina'. split())

##3. Join brothers and sisters tuples and assign it to siblings
familia= hermanos+hermanas
print (familia)

##4. How many siblings do you have?
print (len(familia))

##5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
padres = ('Georgina', 'Raudel')
family_members= familia + padres
print (family_members)

### Exercises: Level 2

##1. Unpack siblings and parents from family_members
family_members=list(family_members)
print (family_members)
siblings= (family_members[0:5])
print('Mis hermanos', siblings)
sibling = (family_members[6:])
print ('Mis papas son ',sibling)

##2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
food_stuff_tp= ('manzana', 'mango', 'platano', 'papa', 'calabaza', 'chayote', 'carne', 'leche', 'huevo')
print (food_stuff_tp)

##3. Change the about food_stuff_tp  tuple to a food_stuff_lt list
lista=list(food_stuff_tp)
print (lista)

##4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.


##5. Slice out the first three items and the last three items from food_staff_lt list

##6. Delete the food_staff_tp tuple completely

##7. Check if an item exists in  tuple:

##- Check if 'Estonia' is a nordic country
##- Check if 'Iceland' is a nordic country##