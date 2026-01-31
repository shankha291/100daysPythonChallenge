print("Welcome to the tip calculator!")
bill_amt=float(input("What was the total bill:$"))
tip=int(input("How much tip would you like to give:(10,12 or 15)::"))#Because input takes it as str
count=int(input("How many people to split the bill:"))
total_amt=bill_amt+bill_amt*(tip/100)
each_pay=round(total_amt/count,2)
print(f"Each person should pay:${each_pay}")
