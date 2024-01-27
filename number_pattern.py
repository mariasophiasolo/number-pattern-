# create a pattern of numbers

# define the range for the outer loop
for numbers in range(1, 5):
    # create an inner loop to print numbers up to the current value of number
    for i in range (1, numbers + 1):
        print (numbers, end=" ")
# move to the next line after each row to display the pattern correctly
        print()