"""tools = ["Linux", "Git", "Docker", "Kubernetes", "Terraform"]
def check_tool(tool):
    if tool in tools:
        print(tool," is installed")
    else:
        print(tool," is not installed")
tool=input("Enter a tool: ") 
check_tool(tool) 

tools = ["Linux", "Git", "Docker", "Kubernetes", "Terraform"]
def check_tool(tool):
    return tool in tools

tool=input("Enter a tool: ")

if check_tool(tool):
    print(f"{tool} is installed.")
else:
    print(f"{tool} is not installed.") """

tools = {"Linux", "Git", "Docker", "Kubernetes", "Terraform"}

def check_tool(tool):
    if tool in tools:
        return True
    return False

tool = input("Enter a tool: ")

if check_tool(tool):
    print(f"{tool} is installed.")
else:
    print(f"{tool} is not installed.")   