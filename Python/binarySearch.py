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
    # Use binary search
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