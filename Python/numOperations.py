"""
check if a integer is palindrome (without converting to a string)
Gotcha: use simple airthmatic by finding reverse of the number
"""
class Solution:
    def isPalindrome(self, x):
        rev_num = 0
        chk_num = x
        while chk_num > 0:
            remainder = chk_num % 10
            rev_num = rev_num * 10 + remainder
            chk_num = chk_num // 10

        if rev_num == x: return True
        return False

if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome(1221))
    print(s.isPalindrome(-121))
    
"""
reverse an integer, ensure values out of max and min allowed range returns 0
gotcha: carefully take care of -ve sign in reversing as well as conditional statement before returning
"""

class Solution:
    def reverse(self, x):
        if x == None: return
        ifneg = True if x < 0 else False
        
        y = abs(x)
        rev_num = 0
        while y > 0:
            y, remainder = divmod(y, 10)
            rev_num = rev_num * 10 + remainder
            
        if ifneg and rev_num < 2**31:
            return -1*rev_num
        elif rev_num < 2**31 - 1: 
            return rev_num
        else: return 0
        
if __name__ == "__main__":
    s = Solution()
    print(s.reverse(2**31-4))
    print(s.reverse(-123000))
    print(s.reverse(1234))
    
"""
find if triplet of numbers from a given array, matches the given target
"""
class Solution:
    
    def ifTriplet(self, target, nums):
        return self.helper(target, nums, 0, 0)

    def helper(self, target, nums, i, count):
        if target == 0 and count == 3: return True
        if target < 0 or count >= 3 or i == len(nums): return False
        # select a number @ i
        select = self.helper(target, nums, i + 1, count + 1)
        # don't select a number @ i
        not_select = self.helper(target - nums[i], nums, i, count)
        return select or not_select

nums = [2, 7, 4, 0, 9, 5, 1, 3]
target = 6

if __name__ == "__main__":
    s = Solution()
    print(s.ifTriplet(target, nums))
    print(s.ifTriplet(0, [1,2]))
    print(s.ifTriplet(27, [2]))
    

"""
find number of pairs to get a target sum from given array and target

Time and Space: O(n)
"""

class Solution:

    def num_pairs(self, target, nums):
        count = 0
        num_dict = {}
        for num in nums:
            if num in num_dict.values():
                count += 1
            num_dict[num] = target - num
        return count
    
if __name__ == "__main__":

    print(Solution().num_pairs(10, [8, 7, 2, 5, 3, 1]))
    print(Solution().num_pairs(0, [1, 2]))
    print(Solution().num_pairs(7, [5, 3, 4, 7, 6, 1]))
    
"""
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1
Gotcha: start the hash maps with initially {0: -1}, to cover when running sum is 0 and size of array is 2 (e.g [0, 1])
"""

class Solution:
    def findMaxLength(self, nums):
        if nums == None or len(nums) == 0: return 0
        num_dict = {0: -1}; rSum = 0; maxLen = 0
        for i in range(len(nums)):
            if nums[i] == 1: rSum += 1
            else: rSum -= 1
            if rSum in num_dict:
                maxLen = max(maxLen, i - num_dict[rSum])
            else:
                num_dict[rSum] = i
        return maxLen
    
if __name__ == "__main__":
    s = Solution()
    print(s.findMaxLength([0,1]))
    print(s.findMaxLength([1,0,1,0,1,1,1,1,0,0,1,0,1]))
    
"""
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k
Gotcha: start with a dictionary where sum 0 has happend 1 (i.e {0: 1})
"""

from collections import defaultdict
class Solution:
    def subarraySum(self, nums, k):
        rSum = 0; sumDict = defaultdict(int); count = 0
        sumDict[0] = 1
        for num in nums:
            rSum += num
            compliment = rSum - k
            if compliment in sumDict:
                count += sumDict[compliment]
            sumDict[rSum] += 1
        return count
    
if __name__ == "__main__":
    s = Solution()
    print(s.subarraySum([1,1,1], 2))
    print(s.subarraySum([1], 0))
    print(s.subarraySum([3,4,7,2,-3,1,4,2,0,1], 7))
    
