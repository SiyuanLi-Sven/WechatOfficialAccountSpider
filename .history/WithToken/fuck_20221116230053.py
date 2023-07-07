import os
import pandas as pd


lis_fakeid = []
lis_appmsg_token = []
lis_cookie = []

lines = open(r'WithToken\filter.txt').readlines()
count = 0
for line in lines:
    count += 1
    if count == 1:
        print(count)

    if line == '\n':
        print("################")
        count = 0