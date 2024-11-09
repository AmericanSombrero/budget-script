# fixed bi-weekly costs
rent = 75.00
car_ins = 30.00
wifi = 25.00
verizon = 10.00
car_payment = 285 # this is bi-weekly

# getting checking account balance
try:
    checking_account = float(input("Enter current amount in checking account: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
    checking_account = 0


# initialize total miscellaneous items
total = rent + car_ins + wifi + verizon + car_payment
misc_total = 0

# Adding payments credit card payments if not already paid
credit_card_total = 0
credit_card_paid = input("Have you paid your credit card minimum (yes/no)").strip().lower()

if credit_card_paid == "no":
    try:
        num_credit_cards = int(input("How many credit cards do you have?: "))
        for i in range(1, num_credit_cards + 1):
            while True:
                try:
                    min_payment = float(input(f"Enter the minimum payment for credit card #{i}: "))
                    credit_card_total += min_payment
                    break
                except ValueError:
                    print("Please enter a valid number.")
    except ValueError:
        print("Invalid Input. No credit cards will be added.")

# add credit card payments to total budget
total += credit_card_total

# adding additional budget items dynamically
while True:
    try:
        misc = input("Enter the amount for an additional budget item if there is one. If not, just type done.: ")

        # check if the user is done
        if misc.lower() == 'done':
            break

        # convert the input to a number and add the misc_total
        misc_total += float(misc)
    except ValueError:
        print("Please enter a valid number or type 'done'. ")

# add miscellaneous total to the fixed budget items
total += misc_total

# calculate remaining balance
remaining_balance = checking_account - total

# print results

print("\nBUDGET BREAKDOWN:")
print(f"Rent: ${rent:.2f}")
print(f"Car Insurance: ${car_ins:.2f}")
print(f"Wifi: $ {wifi:.2f}")
print(f"Verizon Bill: ${verizon:.2f}")
print(f"Bi-Weekly Car Payment Amount: ${car_payment:.2f}")
if credit_card_total > 0:
    print(f"Credit card minimum payments: ${credit_card_total:.2f}")
print(f"Additional Expenses Miscellaneous: ${misc_total:.2f}")
print(f"Total Expenses: ${total:.2f}")
print(f"Payback amount taken out: ${total:.2f}")
print(f"Reamining balance in checking account: ${remaining_balance:.2f}")