import math
import sys

def runCalculator():
    while True:
        print("=== WELCOME TO BASIC CALCULATOR ===")
        print("1. Addition")
        print("2. Substraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exponentation")
        print("Page (1/2)")
        print("Input the letter E if you wish to move on the next page")
        print("Input the symbol ` to exit program")

        options = input("Choose your option {1/2/3/4/5/E/`} : ")

        if options == "1":
            num1 = float(input("Input first number : "))
            num2 = float(input("Input second number : "))
            result = addition(num1,num2)
            print("Result : ",result)

        elif options == "2":
            num1 = float(input("Input first number : "))
            num2 = float(input("Input second number : "))
            result = substraction(num1,num2)
            print("Result : ",result)

        elif options == "3":
            num1 = float(input("Input first number : "))
            num2 = float(input("Input second number : "))
            result = multiplication(num1,num2)
            print("Result : ",result)

        elif options == "4":
            num1 = float(input("Input first number : "))
            num2 = float(input("Input second number : "))
            result = division(num1,num2)
            print("Result : ",result)

        elif options == "5":
            num1 = float(input("Input first number : "))
            num2 = float(input("Input power : "))
            result = exponentation(num1,num2)
            print("Result : ",result)

        elif options == "E":
            while True:
                print("6. Modulo aka Modulus")
                print("7. Square Root")
                print("Page (2/2)")
                print("Input the letter Q if you wish to go back to previous page")
                options = input("Choose your option {6/7/Q} : ")
                if options == "6":
                    num1 = float(input("Input first number : "))
                    num2 = float(input("Input second number : "))
                    result = modulo(num1,num2)
                    print("Result : ", result)
                elif options == "7":
                    num1 = float(input("Input a number : "))
                    result = sqrt(num1)
                    print("Result : ", result)
                elif options == "Q":
                    break
                else :
                    print("Invalid option input!")

        elif options == "`":
            print("See you next time")
            break
        else :
            print("Invalid option input!")


def addition(num1,num2):
    result = num1+num2
    return result
def substraction(num1,num2):
    result = num1-num2
    return result
def multiplication(num1,num2):
    result = num1*num2
    return result
def division(num1,num2):
    result = num1/num2
    return result
def exponentation(num1,num2):
    result = pow(num1,num2)
    return result
def modulo(num1,num2):
    result = num1%num2
    return result
def sqrt(num1):
    result = sqrt(num1)
    return result

