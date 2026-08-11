"""
#Read a file
file = open("sample.txt", "r")

content = file.read()

print(content)

file.close()

#Better approach — with open()
with open("sample.txt","r") as file:
    content=file.read()

print(content)   """

#Read line by line
with open("sample.txt","r") as file:
    for line in file:
        print(line.strip())

#readlines()
with open("sample.txt","r") as file:
    lines=file.readlines()

print(lines)    