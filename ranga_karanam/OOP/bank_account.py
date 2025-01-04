from dates_bank_account import Account

account = Account(1000)
quest = ' '
while True:
    quest = input("Put sold, withdraw, deposit or exit.")
    if quest == 'sold':
        account.show_sold()
    elif quest == 'withdraw':
        account.withdraw()
    elif quest == 'deposit':
        account.deposit()
    elif quest == 'exit':
        break
    else:
        print('Invalid value.')








