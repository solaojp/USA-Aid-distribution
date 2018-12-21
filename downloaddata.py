#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 15:14:57 2018

@author: GD
"""
from urllib import request

# Retrieve the webpage as a string
response = request.urlopen("https://explorer.usaid.gov/data.html")
csv = response.read()

# Save the string to a file
csvstr = str(csv).strip("b'")

lines = csvstr.split("\\n")
f = open("us_foreign_aid_complete.csv", "w")
for line in lines:
   f.write(line + "\n")
f.close()