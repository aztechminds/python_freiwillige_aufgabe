# asking the user to write a number
write_number = int(input("Please type a number: "))

# check if it is positive or negative or zero
if write_number == 0: # check if the given number is equal to zero
    print(f"{write_number} is a null")
elif write_number > 0: # check if the give number is greater than zero
    print(f"{write_number} is a postive number")
else: # if it is not equal to zero and not greater than zero, then it is a negative number
    print(f"{write_number} is a negative number")

