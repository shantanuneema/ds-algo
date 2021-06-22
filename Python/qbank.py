"""
You're given a list of n integers arr[0..(n-1)]. You must compute a list output[0..(n-1)] such that, for each index i (between 0 and n-1, inclusive), output[i] is equal to the median of the elements arr[0..i] (rounded down to the nearest integer).
The median of a list of integers is defined as follows. If the integers were to be sorted, then:
If there are an odd number of integers, then the median is equal to the middle integer in the sorted order.
Otherwise, if there are an even number of integers, then the median is equal to the average of the two middle-most integers in the sorted order.
"""

def findMedian(arr):
  # Write your code here
    n = len(arr)
    hashSet = set()
    result = []
    for i in range(n):
        hashSet.add(arr[i])
        hlen = len(hashSet)
        sortedList = list(hashSet)
        if (i + 1) % 2 == 0:
            median = (sortedList[hlen // 2 - 1] + sortedList[hlen // 2]) // 2
        else:
            median = sortedList[hlen // 2]
        result.append(median)
    
    return result

print(findMedian([5, 15, 1, 3]))
print(findMedian([2, 4, 7, 1, 5, 3]))
      
"""
You're given a list of n integers arr[0..(n-1)]. You must compute a list output[0..(n-1)] such that, for each index i (between 0 and n-1, inclusive), output[i] is equal to the product of the three largest elements out of arr[0..i] (or equal to -1 if i < 2, as arr[0..i] then includes fewer than three elements).
Note that the three largest elements used to form any product may have the same values as one another, but they must be at different indices in arr.
"""
      
def findMaxProduct(arr):
  # Write your code here
    aset = set(arr[0:3])
    product = 1
    for item in aset:
        product *= item
    result = [-1, -1, product]
    for num in arr[3: ]:
        if num > min(aset):
            product = 1
            aset.pop()
            aset.add(num)
            for item in aset:
                product *= item
        result.append(product)
    return result
      
print(findMaxProduct([1,2,3,4,5]))

"""
You have N bags of candy. The ith bag contains arr[i] pieces of candy, and each of the bags is magical!
It takes you 1 minute to eat all of the pieces of candy in a bag (irrespective of how many pieces of candy are inside), and as soon as you finish, the bag mysteriously refills. If there were x pieces of candy in the bag at the beginning of the minute, then after you've finished you'll find that floor(x/2) pieces are now inside.
You have k minutes to eat as much candy as possible. How many pieces of candy can you eat?
"""

from heapq import heappush, heappop
def maxCandies(arr, k):
    maxHeap = []; total_candies = 0
    for num in arr:
        heappush(maxHeap, -1 * num)

    # get largest
    for __ in range(k):
        candies = heappop(maxHeap)
        heappush(maxHeap, candies // 2 + 1)
        total_candies += candies

    return -1 * total_candies

print(maxCandies([2, 1, 7, 4, 2], 3))