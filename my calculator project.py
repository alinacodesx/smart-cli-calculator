# my calculator project
# infnite loop, handles wrong typing, take float input ,prevent divide by zero with continue/ exit option, history
# Smart CLI Calculator 
# Smart CLI Calculator

history = []

while True:
    print("\n" + "=" * 35)
    print("           SMART CALCULATOR")
    print("=" * 35)
    print("Type 'exit' to quit or 'history' to view past calculations.\n")

    operation = input("Enter operator (+, -, *, /, //, **, %): ").strip()

    # Exit program
    if operation.lower() == "exit":
        print("Exiting calculator.")
        break

    # Show history
    if operation.lower() == "history":
        if not history:
            print("No calculations yet.")
        else:
            print("\n--- History ---")
            for item in history:
                print(item)
        continue

    # Take numeric input safely
    try:
        n1 = float(input("Enter first number: "))
        n2 = float(input("Enter second number: "))
    except ValueError:
        print("Error: Please enter valid numbers.")
        continue

    # Perform operations
    if operation == "+":
        result = n1 + n2

    elif operation == "-":
        result = n1 - n2

    elif operation == "*":
        result = n1 * n2

    elif operation == "/":
        if n2 == 0:
            print("Error: Cannot divide by zero.")
            continue
        result = n1 / n2

    elif operation == "//":
        if n2 == 0:
            print("Error: Cannot divide by zero.")
            continue
        result = n1 // n2

    elif operation == "**":
        result = n1 ** n2

    elif operation == "%":
        if n2 == 0:
            print("Error: Cannot divide by zero.")
            continue
        result = n1 % n2

    else:
        print("Error: Invalid operator.")
        continue
    
# Display result nicely 
    output = f"{n1} {operation} {n2} = {result}"
    print("Result:", output)

# save history 
    history.append(output)


   