class Solution:
    
    def findPeakElement(self, nums):
        
        n = len(nums)
        l = 0; h = n - 1
        
        while l < h:
            m = l + (h - l)//2
            if (m == 0 or nums[m] > nums[m - 1]) and (m == n - 1 or nums[m] > nums[m + 1]):
                return m
            elif m >= 0 and nums[m] < nums[m + 1]:
                # move right
                l = m + 1
            elif m <= n - 1 and nums[m] < nums[m - 1]:
                # move left
                h = m - 1
        return l # can return m only when using "l <= h" in while loop
    
if __name__ == "__main__":
    s = Solution()
    print(s.findPeakElement([1]))
    print(s.findPeakElement([1,2]))
    print(s.findPeakElement([2,1]))
    print(s.findPeakElement([1,2,1,3,5,6,4]))
    
"""
Find First and Last Position of Element in Sorted Array

Gotcha: use of l <= r, and duplicated values
"""

class Solution:
    # Use linear search after identifying the element from binary (O(n))
    def searchRange(self, nums, target):
        l = 0; r = len(nums) - 1
        while l <= r:
            m = l + (r - l)//2
            pleft = m; pright = m
            if nums[m] == target: 
                while pleft >= 0 and nums[pleft] == nums[m]:
                    pleft -= 1
                while pright <= len(nums) - 1 and nums[pright] == nums[m]:
                    pright += 1
                return [pleft + 1, pright - 1]
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return [-1, -1]
 
if __name__ == "__main__":
    s = Solution()
    print(s.searchRange([5,7,7,8,8,10], 8))
    print(s.searchRange([1], 1))
    print(s.searchRange([1,2], 3))
    print(s.searchRange([1,1,1,3,3,3,3,3,3,4], 3))
    
# Using binary search on each side (O(log n))
class Solution:
    def searchRange(self, nums, target):
        if nums == None or len(nums) == 0: return [-1, -1]
        l = 0; r = len(nums) - 1
        self.result = [-1, -1]
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                if m == 0 or nums[m] > nums[m - 1]:
                    self.result[0] = m
                    self.result[1] = self.goright(nums, target, m, r)
                    return self.result
                elif m == len(nums) - 1 or nums[m + 1] > nums[m]:
                    self.result[1] = m
                    self.result[0] = self.goleft(nums, target, l, m)
                    return self.result
                else:
                    self.result[0] = self.goleft(nums, target, l, m)
                    self.result[1] = self.goright(nums, target, m, r)
                    return self.result
            elif m == 0 or nums[m] < target:
                l = m + 1
            elif m == len(nums) - 1 or nums[m] > target:
                r = m - 1
        return self.result
            
    def goleft(self, nums, target, l, r):
        while l <= r:
            m  = l + (r - l) // 2
            if nums[m] == target:
                if m == 0 or nums[m - 1] < nums[m]:
                    return m
                else: r = m - 1
            else: l = m + 1
    
    def goright(self, nums, target, l, r):
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                if m == len(nums) - 1 or nums[m] < nums[m + 1]:
                    return m
                else: l = m + 1
            else: r = m - 1

if __name__ == "__main__":
    s = Solution()
    print(s.searchRange([1,1,1,1,1,1], 5))
    print(s.searchRange([5,7,7,8,8,8,8,8,8,10,11], 8))
    print(s.searchRange([1], 1))
    
"""
Check if alphanumeric characters with lower case in a string makes palindrome
Gotcha: use of binary search and ensure lower case characters, 2 pointers solution
"""
    
class Solution:
    def isPalindrome(self, s):
        if s == None or len(s) == 0: return None
        l = 0; r = len(s) - 1
        while l < r:
            if not s[l].isalnum(): l += 1
            elif not s[r].isalnum(): r -= 1
            else:
                if s[l].lower() != s[r].lower(): return False
                else:
                    l += 1
                    r -= 1
        return True
    
if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome("A man, a plan, a canal: Panama"))
    print(s.isPalindrome("race a Car"))
    print(s.isPalindrome("0P"))
    
"""
Find minimum in rotated sorted array:
Gotcha: check the start and end of the array (or partial array) to see which side is sorted
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        r = len(nums) - 1; l = 0
        while l <= r:
            m = l + (r - l) // 2
            if nums[l] < nums[r]: return nums[l]
            if (m == 0 or nums[m] < nums[m - 1]) and (m == len(nums) - 1 or nums[m] < nums[m + 1]):
                return nums[m]
            if nums[m] < nums[r]:
                r = m - 1
            else:
                l = m + 1
                
if __name__ == "__main__":
    s = Solution()
    print(s.findMin([4,5,6,7,0,1,2]))
    print(s.findMin([3,4,5,1,2]))

"""
Find if a given target is present in a given matrix
Gotcha: try to visualize matrix as an array and make use of binary search
"""

class Solution:

    def search2D(self, matrix, target):

        m = len(matrix)
        n = len(matrix[0])

        left = 0; right = m * n - 1

        while left <= right:
            mid = left + (right - left) // 2
            row, col = divmod(mid, n)
            if matrix[row][col] == target: 
                return True
            elif matrix[row][col] > target:
                right = mid - 1 
            else:
                left = mid + 1
        return False
    
if __name__ == "__main__":
    s = Solution()
    print(s.search2D([[1,3,5,7], [10,11,16,20], [23,30,34,60]], 3))
    
"""
Find position of target in a given array with unknown length
Gotcha: move high pointer with 2x speed until we find a number greater than target
"""

"""
This is ArrayReader's API interface.
    class ArrayReader:
        def get(self, index: int) -> int:
You should not implement it, or speculate about its implementation
"""

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        low = 0; high = 1
        if target < reader.get(low): return - 1
        
        while reader.get(high) < target:
            low = high
            high = 2 * low
            
        return self.binarySearch(reader, target, low, high)
            
    def binarySearch(self, reader, target, low, high):
        
        while low <= high:
            mid = low + (high - low) // 2
            if reader.get(mid) == target:
                return mid
            elif reader.get(mid) < target:
                low = mid + 1
            else:
                high = mid - 1
            
        return -1