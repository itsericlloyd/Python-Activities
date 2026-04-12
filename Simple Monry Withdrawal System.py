balance = 5000 

while True:
    print("\n=== Homepage ===")
    print("1.Withdraw")
    print("2.Balance")
    print("3.Log out")

    choice = input("Enter number: ")

    if choice == "1":
        try:
            amount = float(input("Enter amount to withdraw: "))

            if amount <= 0:
                print("Enter a valid amount.")
                continue

            if amount > balance:
                print("Insufficient funds.")
                
                while True:
                    print("\nOptions:")
                    print("1.Try again")
                    print("2.Balance")
                    print("3.Log out")

                    option = input("Choose option: ")

                    if option == "1":
                        break
                    elif option == "2":
                        print("Current balance:", int(balance))
                    elif option == "3":
                        print("Logging Out.")
                        exit()
                    else:
                        print("Invalid choice.")
                continue

            balance -= amount
            print("Withdrawal successful.")
            print("Remaining balance:₱", int(balance))

        except ValueError:
            print("Invalid input. Enter a number.")

    elif choice == "2":
        print("Current balance:₱", int(balance))

    elif choice == "3":
        print("Thank you. Goodbye.")
        break

    else:
        print("Invalid choice. Try again.")