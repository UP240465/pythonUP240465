### Exercises: Level 2

#1. Join A and B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
A.update(B)
print(A)

#1. Find A intersection B
print(A.intersection(B))

#1. Is A subset of B
print(A.issubset(B))

#1. Are A and B disjoint sets
print(A.isdisjoint(B))

#1. Join A with B and B with A
print(A.union(B))
print((B.union(A)))

#1. What is the symmetric difference between A and B
print(A.symmetric_difference(B))

#1. Delete the sets completely
del A
del B
