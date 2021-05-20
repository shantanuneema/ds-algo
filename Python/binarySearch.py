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
    
"""
Check if alphanumeric characters with lower case in a string makes palindrome
Gotcha: use of binary search and ensure lower case characters
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
check if a integer is palindrome (without converting to a string)
Gotcha: use simple airthmatic by finding reverse of the number
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev_num = 0
        chk_num = x
        while chk_num > 0:
            remainder = chk_num % 10
            rev_num = rev_num * 10 + remainder
            chk_num = chk_num // 10

        if rev_num == x: return True
        return False



    