#weight converter program

weight = int(input("Weight: "))

weight_type = input("(K)g or (L)bs: ")

if weight_type.upper() ==  "K":
    converted = weight / 0.45
    print("Weight in kg: " + str(converted))
else: 
    converted = weight * 0.45
    print("Weight in Lb's: " + str(converted))