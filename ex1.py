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
    

#4. Implement a version of the code which uses memoization to improve performance

def func_memo(n, memo=None):
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n == 0 or n == 1:
        memo[n] = n
    else:
        memo[n] = func_memo(n - 1, memo) + func_memo(n - 2, memo)

    return memo[n]

#5. Give an expression for the time complexity of the optimized algorithm
# The time complexity of the memoized algorithm is O(n),
# because each Fibonacci value is computed only once.

#6.

import time
import matplotlib.pyplot as plt

n_values = list(range(36))
times_original = []
times_memo = []

plt.figure()
plt.plot(n_values, times_original)
plt.xlabel("n")
plt.ylabel("Time (seconds)")
plt.title("Naive Recursive Fibonacci Timing")
plt.savefig("ex1.6.1.jpg")

# Plot memoized function timings
plt.figure()
plt.plot(n_values, times_memo)
plt.xlabel("n")
plt.ylabel("Time (seconds)")
plt.title("Memoized Fibonacci Timing")
plt.savefig("ex1.6.2.jpg")

