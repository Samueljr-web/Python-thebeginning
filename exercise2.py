#currency converter program

currency_type = input("Convert to USD or GBP?: ")

usd_1 = 1444 
gbp_1 = 1900

if currency_type.upper() == "USD":
    dollar_amount = int(input("Enter dollar amount: "))
else:
    pounds_amount = int(input("Enter pound amount: "))

if currency_type.upper() == "USD":
    converted = dollar_amount * usd_1
    print("Converted: " + str(converted))
    