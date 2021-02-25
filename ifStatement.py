"""
Assign 8 to the variable x and 15 to the variable y.
In the same cell, create 2 conditional statements.
Let the first one print "At least one of the conditions is satisfied." if x is greater than 3 or y is even.
Let the second one print "Neither condition is satisfied." if x is less than or equal to 3 and y is odd.
"""
x = 8
y = 15

if x > 3 or y %2 ==0:
    print("At least one of the conditions is satisfied.")
elif x <=3 and y %2==1:
    print("Neither condition is satisfied.")

"""
Write an if statement that asks for the user's name via input() function. If the name is "Bond" make it print 
""Hi " name " welcome to the team." Otherwise make it print "Good morning NAME". (Replace Name with user's name)
"""
name= input("What is your name: ")

if name.lower() == "bond":
    print("Welcome on board 007")
else:
    print("Hi " +name +" welcome to the team!")


# Write a function named "evens" which returns True if a number is even and otherwise returns False
def even(i):
    if i%2 ==0:
        return True
    else: 
        return False

print(even(99))
print(even(98))

