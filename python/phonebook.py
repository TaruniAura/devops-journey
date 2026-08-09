name=input("Enter the name : ")
phone_number=input("Enter the phone number : ")
city=input("Enter the City : ")

contact={
    "name":name,
    "phone_number":phone_number,
    "city":city
}

print("------Contact-----")
print("Name : ",contact["name"])
print("Phone : ",contact["phone_number"])
print("City : ",contact["city"])
