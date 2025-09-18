n = int(input("Enter a number: "))  # Example: 5
for i in range(n):
    for j in range(n):
        if i == j:   # primary diagonal condition
            print("*", end="")
        else:
            print(" ", end="")
    print()  # new line after each row
