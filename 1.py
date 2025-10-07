"""Enter first name: Mohit
Enter your Pincode: 560001
Enter your height in feet: 5.8
Enter latitude of your address: 12.9757


Here is what you have entered:
First Letter in Name: M
Pincode: 560001
Height: 5.8 ft
Location: 12.9757   77.6053"""
name = input("Enter your first name:")
pin = int(input("Enter your Pincode:"))
height = float(input("Enter Your Height:"))
lat=float(input("Enter latitude & longitude of your address:"))
print("------------------------------------------------------")
print("Here is what you have entered:")
print("Your First Name is :",name)
print("Your Pincode is :",pin)
print("Your Height is:",height)
print("Your address Location is:",lat)


