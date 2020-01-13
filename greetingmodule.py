#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time,pyttsx3
def calling_name():
    name = input("Enter your name: ")
    eee = pyttsx3.init()
    eee.say(name)
    eee.runAndWait()
    
def greeting():
    current_time = int(time.ctime()[-13:-11])
    print(current_time)
    if (current_time<12):
        print("GOOD MORNING")
    elif (current_time>=12 and current_time<16):
        print("GOOD AFTERNOON")
    elif(current_time>=16 and current_time<=18):
        print("GOOD Evening")
    elif(current_time>18):
        print("GOOD NIGHT")
        
calling_name()
#currenttime()
greeting()


# In[ ]:





# In[ ]:





# In[ ]:




