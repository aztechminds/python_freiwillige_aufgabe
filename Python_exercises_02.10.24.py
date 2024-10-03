# %% Part one: using if, elif and else to compare the numbers

#asking the user to write a number
print("Here you can check if the entered number is a negative, postive or a zero number, don't believe me, try it!!!")
write_number = int(input("enter a number, I will tell you the result: "))
# check if it is positive or negative or zero
if write_number == 0: # check if the given number is equal to zero
    print(f"{write_number} is zero")
elif write_number > 0: # check if the give number is greater than zero
    print(f"{write_number} is a postive number")
else: # if it is not equal to zero and not greater than zero, then it is a negative number
    print(f"{write_number} is a negative number")


# %% Part two: using for-loop to count numbers from one to ten.
print ("Now I am going to count from 1 to 10")
for numbers in range(1 , 11):
    print (numbers)


# %% Part three: using while-loop to check even or odd numbers.

# ask the user to give an input
print("Let's find out, if I can figure out Odd and Even numbers!")
zahl = int(input("Please enter a number: "))
# check if the result of given number divided by two is zero, then print... 
# when the given number divided by two is not zero, then it ask the user to type another number
while zahl % 2 != 0:
    zahl = int(input("it is a odd number, enter an even number: "))
print(f"Wow, I can tell now, you have entered an even number.")


# %% Part four: using def and return to calculate the sum of squares

def sum_of_squares (a, b):
    return a**2 + b**2

# Getting user input for a and b
print("Let's try some mathematic calculation!")
print("What about sum of squares!? Let's try it!!!")
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

result = sum_of_squares(a, b)
print(f"The sum of squares is {result}")
print ("It is fun!")


# %% Part 5: Extra FizzBuzz
print("Let's try something more funny!!")
print("It is called 'FizzBuzz'")
for zahl in range(1, 100):
    if zahl % 3 == 0 and zahl % 5 == 0:
        print("FizzBuzz")
    elif zahl %3 == 0:
        print("Fizz")
    elif zahl %5 == 0:
        print("Buzz")
    else: 
        print (zahl)

print ("\nThank for playing along :)")
print ("I hope you had fun too!")
# %%
