from usage_calc import vaildate_usage_value, calculate_bill
while True:
    number_customer = input("Please Enter the Number of Customers ")
    try:
        number_customer = int(number_customer)
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

while number_customer > 0:
    
    while True:
        usage_in_m3 = input("Please Enter The Water Usage in m3... ")
        try:
            usage_in_m3 = float(usage_in_m3)
            break
        except Exception as e: 
            print(f"Please Enter Thee Water Consmptions ")
    number_customer -= 1
    bill_amount = calculate_bill(usage_in_m3)
    print(f"The customer consmption is {bill_amount}")