# // © [Penguin], [2025]. All rights reserved. //
# Algorithm_Self_Do_Question/Question_1.py
# The solution state of this question is just a example.

arr = [4, 9, 9, 8, 3]

def sort_number(arr):
    max_element = arr[0]  
    max_index = 0       

    for i in range(1, len(arr)):
        if arr[i] > max_element:    
            max_element = arr[i]    
            max_index = i    

    if max_index != 0:
        arr[0], arr[max_index] = arr[max_index], arr[0]      
        return arr  

print(sort_number(arr))