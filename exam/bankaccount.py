# Bank System:

# 1.create account
# 2.Deposit
# 3.Withdraw
# 4.Exit

# თქვენი დავალება იქნება გააკეთოთ ბანკის სისტემა მოცემული სექციებით პითონში,რაც აქამდე ისწავლეთ გააკეთეთ იმ მასალით გამოიყენეთ თქვენი მაქსიმალური ცოდნა,მერე კი ჩვენ შევამოწმეთ თუ რა დონის ცოდნა გამოიყენეთ და იმის მიხედვით შეიგიმოწმებთ!!!

   # creating an account for a bank

def account_created():
    while True:
        account_name = input('write your name for your account: ')    # creating nick name for account
        sur_name = input('write you surname for your account: ')

        
        print('your nickname created ! ! ', account_name, sur_name)

        correct_password = input('correct password for an account: ')    # creating password for account         
        your_password = input('enter your password for an account: ')

        if correct_password == your_password:
            print('well, this password is supported for account')
            break                                                          # checking password
        else:
            print('try again and write new password')


        print('account created ! !')     # account creted


account_created()

    # deliting money to our bank account

def delit_money():
    while True:
        delit_money = int(input('how much money do you want to deposit? (max - 1000000): '))   # deliting money

        if delit_money > 1000000:
            print('you want to delite a lot of money.')    # checking how much money did we delited
        else:
            print('money was deposited ! !')
            print('money was deposited in bank ! !')    # money was delited
            break
delit_money()

    # withdrawing money from our bank account 

def withdraw_money():
    while True:

        withdraw_money = int(input('how much money do you want to withdraw ?(max - 250000): ')) # withdrawing money

        if withdraw_money > 250000:
            print('you want to withdrow a lot of money.')   # checking how much money did we withdrawed
        else:
            print('money was withdrawed ! !')
            print('money was withdrowed from bank ! !')# money was withdrawed
            break

withdraw_money()


def exit():
    while True:
      exit = input('do you want to exit from bank? ')  # do we want to exit or no
      exited = 'yes'

      if exit != exited:
        print('okay. also, what can we do for you ?')   # asking what can we do more
        balance = 'how much money do i have ? '
        print(balance, ' - ' , 'your balance is', delit_money, '$')
        withdraw = 'how much money did i withdrawed ?'
        print(withdraw , '-', 'you withdrawed', withdraw_money, '$')
      else:
        print('bye bye, good luck ! !')  # exiting from the bank and say bye
        break
      
# the end
      
exit()