"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except the number itself
Gotcha: use of reverse for loop 
"""

class Solution:
    def productExceptSelf(self, nums):
        if nums == None or len(nums) == 0: return None
        lproduct = 1; rproduct = 1; result = [1]
        for i in range(len(nums)):
            if i != 0: 
                lproduct = lproduct * nums[i - 1]
                result.append(lproduct)
        for i in reversed(range(len(nums))):
            if i != len(nums) - 1:
                rproduct = rproduct * nums[i + 1]
            result[i] = result[i] * rproduct
        return result
    
if __name__ == "__main__":
    s = Solution()
    print(s.productExceptSelf([1,2,3,4]))
    
"""
Diagonal traversal in a matrix:
Gotcha: very careful observation in boundary conditions
"""

class Solution:
    def findDiagonalOrder(self, matrix):
        direction = "up"
        result = []
        m = len(matrix); n = len(matrix[0])
        i = 0; j = 0

        for __ in range(m * n):
            result.append(matrix[i][j])
            if direction == "up":
                i -= 1; j +=1
                if i < 0 or j > n - 1: 
                    direction = "down"
                    if j <= n - 1:
                        i += 1;
                    else:
                        i += 2; j -= 1
            elif direction == "down":
                i += 1; j -= 1
                if j < 0 or i > m - 1:
                    direction = "up"
                    if i <= m - 1:
                        j += 1; 
                    else:
                        i -= 1; j += 2
        return result                
        
if __name__ == "__main__":
    s = Solution()
    print(s.findDiagonalOrder([[1,2,3,4], [5,6,7,8], [9,10,11,12]]))
    print(s.findDiagonalOrder([[1,2,3,4]]))
    print(s.findDiagonalOrder([[1,2],[3,4]]))
    

"""
Traverse in spiral for a given m x n matrix
Gotcha: ensure last direction don't re-run using condtional statements
"""

class Solution:
    def spiralOrder(self, matrix):

        top = 0; bottom = len(matrix) - 1
        left = 0; right = len(matrix[0]) - 1
        result = []

        while top <= bottom and left <= right:
            # move right
            if left <= right and bottom >= top:
                for i in range(left, right + 1):
                    result.append(matrix[top][i])
                top += 1
            # move down
            if left <= right and bottom >= top:
                for i in range(top, bottom + 1):
                    result.append(matrix[i][right])
                right -= 1
            # move left
            if left <= right and bottom >= top:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1
            # move up
            if left <= right and bottom >= top:
                for i in range(bottom, top -1 , -1):
                    result.append(matrix[i][left])
                left += 1
                
        return result
        
if __name__ == "__main__":
    s = Solution()
    print(s.spiralOrder([[1,2,3,4], [5,6,7,8], [9,10,11,12]]))
    print(s.spiralOrder([[1,2,3,4]]))
    print(s.spiralOrder([[1,2],[3,4]]))
    
"""
Game of life: LC use 4 rules to update the matrix
Gotcha: use indicators for in-place operation in 2 pass
"""

class Solution:
    def gameOfLife(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        self.dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, 1), (-1, -1), (1, -1), (1, 1)]
        self.m = len(board); self.n = len(board[0])
        
        for i in range(self.m):
            for j in range(self.n):
                count = self.findNeighbors(board, i, j)
                if board[i][j] == 1 and (count < 2 or count > 3):
                    board[i][j] = 2
                elif count == 3 and board[i][j] == 0:
                    board[i][j] = 3
                    
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == 3: board[i][j] = 1
                if board[i][j] == 2: board[i][j] = 0
        
        return board
                
    def findNeighbors(self, board, i, j):
        count = 0
        for d in self.dirs:
            row = i + d[0]
            col = j + d[1]
            if row >= 0 and col >= 0 and row < self.m and col < self.n:
                if board[row][col] == 1 or board[row][col] == 2: 
                    count += 1
                    
        return count
    
if __name__ == "__main__":
    s = Solution()
    print(s.gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]]))
    
"""
Find disappeared number in an array from 1 to n
Gotcha: use of indices and smartly using them based on value of the number at any index to get O(n) solution
"""

class Solution:
    def findDisappearedNumbers(self, nums):
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            if nums[idx] > 0: 
                nums[idx] = -nums[idx]
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)
        return result
    
if __name__ == "__main__":
    s = Solution()
    print(s.findDisappearedNumbers([4,3,2,7,8,2,3,1]))
    print(s.findDisappearedNumbers([1,1]))
    
"""
3 sum problem using 2-pointers

