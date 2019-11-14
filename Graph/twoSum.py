# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 15:38:27 2019

@author: xiaoy
"""
import time

file = open('twoSum_input.txt', 'r')
data = file.readlines()
nums = {}
for num in data:
    nums[int(num)] = 1



cnt = 0
start = time.time()
for t in range(-10000, 10001):
    for key in nums.keys():
        a = t - key
        if a in nums:
            cnt += 1
            break
end = time.time()

print(end-start)
print(cnt)