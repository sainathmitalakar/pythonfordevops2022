cloud_env = ["AWS" , "GCP", "AZURE"]

try:
    print(cloud_env[200])

except:
       print("exception handle")
finally:
       print("I will excute anyways")
print("this code should run")



try:
    a=10
    b=0
    c=a/b
except ZeroDivisionError as e:
    print(e)

