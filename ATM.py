print("1: user 1")
print("2: user 2")
print("3: user 3")
user_num = int(input('Enter the user number: '))

if user_num == 1:
  card_num = int(input("Enter the card number: "))
  pin = int(input("Enter the pin of the card: "))
  if card_num == 1234 and pin == 6767:
    print("1. Bank balance")
    print("2. withdraw")
    option = int(input("Enter the option: "))
    if option == 1:
      print("your bank balance is 5000")
    elif option == 2:
      print("Withdrawal ")
      withdraw_amount = int(input("Enter the amount to withdraw: "))
      if withdraw_amount <= 5000:
        print("Withdrawal successful.")
      else:
        print("insuficient balance")
    else:
      print("Invalid option.")
  else:
    print("Invalid card number or pin for user 1.")

elif user_num == 2:
  card_num = int(input("Enter the card number: "))
  pin = int(input("Enter the pin of the card: "))
  if card_num == 6234 and pin == 1234:
    print("1. Bank balance")
    print("2. withdraw")
    option = int(input("Enter the option: "))
    if option == 1:
      print("your bank balance is 10000")
    elif option == 2:
      print("Withdrawal ")
      withdraw_amount = int(input("Enter the amount to withdraw: "))
      if withdraw_amount <= 10000:
        print("Withdrawal successful.")
      else:
        print("insuficient balance")
    else:
      print("Invalid option.")
  else:
    print("Invalid card number or pin for user 2.")

elif user_num == 3:
  card_num = int(input("Enter the card number: "))
  pin = int(input("Enter the pin of the card: "))
  if card_num == 8891 and pin == 3636:
    print("1. Bank balance")
    print("2. withdraw")
    option = int(input("Enter the option: "))
    if option == 1:
      print("your bank balance is 15000")
    elif option == 2:
      print("Withdrawal ")
      withdraw_amount = int(input("Enter the amount to withdraw: "))
      if withdraw_amount <= 15000:
        print("Withdrawal successful.")
      else:
        print("insuficient balance")
    else:
      print("Invalid option.")
  else:
    print("Invalid card number or pin for user 3.")

else:
  print("Invalid user number.")