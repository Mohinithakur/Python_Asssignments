#!/usr/bin/python3

#importing the required package
import datetime
name = input("enter your name: ")
age = int(input("Enter your age: "))

#taking user input,which age they want to get prediction for.
desired_age =int(input("Enter your age for prediction: "))

#the current time of age.
current_time = datetime.datetime.now()
print (current_time)


#calculate the predicted year.
cal = (desired_age-age)+current_time.year

print("{} you will turn {} by the year : {}".format(name,desired_age,cal))
