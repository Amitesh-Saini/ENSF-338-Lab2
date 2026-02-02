#1. What does this code do?
#Ans: Its a Fibonacci code and it outputs the nth Fibonacci number.

#2. Is this an example of a divide-and-conquer algorithm (think carefully about this one)? 
#Ans: Yes

#3. Give an expression for the time complexity of the algorithm
#Ans: O(2^n)





def func(n):
    if n == 0 or n == 1:    
        return n
    else:
        return func(n-1) + func(n-2)
    

print(func(7))
