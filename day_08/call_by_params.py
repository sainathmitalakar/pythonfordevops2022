def check_environment(list_of_env):
    output = ""
    for env in list_of_env:

       if env.lower() == "aws":
        output = "you are in AWS"
       elif env.lower() == "azure":
        output = "you are in AZURE"
       else:
        output = "you are in other env"

    return output
output = check_environment(["digital ocean"])
print(output)