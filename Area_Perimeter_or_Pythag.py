x, y, pi = 0, 0, 3.14159
perimeter, area, pythag = 0, 0, 0
satisfied = False

question = input("Would you like to work out:\n1. Perimeter\n2. Area\n3. Pythag\n")

while not satisfied:
    if question == "1" or question.lower() == "perimeter":
        question2 = input("Square or Circle?\n")
        if question2.lower() == "square":
            x = float(input("What is the side length of the square?\n"))
            perimeter = 4 * x
            print("Perimeter of square:", perimeter)
        elif question2.lower() == "circle":
            x = float(input("What is the radius of the circle?\n"))
            perimeter = 2 * pi * x
            print("Perimeter of Circle:", perimeter)
        satisfied = True
    elif question == "2" or question.lower() == "area":
        question2 = input("Square or Circle?\n")
        if question2.lower() == "square":
            x = float(input("What is the side length of the square?\n"))  
            area = x**2
            print("Square area is:", area)
        elif question2.lower() == "circle":
            x = float(input("What is the radius of the circle?\n"))
            area = pi * (x**2)
            print("Circle area:", area)
        satisfied = True
    elif question == "3" or question.lower() == "pythag":
        x = float(input("What is the length of the first side?\n"))
        y = float(input("What is the length of the second side?\n"))
        from math import sqrt
        pythag = sqrt(x**2 + y**2)
        print("Hypotenuse is:", pythag)   
        satisfied = True           
    else:
        print("Invalid input! Please choose 1, 2, or 3.")
        question = input("Would you like to work out:\n1. Perimeter\n2. Area\n3. Pythag\n")
        satisfied = False
