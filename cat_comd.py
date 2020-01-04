#!/usr/bin/env python

#to create a new file just like cat command in linux
import subprocess
filename = input("enter file name: ")

try:
    
    file = open(filename)
    
except FileNotFoundError:
    file =open(filename,'w+')
    file=file.write(input())
    
   
file_read = open(filename,'r')

file_read = file_read.read()
print(file_read)



