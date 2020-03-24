# -*- coding: utf-8 -*-
import sys

import pandas

import time
import datetime
import csv



path = "D:/User/Desktop/Insta/Posts.xlsx"

df = pandas.read_excel(path)


print(df.columns)

for index, row in df.iterrows():
    print(index,row,row['Name '])