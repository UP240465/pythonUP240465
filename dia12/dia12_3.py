### Exercises: Level 3

#1. Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
import random
def shuffle_list(lst):
    shuffled=lst[:]
    random.shuffle(shuffled)
    return (shuffled)
print('lista normal ', [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(shuffle_list([1, 2, 3, 4, 5, 6, 7, 8, 9]))

#1. Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
def u_r_numbers():
    import random
    return random.sample(range(0, 10), 7)
print("unique random Number: ", u_r_numbers())