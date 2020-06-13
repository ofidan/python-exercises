import time

"""localtime"""

hour = input("Hour: ")
minute = input("Minute: ")

while True:
    lc = time.localtime(time.time())
    
    if hour == lc.tm_hour and minute ==lc.tm_min:  
        print ("Alarm caldi!\nSaat ", lc.tm_hour, ":", lc.tm_min)
        break
    else:
        pass

print("Donguden cikildi!")