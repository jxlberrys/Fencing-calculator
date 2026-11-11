# Main routine starts here...

keep_going = ""
while keep_going =="":
    # Get width and height
    
    width = float(input("Enter the width of the fence: "))
    height = float(input("Enter the height of the fence: "))
    cost = float(input("Enter the cost per unit: "))
    # Calculate the perimeter and price
    perimeter = 2 * (width + height)
    # Display output
    print(f"Perimeter: {perimeter} units")
    print(f"Price: ${price:.2f}")
    # Ask user to keep going
    keep_going = input("Press <Enter> to continue or any key to stop")
print()
print("Thanks for using this program")
