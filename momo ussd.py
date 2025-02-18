pin = "1234"
balance = 1000.00


#              Main Menu
def menu():
    print("1 Send Money")
    print("2 Withdraw Cash")
    print("3 Check Balance")
    print("4 Reset/ Change Pin")
    print("5 Exit ")
    option = input("Option: ")
    return option


#               Check and Validate the pin
def checkPin():
    access = False
    for i in range(3):
        guessPin = input("Enter Pin: ")
        if pin == guessPin:
            access = True
            break
        else:
            print("Incorrect Pin.")
    return access


#                   Operations
def operation(option):
    global balance, pin

#                   Sending
    if option == '1':
        receiver = input("Enter recipient number: ")
        if len(receiver) == 10:
            amount = float(input("Enter amount to send: GH$"))
            if amount <= balance and checkPin():
                balance -= amount
                print(f"An amount of GH$ {amount} has been sent Successfully to {receiver}\n  Thank You!!!")
            else:
                print(f"Insufficient Funds \nAccount Balance: GH$ {balance}")
        else:
            print("Phone number should be 10 digit.")
            operation('1')

#                   Withdrawal
    elif option == '2':
        tillNumber = input("Enter agent till number: ")
        if 4 <= len(tillNumber) <= 6:
            tillNumber = int(tillNumber)
            amount = float(input("Enter amount to withdraw: GH$"))
            if amount <= balance and checkPin():
                balance -= amount
                print(f"You've successfully withdrawn GH${amount} from agent: {tillNumber} \n Your Welcome!!!")
            else:
                print(f"Insufficient Funds \nAccount Balance: GH$ {balance}")
        else:
            print("Merchant till number should be 4 - 6 digits. Try again.")
            operation('2')

#                    Check Balance
    elif option == '3':
        if checkPin():
            print(f"Your account balance is GH${balance}")
            print("Your Monies are safe here! Fear not.")
        else:
            print("Incorrect pin")

#                    Reset pin
    elif option == '4':
        for i in range(3):
            if i > 0:
                print("Incorrect Pin.")
            if checkPin():
                newPin = input("Set New Pin: ")
                if len(newPin) == 4:
                    pin = newPin
                    break
                else:
                    print("Pin must be 4 numbers.")


operation(menu())
