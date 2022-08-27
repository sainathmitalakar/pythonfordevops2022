"""
This  script checks if
MY Cloud Environment is Amongdt Following 
- AWS
- Azure
- GCP

"""

cloud_env = input("Enter  Cloud Envirnment:")
service = input("Enter a service:")
print(dir(cloud_env.lower.__doc__))
if cloud_env.lower =="AWS":
    if service == "ec2":
     print("You are in AWS")
    else:
        print("you are in AWS but in another service")

elif cloud_env.lower =="Azure":
    print("You are in Azure")

elif cloud_env.lower =="GCP":
    print("You are in GCP")
else:
    print("you are not using any cloud services")


