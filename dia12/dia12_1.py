##1 Writ a function which generates a six digit/character random_user_id
def random_user_id():
    import random
    import string
    user= ''.join(random.choices(string.ascii_letters+ string.digits + string.punctuation, k=6))
    return user
print( random_user_id())

#2. Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
def user_id_gen_by_user():
    import random
    import string
    ch= int(input('put thr number of characters'))
    numID=int(input('put the number of ID to generate'))
    userID= [''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=ch))for _ in range(numID)]
    return userID
print(user_id_gen_by_user())
   

#3. Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
def rgb_color_gen():
   import random
   red=random.randint(0, 255)
   green=random.randint(0, 255)
   blue=random.randint(0, 255)
   return(red,green,blue)
print(rgb_color_gen)

print("revisado")