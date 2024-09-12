import time
import os

my_time = int(input("Enter the time in seconds: "))
for x in range(my_time, 0, -1):
    os.system("CLS")  # Clear screen based on OS
    seconds = x % 60
    minutes = (x // 60) % 60
    hours = x // 3600
    print(f"{hours:02} : {minutes:02} : {seconds:02}")
    time.sleep(1)

print("Time's Up.......")
