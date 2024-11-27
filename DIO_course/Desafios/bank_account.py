'''Create a bank system with the operations: withdraw, deposit and balance.'''

value_withdraw=0
value_deposit= 0
balance = 0
decision = ''
counter = 1

def withdraw(value_withdraw):
    global balance, counter
    if balance < 0 or value_withdraw > 500:
        return print(f'Invalid value, you can"t withdraw more than 500 or your balance is less than zero, your balance is: {balance}')
    elif counter > 2:
        return print("You can't withdraw. You can withdraw only two times a day. Please, back tomorrow.")
    else:
        balance = balance -value_withdraw
        counter = counter + 1
        return print(f'Your balance is: {balance}')



def deposit(value_deposit):
    global balance
    balance = balance + value_deposit
    return print(f'Your balance is: {balance}')

def toSeeBalance():
    return print(f'Your balance is: {balance}')

while decision != 'e':
    print('What do you want to do if withdraw type(w), if deposit(d), if balance(b), if exit(e):')
    decision = input()
    if decision == 'w':
        print('How much do you want to withdraw?')
        w = input()
        withdraw(float(w))
    elif decision == 'd':
        print('How much do you want to deposit?')
        d = input()
        deposit(float(d))
    elif decision == 'b':
        toSeeBalance()
    elif decision == 'e':
        break
    else:
        print('invalid value, type w, d, b or e.')