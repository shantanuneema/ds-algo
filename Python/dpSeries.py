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

# howsum with recursion:
class Solution:

    def howsum(self, target, nums):

        if target == 0: return []
        if target < 0: return None

        answer = []
        for num in nums:
            balance = target - num
            result = howsum(balance, nums)
            if result != None:
                return result + [num]
        return None

if __name__ == "__main__":
    s = Solution()
    print(s.howsum(7, [5,3,4,7]))
    
# howsum with memoization

class Solution:

    def __init__(self):
        self.result_dict = {}

    def howsum(self, target, nums):

        if target == 0: return []
        if target < 0: return None
        if target in self.result_dict: return self.result_dict[target]

        answer = []
        for num in nums:
            balance = target - num
            result = howsum(balance, nums)
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
