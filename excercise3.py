# write a python program that uses a while loop to repeatedly prompt a user 
# to enter a number unitl they enter a negative number


input = int(input("Enter a number:"))
def PromptInput():
    while input >= 0:
      input


i = 0 #a positive number


if (input):
  if("-" in str(input)):
     print("correct... you entered: " + str(input)  ) 
  else:
    print("number must be negative")

else:
   print("input must contain a value")     

 

PromptInput()