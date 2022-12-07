import math
def calc():
    pi = 22/7
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Mod")
    print("6. Square Root")
    print("7. Exponent")
    print("8. Sine")
    print("9. Cosine")
    print("10. Tangent")
    print("11. Conversion from radian to degree")
    print("12. Conversion from degree to radian")
    operation = int(input("Which operation do you want to perform? "))
    if operation == 1 or operation == 2 or operation == 3 or operation == 4 or operation == 5:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        if operation == 1:
            print("The sum of", num1, "and", num2, "is", (num1 + num2))
            cont = int(input("If you wish to exit press 0 else press 1: "))
            if cont == 0:
                return None
            if cont == 1:
                calc()
        if operation == 2:
            print(num1, "subtracted by", num2, "is", (num1 - num2))
            cont = int(input("If you wish to exit press 0 else press 1: "))
            if cont == 0:
                return None
            if cont == 1:
                calc()
        if operation == 3:
            print("The multiplication of", num1, "and", num2, "is", (num1 * num2))
            cont = int(input("If you wish to exit press 0 else press 1: "))
            if cont == 0:
                return None
            if cont == 1:
                calc()
        if operation == 4:
            print(num1, "divided by", num2, "is", (num1 / num2))
            cont = int(input("If you wish to exit press 0 else press 1: "))
            if cont == 0:
                return None
            if cont == 1:
                calc()
        if operation == 5:
            print("The mod of", num1, "and", num2, "is", (num1 % num2))
            cont = int(input("If you wish to exit press 0 else press 1: "))
            if cont == 0:
                return None
            if cont == 1:
                calc()
    if operation == 6:
        num = int(input("Enter the number: "))
        print("The square root of", num, "is", (math.sqrt(num)))
        cont = int(input("If you wish to exit press 0 else press 1: "))
        if cont == 0:
            return None
        if cont == 1:
            calc()
    if operation == 7:
        num = int(input("Enter the number: "))
        power = int(input("Enter the exponent: "))
        print(num, "raised to the power of", power, "is", (pow(num,power)))
        cont = int(input("If you wish to exit press 0 else press 1: "))
        if cont == 0:
            return None
        if cont == 1:
            calc()
    if operation == 8:
        num = int(input("Enter the number: "))
        print("The sine of", num, "is", (math.sin(num)))
        cont = int(input("If you wish to exit press 0 else press 1: "))
        if cont == 0:
            return None
        if cont == 1:
            calc()
    if operation == 9:
        num = int(input("Enter the number: "))
        print("The cosine of", num, "is", (math.cos(num)))
        cont = int(input("If you wish to exit press 0 else press 1: "))
        if cont == 0:
            return None
        if cont == 1:
            calc()
    if operation == 10:
        num = int(input("Enter the number: "))
        print("The tangent of", num, "is", (math.tan(num)))
        cont = int(input("If you wish to exit press 0 else press 1: "))
        if cont == 0:
            return None
        if cont == 1:
            calc()
    if operation == 11:
        num = int(input("Enter the number(in radian): "))
        print(num,"radian in degree is", (num*(180/pi)))
        cont = int(input("If you wish to exit press 0 else press 1: "))
        if cont == 0:
            return None
        if cont == 1:
            calc()
    if operation == 12:
        num = int(input("Enter the number(in degree): "))
        print(num,"degree in radian is", (num*(pi/180)))
        cont = int(input("If you wish to exit press 0 else press 1: "))
        if cont == 0:
            return None
        if cont == 1:
            calc()
calc()