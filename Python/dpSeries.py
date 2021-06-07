# simple fibonacci
def fib(n):
    
    if n == 1: return 1
    if n == 2: return 1
    
    return fib(n - 1) + fib(n - 2)
  
# fibonacci with memoization
from collections import defaultdict
fib_dict = defaultdict(int)

def fib(n):
    if fib_dict[n]: return fib_dict[n]
    if n <= 2: return 1
    fib_dict[n] = fib(n - 1) + fib(n - 2)
    return fib_dict[n]
  
# gridTravel recursive
def gridTravel(m, n):
    
    # base
    if m == 0 or n == 0: return 0
    if m == 1 or n == 1: return 1
    
    # logic to move right or down
    movements = gridTravel(m - 1, n) + gridTravel(m, n - 1)
    
    return movements
  
# gridTravel with memoization:
from collections import defaultdict
node_dict = defaultdict(int)

def gridTravel(m, n):
    # memoization
    if (m, n) in node_dict.keys():
        return node_dict[(m, n)]
    # base
    if m == 0 or n == 0: return 0
    if m == 1 or n == 1: return 1
    # logic
    node_dict[(m, n)] = gridTravel(m - 1, n) + gridTravel(m, n - 1)
    return node_dict[(m, n)]
  
# canSum with recursion

def canSum(targetSum, numbers):
    
    # base
    if targetSum == 0: return True
    if targetSum < 0: return False
    
    # logic
    for number in numbers:
        balance = targetSum - number
        if canSum(balance, numbers): return True
        
    return False
  
# canSum with memoization
from collections import defaultdict
node_dict = defaultdict(bool)

def canSum(targetSum, numbers):
    
    # memoization
    if targetSum in node_dict: return node_dict[targetSum]
    
    # base
    if targetSum == 0: return True
    if targetSum < 0: return False
    
    # logic
    for number in numbers:
        balance = targetSum - number
        if canSum(balance, numbers):
            node_dict[targetSum] = True
            return True
        
    node_dict[targetSum] = False
    
    return node_dict[targetSum]

"""
How sum problem
"""
# without memoization
class Solution:
    def howsum(self, target, nums):

        if target == 0: return []
        if target < 0: return None

        answer = []
        for num in nums:
            balance = target - num
            result = self.howsum(balance, nums)
            if result != None:
                return result + [num]
        return None

if __name__ == "__main__":
    s = Solution()
    print(s.howsum(7, [5,3,4,7]))
    
# with memoization
class Solution:

    def __init__(self):
        self.result_dict = {}

    def howsum(self, target, nums):

        if target == 0: return []
        if target < 0: return None
        if target in self.result_dict: return self.result_dict[target]
        
        for num in nums:
            balance = target - num
            result = self.howsum(balance, nums)
            if result != None:
                self.result_dict[target] = result + [num]
                return self.result_dict[target]
        self.result_dict[target] = None
        return None

if __name__ == "__main__":
    s = Solution()
    print(s.howsum(200, [7, 14]))
    print(s.howsum(7, [2,3,4,7]))
    print(s.howsum(0, [1,2]))
    print(s.howsum(50, [1,2]))

"""
Best sum problem
"""
# without memoization
class Solution:
        
    def best_sum(self, target, nums):

        if target == 0: return []
        if target < 0: return None
        
        shortest_result = None
        for num in nums:
            balance = target - num
            result = self.best_sum(balance, nums)
            if result != None:
                comb_result = result + [num]
                if shortest_result == None or len(comb_result) < len(shortest_result):
                    shortest_result = comb_result

        return shortest_result

if __name__ == "__main__":
    s = Solution()
    print(s.best_sum(7, [5, 3, 4, 7]))
    print(s.best_sum(8, [2, 3, 5]))

# with memoization
class Solution:
    
    def __init__(self):
        self.result_dict = {}
        
    def best_sum(self, target, nums):

        if target == 0: return []
        if target < 0: return None
        if target in self.result_dict: return self.result_dict[target]
        
        shortest_result = None
        for num in nums:
            balance = target - num
            result = self.best_sum(balance, nums)
            if result != None:
                comb_result = result + [num]
                if shortest_result == None or len(comb_result) < len(shortest_result):
                    shortest_result = comb_result
                    
        self.result_dict[target] = shortest_result
        return shortest_result

if __name__ == "__main__":
    print(Solution().best_sum(7, [5, 3, 4, 7, 6, 1]))
    print(Solution().best_sum(8, [2, 3, 5]))
    print(Solution().best_sum(300, [7, 14]))


"""
Coin change problem (LC, using recursion) - Not optimum (gives TLE)
"""
class Solution:
    
    def coinChange(self, coins, amount):
        # Recursive Solution
        return self.helper(coins, amount, 0, 0)
        
    def helper(self, coins, amount, i, min_coins):
        
        if amount == 0: return min_coins
        if amount < 0 or i == len(coins): return -1

        # not select coin at index i
        not_select = self.helper(coins, amount, i + 1, min_coins)
        # select coin at index i
        select = self.helper(coins, amount - coins[i], i, min_coins + 1)
        
        if not_select == -1: return select
        if select == -1: return not_select
        
        return min(not_select, select)
    
"""
Minimum steps to 1 from number N to 1 by:
    1. reduce by 1
    2. divide by 2, and
    3. divide by 3
    
Approach: Recursive solution and the same with memoization
"""
# recursively
class Solution:

    def min_steps(self, num):
        if num == 1: return 0
        
        steps = 1 + self.min_steps(num - 1)
        if num % 2 == 0:
            steps = min(steps, 1 + self.min_steps(num // 2))
        if num % 3 == 0:
            steps = min(steps, 1 + self.min_steps(num // 3))
            
        return steps
    
if __name__ == "__main__":
    s = Solution()
    print(s.min_steps(300))
    
# with Memoization
class Solution:
    
    def __init__(self):
        self.num_dict = {}

    def min_steps(self, num):
        if num == 1: return 0
        if num in self.num_dict: return self.num_dict[num]
        
        steps = 1 + self.min_steps(num - 1)
        if num % 2 == 0:
            steps = min(steps, 1 + self.min_steps(num // 2))
        if num % 3 == 0:
            steps = min(steps, 1 + self.min_steps(num // 3))
            
        self.num_dict[num] = steps
        return steps
    
if __name__ == "__main__":
    s = Solution()
    print(s.min_steps(300))
    
"""
Find if triplet exist
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

if __name__ == "__main__":
    s = Solution()
    print(s.ifTriplet(6, [2, 7, 4, 0, 9, 5, 1, 3]))
    print(s.ifTriplet(0, [1, 2]))
    print(s.ifTriplet(27, [2]))














