# Questions:


# Question 1: What is a profiler, and what does it do?

# A profiler is a set of statistics that dscribes how often and how long
# parts of a program are executed. It is useful to find bottlenecks,
# which parts need to be optimized and which dont etc



# Question 2: How does profiling differs from benchmarking?

# Benchmarking is for the overall program execution meaning how fast it runs all together which is 
# useful in comparing different algoirthms programs etc. Profiling is why is the program slow or 
# ineeficent in the same program it shows which parts are slow which are fast. 


# Question 3: Use a profiler to measure execution time of the program (skip function definitions)

import cProfile
import pstats



import timeit

def sub_function(n):
    #sub function that calculates the factorial of n
    if n == 0:
        return 1
    else:
        return n * sub_function(n-1)
    

def test_function():
    data = []
    for i in range(10):
        data.append(sub_function(i))
    return data



def third_function():
    # third function that calculates the square of the numbers from 0 to 999
    return [i**2 for i in range(100000000)]


pr = cProfile.Profile()
pr.enable()



test_function()
third_function()

pr.disable()

pstats.Stats(pr).sort_stats("cumulative").print_stats(30)



# Question 4: Discuss a sample output. Where does execution time go?


# Output:
#         68 function calls (23 primitive calls) in 4.016 seconds
#
#  Ordered by: cumulative time
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    4.015    4.015    4.015    4.015 /Users/amiteshsaini/Desktop/ENSF-338-Lab2/ex3.py:44(third_function)
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        1    0.000    0.000    0.000    0.000 /Users/amiteshsaini/Desktop/ENSF-338-Lab2/ex3.py:36(test_function)
#    55/10    0.000    0.000    0.000    0.000 /Users/amiteshsaini/Desktop/ENSF-338-Lab2/ex3.py:28(sub_function)
#       10    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects} 

  # Before approaching this looking at the functions it is clear that Third_function will take the 
  # most anount of time as it is looping 100000000 times and computing those many squares which is 
  # an enormous amount of calculations. Test_function in comparison only loops 10 times ppending the
  # element to the list, so we can expet the time for this function to be next to 0. We can see 
  # both of these hypotheses are true as the cum time for third_function was 4.015 seconds and the total
  # time for all function calls was 4.016 seconds which is very close to 4.015 seconds, meaning the time 
  # spent on the test_function was around 0.001 seconds which is incredibaly small 


