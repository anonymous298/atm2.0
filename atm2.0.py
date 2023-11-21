# this project is about an working atm logic
def atm_card():
    card = int(input("Enter your card (1 to add): "))
    if card == 1:
        pin()

    else:
        print("Get lost from here!")
        
# function to create a pin in atm
def pin():
    user_pin = int(input("Enter your 4 digits atm pin: "))
    pin = 1807

    if user_pin == pin:
        atm_options()
    else:
        raise ValueError("Your atm is blocked!")
        
# function to create options that will show on atm
def atm_options():
    
    # initiliazing balance
    balance = 0
    for i in range(0,50):

            print("\n(1 for withdrawal)")
            print("(2 for deposit)")
            print("(3 for balance check)")
            print("(0 for quit)")

            options = int(input("\nEnter Here: "))

            if options == 1:

                withdraw_user = int(input("enter your amount for withdrawal: "))

                if balance >= withdraw_user:
                    balance -= withdraw_user
                    print(f"Here is your {withdraw_user} amount")
                    
                else:
                    print("You Have Not Sufficient Balance!")

            elif options == 2:

                deposit_user = int(input("enter your amount to deposit: "))

                if deposit_user <= 0 :
                    print("enter money greater than 0")

                else:
                    balance += deposit_user
                    print(f"You have deopsited {deposit_user} money successfully")

            elif options == 3:
                print(f"Your current balance is {balance}")

            elif options == 0:
                print("\nExiting the atm")
                break

            else:
                print("\nEnter above options")  

    again = input("Do your want to enter to our atm again [Yes][No]: ").lower()

    if again == 'yes':
        atm_card()

    elif again == "no":
        print("Ok no problem!")
    
    else:
        print("enter yes or no")

# calling main function
atm_card()

    

