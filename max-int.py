
num_int = int(input("Input a number: "))    # Do not change this line
max_int = None
while num_int > 0:
    num_int = int(input("Input a number: "))
    if max_int is None:
        max_int = num_int
    elif max_int < num_int:
        max_int = num_int
print("The maximum is", max_int)    # Do not change this line