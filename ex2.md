# Exercise 2 – Interpolation Search

## Question 1
**Mention at least two aspects that make interpolation search better than binary search**

- Interpolation search can be faster than binary search when the data is **uniformly distributed**, achieving an average time complexity of **O(log log n)** compared to binary search’s **O(log n)**.
- Instead of always checking the middle element, interpolation search **estimates the likely position** of the target value, which often reduces the number of comparisons.

---

## Question 2
**Interpolation search assumes that data is uniformly distributed. What happens if the data follows a different distribution? Will the performance be affected? Why?**

Yes, the performance will be negatively affected.

Interpolation search estimates the position of the target based on the assumption that values are evenly spaced. If the data is **non-uniformly distributed** (e.g., clustered or skewed), the estimated position will be inaccurate. This can cause the algorithm to make poor jumps and potentially degrade its performance to **O(n)** in the worst case, similar to linear search.

---

## Question 3
**If we wanted to modify interpolation search to follow a different distribution, which part of the code would be affected?**

The position calculation would be affected:


pos = low + int(((float(high - low) / (arr[high] - arr[low])) * (x - arr[low])))

## Exercise 2 /2

### Question 4
**When is linear search your only option for searching data as binary and interpolation search may fail?**

Linear search is the only option when the data is **unsorted**.

Binary search and interpolation search both require the data to be sorted. If the data is not sorted, these algorithms may return incorrect results or fail, while linear search still works correctly.

---

### Question 5
**In which case will linear search outperform both binary and interpolation search, and why?**

Linear search can outperform both binary and interpolation search when the dataset is **very small** or when the target element is **near the beginning** of the data.

In these cases, linear search may find the element immediately, while binary and interpolation search incur additional overhead from calculations and comparisons.

---

### Question 6
**Is there a way to improve binary and interpolation search to solve this issue?**

Yes.

- The data can be **sorted in advance**, allowing binary or interpolation search to be used.
- Hybrid approaches can be applied, such as switching to linear search for small datasets.
- Alternative data structures like **hash tables** can be used to achieve average **O(1)** search time without requiring sorted data.
