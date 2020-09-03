
num_int = int(input("Input a number: "))    # Do not change this line

max_int = 0

# While num_int er positive number ask again

while num_int >= 0 :
    # If max_int is less than num_int, set max_int == num_int
    if num_int >= max_int :
        max_int = num_int
    num_int = int(input("Input a number: "))

print("The maximum is", max_int)    # Do not change this line
