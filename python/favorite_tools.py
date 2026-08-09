devops_tools=["Git","Docker","Linux","Python","Terraform"]
print(devops_tools)
print(devops_tools[0])
print(devops_tools[-1])
devops_tools.append("Kubernetes")
print(devops_tools)
devops_tools.remove("Git")
print(devops_tools)
print(len(devops_tools))
for tools in devops_tools:
    print(tools)
