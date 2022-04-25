##### Drawing scheme pattern square

#   # # # # # # # # # #
#   # . . . . . . . . #
#   # . . . . . . . . #
#   # . . . . . . . . #
#   # . . . . . . . . #
#   # . . . . . . . . #
#   # . . . . . . . . #
#   # . . . . . . . . #
#   # . . . . . . . . #
#   # # # # # # # # # #
n = int(input("Enter the number: "))

print("\n")

for y in range(1, n):
    for x in range(1, n):
        if y == 1 or y == n-1 or x == 1 or x == n-1:
            print("#", end=" ")
        else:
            print(".", end=" ")
    print()

print("\n")