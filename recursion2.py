def factorial(number):    
    if number>1:
        return number*factorial(number-1)
    return number
    
print(factorial(11))