"""

class Solution:
    def threeSum(self, nums):
        result = []
        if nums == None or len(nums) < 3: return result
        nums = sorted(nums)
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            else:
                low = i + 1; high = len(nums) - 1
                remainder = -nums[i]
                while low < high:
                    if nums[low] + nums[high] == remainder:
                        result.append([nums[i], nums[low], nums[high]])
                        low += 1
                        high -= 1
                        while low < high and nums[low] == nums[low - 1]: 
                            low += 1
                        while low < high and nums[high] == nums[high + 1]:
                            high -= 1
                    elif nums[low] + nums[high] > remainder:
                        high -= 1
                    else: low += 1
        return result
               
if __name__ == "__main__":
    s = Solution()
    print(s.threeSum([-1,0,1,2,-1,-4]))
    
    
"""
sort 3 colors indicated by 0,1 and 2 without using sort function (O(n) instead of O(n log n))
Gotcha: mid <= high for while condition, and only moving high pointer when swapping with middle
"""

from collections import defaultdict
class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums == None or len(nums) == 0: return None
        l = 0; m = 0; h = len(nums) - 1
        
        while m <= h:
            if nums[m] == 0:
                nums[m], nums[l] = nums[l], nums[m]
                l += 1; m += 1
            elif nums[m] == 1:
                m += 1
            elif nums[m] == 2:
                nums[m], nums[h] = nums[h], nums[m]
                h -= 1
                
        return nums
    
if __name__ == "__main__":
    s = Solution()
    print(s.sortColors([2,0,1,0,1,1,0,2]))
    print(s.sortColors([1,2,0]))
    
"""
Find maximum area in an given array (no slant allowed)
Gotcha: conditional statements in 2-pointer solution, O(n^2) too as acceptable solution
"""

class Solution:
    def maxArea(self, height):
        if height == None or len(height) == 0: return 0
        l = 0; h = len(height) - 1; maxHeight = 0
        while l < h:
            maxHeight = max(maxHeight, min(height[l], height[h]) * (h - l))
            if height[l] <= height[h]:
                l += 1
            else: h -= 1  
        return maxHeight
    
if __name__ == "__main__":
    s = Solution()
    print(s.maxArea([1,8,6,2,5,4,8,3,7]))
    
"""
Remove duplicates more than k in place, use of two pointers and return length to limit the in-place array

"""
class Solution:
    def removeDuplicates(self, nums, k = 2):
        count = 1; length = 1; p = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 1
            if count <= k:
                nums[p] = nums[i]
                p += 1
                length += 1
        return length
    
if __name__ == "__main__":
    s = Solution(); nums = [1,1,1,2,2,3]
    print(nums[0: s.removeDuplicates(nums)])
    s = Solution(); nums = [0,0,0,1,1,1,1,2,2,3]
    print(nums[0: s.removeDuplicates(nums, k = 3)])
    
"""
merge sorted arrays with 0s at the end
Gotcha: extra while loop for the second array
"""

class Solution:
    
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0: return nums1
        p1 = m - 1; p2 = n - 1
        idx = m + n - 1
        
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] >= nums2[p2]:
                nums1[idx] = nums1[p1]
                p1 -= 1
            else:
                nums1[idx] = nums2[p2]
                p2 -= 1
            idx -= 1
        while p2 >= 0:
            nums1[idx] = nums2[p2]
            idx -= 1; p2 -= 1
        return nums1
            
if __name__ == "__main__":
    s = Solution()
    print(s.merge([1,2,8,0,0,0,0,0,0], 3, [-3,-2,2,2,5,6], 6))
    
    
    

