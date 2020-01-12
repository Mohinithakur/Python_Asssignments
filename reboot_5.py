import time

name = input("Enter your name: ")

current_time = int(time.ctime()[-13:-11])
print(current_time)

if (current_time<12):
    print("GOOD MORNING")
if (current_time>12 and current_time<16):
    print("GOOD AFTERNOON")
if(current_time>16):
    print("GOOD NIGHT")
    
