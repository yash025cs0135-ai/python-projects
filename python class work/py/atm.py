
from datetime import datetime
deposit1 = 0.0
deposit = deposit1
withdrol1 = 0
withdrol = withdrol1
new_balance = 0
new_balance0 = 0
def void_fun ( choise ):
   if(choise == 0 ):
          print('-'* 10,'INFORMATION','-'*10)
          user_name = 'YASH GAUTAM '
          acc_NO = 'xxxxxxxxx746 '
          phone = '********98'
          print('user_name :',user_name)
          print('acc_No:',acc_NO)
          print('phone :',phone)
          print('Deposit :',deposit)
          print('Withdraw :',withdrol)
          print('Current Balance :',new_balance0)
          
           #   Current date and time
          now = datetime.now()
          print("Current Date & Time:", now)
            #  Only date
          print("Date:", now.date())
            #  Only time
          print("Time:", now.time())
           # Formatted date and time
          print("Formatted:", now.strftime("%d-%m-%Y %H:%M:%S"))
      
   




pin1 = 0000
print("="*10,'ATM',"="*10)
pin = int(input('enter the 4 digit pin:'))
if  pin == pin1:
    print('login ! sucessfully ')
    print("="*10,'ATM MENU ',"="*10)
    print('1.ACCOUNT DETAILS \n 2.CHECK BALANCE \n 3.DEPOSIT MONEY \n 4.WITHDRAW MONEY \n 5.MINI STATEMENT \n 6.CHANGE PIN  \n 7.EXIT / LOGOUT ')
    print("enter  the your choice : ")

    choise = int(input('enter the your choise '))

    if (choise == 1 ):
     print('1.ACCOUNT DETAILS ')
     user_name = 'YASH GAUTAM '
     acc_NO = 'xxxxxxxxx746 '
     phone = '********98'
     print('user_name :',user_name)
     print('acc_No:',acc_NO)
     print('phone :',phone)
     choise = int(input(' again   your choise '))
    if (choise == 2):
       print('2.CHECK BALANCE')
       balance = 10000.00
       print(' current amount ',balance)
       choise = int(input(' again your choise '))
    if(choise == 3 ):
      balance = 10000.00
      print('3.DEPOSIT MONEY')
      print(' enter the deposit amount  :')
      deposit = int(input ('enter the deposit amount  :'))
      print("deposit succesfull !")
      print('Deposited', '$',deposit)
      print('new Balance :', balance + deposit)
      new_balance = balance + deposit
      choise = int(input(' again your choise '))
    if(choise == 4):
      withdrol = int(input('enter the withdrol amount '))
      print('withdrol succesfully ')
      print('your withdrol amount is &',withdrol)
     # print('withdraw amount ',new_balance - withdrol )
      print('new_balance :', new_balance - withdrol )
      new_balance0 = new_balance - withdrol 
      choise = int(input(' again your choise '))
    if(choise == 5):
      print('-'*10,'MINI Statement ','-'*10)
      print('Deposit :',deposit)
      print('Withdraw :',withdrol)
      print('Current Balance :',new_balance0)

 #   Current date and time
      now = datetime.now()
      print("Current Date & Time:", now)
  #  Only date
      print("Date:", now.date())
  #  Only time
      print("Time:", now.time())
 # Formatted date and time
      print("Formatted:", now.strftime("%d-%m-%Y %H:%M:%S"))
      choise = int(input(' again your choise '))
    if(choise == 6):
       new_pin = int(input('enter the 4-digits new pin'))
      #  new_pin == pin
       print('your ATM pin is change :')
       print('congratulations sir ')
       pin = int(input('enter the 4 digit pin:'))
       if  pin == new_pin:
        print('login ! sucessfully ')
       else:
           print("wrong password:")
       choise = int(input(' again your choise , 0 '))
       print(void_fun(choise))
    if(choise == 7):
      logout = int(input('for logout enter 1,otherwise  not logout '))
      if(logout == 1  ):
         print('THANKYOU')
         
else :
     print('wrong password ')
