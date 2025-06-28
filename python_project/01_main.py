def show_menu():
    print("=== Main Menu ===")
    print("1. 2 Dimensional Shapes")
    print("2. 3 Dimensional Shapes")
    print("3. Simple Calculator")
    print("4. Exit Program")

import math
from shapes_2d import square, rectangle, circle
from shapes_3d import cube, cuboid, sphere

def shapes_2d_menu():
    while True:
        print("=== 2D Shapes Menu ===")
        print("1. Square")
        print("2. Rectangle")
        print("3. Circle")
        print("4. Back to main menu")

        options = input("Choose your options {1/2/3/4} : ")

        if options == "1":
            s = float(input("Input square side length: "))
            perimeter,area = square(s)
            print("Perimeter : ", perimeter)
            print("Area : ", area)
        elif options == "2":
            l = float(input("Input rectangle length: "))
            w = float(input("Input rectangle width: "))
            perimeter,area = rectangle(l,w)
            print("Perimeter : ", perimeter)
            print("Area : ", area)
        elif options == "3":
            r = float(input("Input circle radius: "))
            d, perimeter, area = circle(r)
            print("Diameter : ", d)
            print("Perimeter : ", perimeter)
            print("Area : ", area)
        elif options == "4":
            break
        else:
            print("Option invalid!")  

def shapes_3d_menu():
    while True:
        print("=== 3D Shapes Menu ===")
        print("1. Cube")
        print("2. Cuboid")
        print('3. Sphere')
        print("4. Back to main menu")

        options = input("Choose your options {1/2/3/4} : ")

        if options == "1":
            r = float(input("Input cube edge length: "))
            surfaceArea,volume = cube(r)
            print("Surface area : ", surfaceArea)
            print("Volume : ", volume)
        elif options == "2":
            l = float(input("Input cuboid length: "))
            w = float(input("Input cuboid width: "))
            h = float(input("Input cuboid height: "))
            surfaceArea,volume = cuboid(l,w,h)
            print("Surface area : ", surfaceArea)
            print("Volume : ", volume)
        elif options == "3":
            r = float(input("Input sphere radiusL: "))
            surfaceArea,volume,d = sphere(r)
            print("Diameter : ",d)
            print("Surface area : ",surfaceArea)
            print("Volume",volume)
        elif options == "4":
            break
        else:
            print("Option invalid!")


#main loop
while True:
    show_menu()
    options = input("Choose your option {1/2/3/4} : ")

    if options == "1":
        shapes_2d_menu()
    elif options == "2":
        shapes_3d_menu()
    elif options == "3":
        print("WORK IN PROGRESS")
    elif options == "4":
        print("Bye")
        break
    else:
        print("Invalid Input!!")











