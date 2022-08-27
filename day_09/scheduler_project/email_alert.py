import shutil
import time

print("used % ",used_per)
print("free % ",free_per)
while True:
    total,used,free = shutil.disk_usage("/")

    used_per = (used / total)*100
    free_per = (free / total)*100

    if free_per < 15 :
      print("email alret sent")