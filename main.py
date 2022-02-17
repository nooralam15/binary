#Import library
import math


#create global arrays 
nums = [10, 30, 40, 45, 70, 80, 85, 90, 100];
words = ["at", "ball", "cat", "dog", "eye", "fish", "good"];
unsorted = [30, 20, 70, 40, 50, 100, 90];


#create a function that will search the array using binary search
def binarySearch(array, item):
    #set variables 
    li = 0
    ui = len(array) - 1
    loop = True
    
    while loop:
        mi = math.floor((li + ui)/2)
        if item == array[mi]:
            return mi
        elif item < array[mi]:
            ui = mi - 1
        else:
            li = mi + 1
    return -1


#print results of the linear search function
print(binarySearch(nums, 100))
print(binarySearch(nums, 75))
print(binarySearch(words, "fish"))
print(binarySearch(words, "at"))
print(binarySearch(unsorted, 70))
