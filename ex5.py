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







