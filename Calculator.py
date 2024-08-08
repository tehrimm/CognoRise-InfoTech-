def calculator():
    while True:
        print("\nSimple Calculator")
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("0. Exit")

        # Get user input
        choice = input("Enter choice(0 to exit!): ")

        # Check if the user wants to exit
        if choice == '0':
            print("Exiting the calculator. Goodbye!")
            break

        # Check if the choice is valid
        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"{num1} + {num2} = {num1 + num2}")

            elif choice == '2':
                print(f"{num1} - {num2} = {num1 - num2}")

            elif choice == '3':
                print(f"{num1} * {num2} = {num1 * num2}")

            elif choice == '4':
                if num2 != 0:
                    print(f"{num1} / {num2} = {num1 / num2}")
                else:
                    print("Error! Division by zero.")
        else:
            print("Invalid Input")

# Run the calculator function
calculator()
