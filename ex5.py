import timeit
import random
import matplotlib.pyplot as plt
import numpy as np

def linear_search(array, x):
    for i in range(len(array)):
        if array[i] == x:
            return i
    return -1 


def binary_search(array, x):
    lo, hi = 0, len(array) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        if array[mid] == x:
            return mid
        elif x < array[mid]:
            hi = mid - 1
        else:
            lo = mid + 1

    return -1

def measure_time(search, array, trials = 1000, number = 100):
    total_time = 0.0
    for i in range(trials):
        x = array[random.randrange(len(array))]
        t = timeit.timeit(lambda: search(array, x), number = number )
        total_time += t/number 
    return total_time/trials


size = np.array([1000, 2000, 4000, 8000, 16000, 32000])

linear_times = []
binary_times = []

for n in size:
    arr= list(range(1, n+1))

    lin_time = measure_time(linear_search, arr, trials=1000, number=100)
    bin_time = measure_time(binary_search, arr, trials=1000, number=100)

    linear_times.append(lin_time)
    binary_times.append(bin_time)

    print(f"n={n:5d} | linear avg = {lin_time:.10f} s | binary avg = {bin_time:.10f} s")

linear_times = np.array(linear_times)
binary_times = np.array(binary_times)

a_lin, b_lin = np.polyfit(size, linear_times, 1)
lin_fit = a_lin * size + b_lin

logn = np.log2(size)
a_bin, b_bin = np.polyfit(logn, binary_times, 1)
bin_fit = a_bin * logn + b_bin

print("\nFitted models:")
print(f"Linear search fit:  t(n) = {a_lin:.3e} * n + {b_lin:.3e}")
print(f"Binary search fit:  t(n) = {a_bin:.3e} * log2(n) + {b_bin:.3e}")

# ---- plotting
# Plot 1: linear search
plt.figure()
plt.scatter(size, linear_times, label="measured")
plt.plot(size, lin_fit, label="linear fit: a*n + b")
plt.xlabel("n (vector size)")
plt.ylabel("avg time per search (s)")
plt.title("Linear Search: measured vs linear fit")
plt.legend()
plt.grid(True)
plt.show()

# Plot 2: binary search
plt.figure()
plt.scatter(size, binary_times, label="measured")
plt.plot(size, bin_fit, label="log fit: a*log2(n) + b")
plt.xlabel("n (vector size)")
plt.ylabel("avg time per search (s)")
plt.title("Binary Search: measured vs log fit")
plt.legend()
plt.grid(True)
plt.show()




# Question 4 

# The linear sort function goes through the array one by one to find what we want so the time complexity
# of the worst case is O(n) while the best case is O(1). - Array can either be sorted or not sorted
# the function we made takes in two inputs the array we want to go through and x - what were looking for
# then we iterate through using a for loop so this justifes the O(n) time complexity 
# Becase the time complexity is O(n) it is linear we model using y = mx+b and the graph that
# is plotted shows the realtionship is very close to linear based on the data we plotted. 

# The binary sort function splits the array into two parts so from 0-hald then half-n and checkas if what we are looking for 
# is bigger then the half value. If it is then goes onto the array half - n. If x is smaller than hald then it checks
# the array 0 - half, and it keeps doing thing until it finds x. For this to work the array needs to be sorted 
# This gives us a time complexity of O(log (base 2) n) as everytie we are splitting the array in half which leads to 
# n/2^k <= 1 steps as at the last step we willl have our anwer so its easy to see that the complexity time 
# is (log (base 2) n). The parameters for this function were the sorted array and x - what we want to find
# When we plot this we can see it clearly that the grapgh closley follows the log curve which is what we expected  






