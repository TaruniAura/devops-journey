""""
#functions without parameters
def say_hello():
    print("Hello ,Devops!")

say_hello()    

#functions with parameter
def greet(name):
    print("Hello",name)

greet("Rama")
greet("Krishna") 

#functions with Multiple parameter
def introduce(name,city):
    print("My name is",name)
    print("I live in",city)

introduce("Tom","Venice")   

#functions with return value
def add(a,b):
    return a+b

result=add(1,9)

print(result) """

#function with if
def check_number(number):
    if number>0:
        return "Positive"
    elif number<0:
        return "Negative"
    else:
        return "Zero"

result=check_number(10)
print(result)

