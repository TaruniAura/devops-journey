tools = ["Linux", "Git", "Docker"]
print(tools)
new_tool=input("Enter a new tool: ")
tools.append(new_tool)
print(tools)
remove_tool=input("Enter a tool to remove: ")
if remove_tool in tools:
    tools.remove(remove_tool)
    print("Tool removed successfully.")
else:
    print("Tool not found.")
for tool in tools:
    print(tool)    
