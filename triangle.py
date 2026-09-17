traiangleOne = float(input("Enter the first side of triangle: "))
triangleTwo = float(input("Enter the second side of triangle: "))
triangleThree = float(input("Enter the third side of triangle: "))


if (traiangleOne + triangleTwo)> triangleThree and (traiangleOne + triangleThree) > triangleTwo and (triangleTwo + triangleThree) > traiangleOne:
    print(f"The triangle is valid with sides {traiangleOne}, {triangleTwo}, and {triangleThree}.")
else:
    print(f"The triangle is not valid with sides {traiangleOne}, {triangleTwo}, and {triangleThree}.")


s = (traiangleOne + triangleTwo + triangleThree) / 2
area = (s * (s - traiangleOne) * (s - triangleTwo) * (s - triangleThree)) ** 0.5

print(f"The area of the triangle is: {area}")
