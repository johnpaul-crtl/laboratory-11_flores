fullname = input("Enter you name here:") #enter you name here
choice = input("type 1 or 2:") # choose 1 or 2 
temperature = float(input("Enter temperature:")) #enter temperature
if choice =="1": # one you entered 1 it will convert celsius to fahrenheit
    celsius = float(input("enter tempeature in celsius:")) #use float for because some of the temperature has decimals
    fahrenheit = (9/5) * celsius + 32 
    print (f"hello, {fullname}! {temperature} celsius is equal to {fahrenheit:2f} degrees fahrenheit.")
    
elif choice =="2": # if you choose fahrenheit to celsius
    fahrenheit = float(input("enter temperature in celsius"))
    celsius = (5/9) * fahrenheit - 32
    print (f"hello, {fullname}! {temperature} celsius is equal to {fahrenheit:2f} degrees celsius.")
else: 
    print("Invalid choice, please 1 or 2") # if you pick above from 1 and 2 it will automatically tell you to enter 1 or 2
   
    