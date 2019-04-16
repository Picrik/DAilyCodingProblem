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
#Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
#For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
#You can assume that the messages are decodable. For example, '001' is not allowed.

def numberWaysDecode(message):
    message = str(message)
    liste3 = []
    for i in range(len(str(message))):
        if int(message[i]) > 0:
            liste3.append(message[i])
            val = 0
            if i == 0:
                continue
            else:
                val = message[i-1] + message[i]
                if int(val) < 27 and int(val) > 0 and int(message[i-1]) > 0:
                    liste3.append(val)
    return liste3
