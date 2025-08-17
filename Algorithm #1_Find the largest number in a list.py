#// © [Penguin], [2025]. All rights reserved. //
# Algorithm #1: Find the largest number in a list
#The output should be 8

arr_numbers = [3, 5, 7, 2, 8]

def largest_number(num):
    largest = num[0]
    for arr_number in num:
        if arr_number > largest:
            largest = arr_number
    return largest

print(largest_number(arr_numbers)) 
