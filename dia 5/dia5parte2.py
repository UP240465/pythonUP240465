### Exercises: Level 2

#1 The following is a list of 10 students ages:

#```sh
#ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#```

#- Sort the list and find the min and max age
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
age_en_orden=sorted(ages)
print(age_en_orden)
minimo=min(age_en_orden)
maximo=max(age_en_orden)
print(minimo, maximo)
# Add the min age and the max age again to the list
age_en_orden.insert(0, age_en_orden[0])
age_en_orden.insert(-1, age_en_orden[-1])
print(age_en_orden)

# Find the median age (one middle item or two middle items divided by two)
medio=len(age_en_orden)//2
print(age_en_orden[medio])
# Find the average age (sum of all items divided by their number )
promedio=sum(age_en_orden)//(len(age_en_orden))
print(promedio)
# Find the range of the ages (max minus min)
rango=max(age_en_orden)-(min(age_en_orden))
print (rango)

# Compare the value of (min - average) and (max - average), use _abs()_ method
valor1=min(age_en_orden)-(promedio)
valor2=max(age_en_orden)-(promedio)
print(abs(valor1-valor2))

#. Find the middle country(ies) in the [countries list](https://github.com/Asabeneh/30-Days-Of-Python/tree/master/data/countries.py)
#. Divide the countries list into two equal lists if it is even if not one more country for the first half.
#. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.

