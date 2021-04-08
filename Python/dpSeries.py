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
