import rios0021Library
import os
exit = False
while (exit != True):
    os.system("cls||clear")
    print("************************************************")
    print("**                    MENU                    **")
    print("**--------------------------------------------**")
    print("** 1. Vertical Line                           **")
    print("** 2. Horizontal Line                         **")
    print("** 3. Staircase                               **")
    print("** 4. Random Pixels                           **")
    print("** 5. Clear Backlight                         **")
    print("** 6. Bonus Rainbow!!!                        **")
    print("**                                            **")
    print("** 0. EXIT                                    **")
    print("************************************************")
    option = (input("Please choose an option (number): "))
    print(option)

    if(option == "1"):
        # Vertical Line
        os.system("cls||clear")
        x = (int(input("Please enter the x pixel for the line (0 - 127)")))
        rios0021Library.drawVerticalLine(x)
    elif(option == "2"):
        # Horizontal Line
        os.system("cls||clear")
        rios0021Library.drawHorizontalLine(int(input("Please enter the y value for the horizontal line (0 - 63)")))
    elif(option == "3"):
        # Staircase
        os.system("cls||clear")
        startPoint = input("Please enter point x,y separated by comma: ").split(",")
        width = (int(input("Enter a width for the stair: ")))
        height = (int(input("Enter a height for the stair: ")))
        orientation = (input("Please enter 'r' for right or 'l' for left: "))
        rios0021Library.drawStair(startPoint,width,height,orientation)
    elif(option == "4"):
        # Random pixels
        os.system("cls||clear")
        numSeconds = (int(input("Pleas enter how many seconds to print random pixels: ")))
        rios0021Library.drawRandomPixels(numSeconds)
    elif(option == "5"):
        # Clear backlight
        rios0021Library.clearBacklight()
    elif(option == "6"):
        # RAINBOW
        os.system("cls||clear")
        numLoops = (int(input("Pleas enter how many loops to do in the rainbow: ")))
        rios0021Library.colorRainbow(numLoops)
    else:
        exit = True
