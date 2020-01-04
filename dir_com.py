#!/usr/bin/env python
# coding: utf-8

#neccessary pacakage to list the directory.
import os

#Taking user input  
loc = input("enter the directory u want to list: ")

#generating the list of item in a directory
gen_list = os.listdir(loc)
print(gen_list)





