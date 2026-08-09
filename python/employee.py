employee = {
    "name": "Mahesh",
    "role": "DevOps Engineer",
    "experience": 2,
    "city": "Sans Francisco"
}

print(employee)

print(employee["name"])

print(employee["role"])

employee["company"]="Google"

employee["city"]="Bengaluru"

employee.pop("experience")

for key,value in employee.items():
    print(key,":",value)