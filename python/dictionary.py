trip = {
    "place": "Kerala",
    "transport": "Train",
    "days": "5",
    "budget":"15"
}

print(trip)

print(trip["budget"])
print(trip["place"])

trip["month"]="October"
print(trip)

trip["days"]=6

trip.pop("transport")

print(trip)

for key,value in trip.items():
    print(key, ":" ,value)

if "place" in trip:
    print("Place found")
else:
    print("Place not found")

        
