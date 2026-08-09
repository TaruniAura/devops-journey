tools = ["Linux","Git","Docker","Python"]
print(tools)
print(tools[0])
print(tools[1])
print(tools[-1])
tools.append("Terraform")
print(tools)
tools.remove("Git")
print(tools)
tools[1]="Git"
print(tools)
print(len(tools))
#Loops
for tool in tools:
    print(tool)
