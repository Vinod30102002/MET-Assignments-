 
print("####### ELECTRICITY BILL CALCULATOR #######")

total_bill = 0

rate_per_unit = 0
 
units = int(input("Enter units consumed: "))

user_type = input('Enter user type (residential / commercail): ')

billing_time = input("Enter time of billing  (peak/off-peak): ")
 
if user_type == "residential":

    if units > 0 and units <= 100:

        rate_per_unit = 3

    elif units > 100 and units <= 300:

        rate_per_unit = 5

    elif units > 300:

        rate_per_unit = 7

else:

    if units > 0 and units <= 100:

        rate_per_unit = 6

    elif units > 100 and units <= 300:

        rate_per_unit = 8

    elif units > 300:

        rate_per_unit = 10
 
 
base_bill = units * rate_per_unit
 
if billing_time == "peak":

    total_bill = base_bill + 5

else:

    total_bill = base_bill
 
 
print(f'''

   ####### YOUR TOTAL BILL #######

   Your Connection Type: {user_type}

   Total Units Consumed: {units}

   Your Rate Per Unit: {rate_per_unit}

   Total Base Price: {base_bill}

   -----------------------------------

   Total Bill: {total_bill}

   -----------------------------------

''')
 