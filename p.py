print("="*50)
print('smartcampus automated pass & tariff calculator')
print('='*50)
print("1.student \n 2.faculty / staff")
category = int(input(' enter the choise : '))
if(category == 1):
   print('you selected : student ')


   sub_catagroy  = input('enter sub catagroy (ug /pg) ').lower()
   if sub_catagroy == "ug":
        base_fee = 500
        print("base_fee : ₹500")
   elif sub_catagroy == "pg":
        base_fee = 350
        print("base_fee : ₹350")
   else:
        print('invalid sub_catagroy : [Error]')
        exit()
   cgpa = float(input("Enter Student CGPA (0.0 - 10.0)"))
   if cgpa < 0 or cgpa > 10:
        print("[ERROR]: CGPA must be between 0.0 and 10.0")
        exit()

   elif cgpa >= 8.5:
        discount = base_fee * 0.20

   elif cgpa >= 7.5:
        discount = base_fee * 0.10

   else:
        discount = 0


    

elif (category == 2):
      print("you selected : faculty / staff ") 


      sub_catagroy  = input("Enter Sub-Category (Resident / Visiting) ").lower()
      if sub_catagroy == "resident":
        base_fee = 800
        print("base_fee : ₹800")
      elif sub_catagroy == "visiting":
        base_fee = 1200
        print("base_fee : ₹1200")
      else:
        print('invalid sub_catagroy : [Error]')
        exit()


      years = int(input("Enter Years of Service: "))

      if years < 0:
        print("[ERROR]: Years of Service cannot be negative")
        exit()

      elif years > 10:
        discount = base_fee * 0.15

      else:
        discount = 0

else:
         print("[ERROR]: Invalid User Category")
         exit()


net_fee = base_fee - discount

print("\nBase Fee:", base_fee)
print("Discount:", discount)

print("Net Fee:", net_fee)
# --------parking-------
parking = int(input('\n select parking permit : (0: none , 2: Two - wheeler , 4: Four - wheeler ): '))
if parking == 0:
    parking_fee = 0
    peak_surcharge = 0
elif parking ==2: 
    parking_fee = 200
    peak_surcharge = 0
elif parking ==4 :
    parking_fee =400

    if category ==1:
        peak_surcharge =150
    else:
        peak_surcharge = 0
else:
    print("[error]: Invalid parking option ")
    exit()

pass_parking_total = net_fee + parking_fee +peak_surcharge
print("\n Parking fee :", parking_fee)
print("\n peak surcharge :",peak_surcharge)
print("pass & parking  total : ", pass_parking_total)

#  ---------Electricity bill----------



units = float(input("\n Enter monthly electricity consumption (in Kwh): "))
if units < 0:
    print("[error]: electricity units can not be negative :")
    exit()
elif units <= 100:
    electricity_bill = units *3
    fixed_charge = 50
elif units<=300:
    electricity_bill = (100 * 3 ) +((units - 100) *5)
    fixed_charge = 100
elif units <= 500:
    electricity_bill = (100*3) + (200 *5 ) + ((units-300)*7.5)
    fixed_charge = 150
else :
    electricity_bill = (100*3)+ (200*5) + (200 * 7.5) + ((units - 500)*10)
    fixed_charge = 250


electricity_total = electricity_bill + fixed_charge
print("\n Electricity Bill : ",electricity_bill)
print("\n Fixed charge :", fixed_charge)
print("Electricity Total :",electricity_total)



#  ----- final Total ----  
total_monthly_paybal = pass_parking_total + electricity_total
print("\n" + "=" *60 )
print("             CALCULATED INVOICE BREAKDOWN ")
print("-" *60)
print(f"Base Access pass fee    : {base_fee:.2f}")
print(f" Discount               : {discount:.2f}")
print(f"parking fee             : { parking_fee:.2f}")
print(f"peak surcharge          : {peak_surcharge:.2f}")
print(f"Net pass & parking total: {pass_parking_total:.2f}")

print("-"*60)

print(f"Electricity Bill ({units:.0f}kwh) :  {electricity_total:.2f}")

print("-"*60)

print(f"TOTAL MONTHLY PAYBAL     : {total_monthly_paybal:.2F}")

print("-"*60)
