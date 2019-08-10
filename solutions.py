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

#3
# Given an array of integers, find the first missing positive integer in linear time and constant space.
#In other words, find the lowest positive integer that does not exist in the array.
#The array can contain duplicates and negative numbers as well.

def findFirstMissing(liste):
    liste.sort()
    anVal = liste[0]
    for i in range(len(liste)):
        newVal = liste[i]
        if (anVal + 1) == newVal or anVal == newVal:
            anVal = newVal
        else:
            if anVal > 0:
                return anVal
            else:
                return 0
            break

#4
#Given a list of integers, write a function that returns the largest sum of non-adjacent numbers.
#Numbers can be 0 or negative.
#For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5]
#should return 10, since we pick 5 and 5.

def sumNonAdj(liste):
    val = min(liste)
    for i in range(len(liste)):
        for j in range(i+2,len(liste)):
            if val < (liste[i] + liste[j]):
                val = liste[i] + liste[j]
    return val

#5
#Given a singly linked list and an integer k, remove the kth last element from the list.
#k is guaranteed to be smaller than the length of the list.
#The list is very long, so making more than one pass is prohibitively expensive.
#Do this in constant space and in one pass.

def returnFirst(Liste, k):
    return Liste[:-k]
