#1
#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

def findingKSum(liste, k):
    for i in range(len(liste)):
        if i == len(liste)-1:
            return False
            break
        for j in range(i, len(liste)):
            if liste[i] + liste[j] == k:
                return True

#2
#Given an array of integers, return a new array such that each element at index i of the new 
#array is the product of all the numbers in the original array except the one at i.

def multiplicationArrayWDIV(Arr):
    newArray = []
    val = 1
    for num in Arr:
        val *= num
    for item in Arr:
        newArray.append(int(val/item))
    return newArray

def multiplicationArrayWODIV(Arr):
    newArray = []
    for item in Arr:
        val = 1
        for num in Arr:
            if num == item:
                continue
            val *= num
        newArray.append(val)
    return newArray
    
