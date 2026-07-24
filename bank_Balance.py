# ATM Withdrawal Program

balance = 10000

amount = int(input("Enter withdrawal amount: "))

if amount > balance:
    print("Invalid")
elif amount % 100 != 0:
    print("Invalid")
else:
    balance = balance - amount
    print("Amount Withdrawn:", amount)
    print("Available Balance:", balance)