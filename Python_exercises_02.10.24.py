# Part one: using if, elif and else to compare the numbers

# #asking the user to write a number
write_number = int(input("Please type a number: "))
# check if it is positive or negative or zero
if write_number == 0: # check if the given number is equal to zero
    print(f"{write_number} is a null")
elif write_number > 0: # check if the give number is greater than zero
    print(f"{write_number} is a postive number")
else: # if it is not equal to zero and not greater than zero, then it is a negative number
    print(f"{write_number} is a negative number")


# Part two: using for-loop to count numbers from one to ten.
for numbers in range(1 , 11):
    print (numbers)


# Part three: using while-loop to check even or odd numbers.

# ask the user to give an input
zahl = int(input("Please type a number"))
# check if the result of given number divided by two is zero, then print... 
# when the given number divided by two is not zero, then it ask the user to type another number
while zahl % 2 != 0:
    zahl = int(input("The number is odd, please enter an even number: "))
print(f"The number {zahl} is an even number.")


