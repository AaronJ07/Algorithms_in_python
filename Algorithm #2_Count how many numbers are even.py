#// © [Penguin], [2025]. All rights reserved. //
# Algorithm #2: Count how many numbers are even
#The output should be 2

nums = [4, 7, 1, 9, 3, 10]

def count_even_(num):
    count = 0
    for n in nums:
        if n % 2 == 0:
            count = count + 1   # Also can write in term of count += 1
    return count

print(count_even_(nums))
