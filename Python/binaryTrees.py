"""
Construction of binary trees in Python
"""

class TreeNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BinaryTree:

    def insertLevelOrder(self, arr, root, i, n):
        if i < n:
            temp = TreeNode(arr[i]) 
            root = temp 
            # insert left child 
            root.left = self.insertLevelOrder(arr, root.left, 2 * i + 1, n)
            # insert right child 
            root.right = self.insertLevelOrder(arr, root.right, 2 * i + 2, n)
        return root

if __name__ == "__main__":
    s = BinaryTree()
    nums = [25,20,30,10,22,28,40,5,15,21,23,27,29,35,50]
    arr = [1,2,3,4,5]
    tree_node = s.insertLevelOrder(nums, None, 0, len(nums))
    new_node = s.insertLevelOrder(arr, None, 0, len(arr))
    
"""
In-Order, Pre-Order and Post-Order traversal techniques for Binary Search Trees
"""

"""
Construction of binary trees in Python
"""

class TreeNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BinaryTree:

    def insertLevelOrder(self, arr, root, i, n):
        if i < n:
            temp = TreeNode(arr[i]) 
            root = temp 
            # insert left child 
            root.left = self.insertLevelOrder(arr, root.left, 2 * i + 1, n)
            # insert right child 
            root.right = self.insertLevelOrder(arr, root.right, 2 * i + 2, n)
        return root

if __name__ == "__main__":
    s = BinaryTree()
    nums = [25,20,30,10,22,28,40,5,15,21,23,27,29,35,50]
    arr = [1,2,3,4,5]
    tree_node = s.insertLevelOrder(nums, None, 0, len(nums))
    new_node = s.insertLevelOrder(arr, None, 0, len(arr))
    
"""
In-Order, Pre-Order and Post-Order traversal techniques for Binary Search Trees
"""

class Solution:
    
    def __init__(self):
        self.result = []
        
    def in_order(self, root, ascending = True):
        if ascending:
            self.inhelper_asc(root)
        else: self.inhelper_desc(root)
        return self.result
    
    def pre_order(self, root, ascending = True):
        if ascending:
            self.prehelper_asc(root)
        else: self.prehelper_desc(root)
        return self.result
    
    def post_order(self, root, ascending = True):
        if ascending:
            self.posthelper_asc(root)
        else: self.posthelper_desc(root)
        return self.result
        
    def inhelper_asc(self, root):
        if root:
            self.inhelper_asc(root.left)
            self.result.append(root.value)
            self.inhelper_asc(root.right)
    
    def inhelper_desc(self, root):
        if root:
            self.inhelper_desc(root.right)
            self.result.append(root.value)
            self.inhelper_desc(root.left)
            
    def prehelper_asc(self, root):
        if root:
            self.result.append(root.value)
            self.prehelper_asc(root.left)
            self.prehelper_asc(root.right)
    
    def prehelper_desc(self, root):
        if root:
            self.result.append(root.value)
            self.prehelper_desc(root.right)
            self.prehelper_desc(root.left)
            
    def posthelper_asc(self, root):
        if root:
            self.posthelper_asc(root.left)
            self.posthelper_asc(root.right)
            self.result.append(root.value)
    
    def posthelper_desc(self, root):
        if root:
            self.posthelper_desc(root.right)
            self.posthelper_desc(root.left)
            self.result.append(root.value)

print(Solution().in_order(tree_node))
print(Solution().in_order(tree_node, ascending = False))
print(Solution().pre_order(tree_node))
print(Solution().pre_order(tree_node, ascending = False))
print(Solution().post_order(tree_node))
print(Solution().post_order(tree_node, ascending = False))

"""
Validate a Binary-Tree
"""

# Recursive Solution (more memory):
class Solution:
    
    def isValidBST(self, root: TreeNode) -> bool:
        if root == None: return True
        self.result = []
        self.inOrder(root)
        if len(self.result) > 1:
            for i in range(1, len(self.result)):
                if self.result[i - 1] >= self.result[i]:
                    return False
        return True
    
    def inOrder(self, root):
        if root:
            self.inOrder(root.left)
            self.result.append(root.value)
            self.inOrder(root.right)
            
if __name__ == "__main__":
    print(Solution().isValidBST(tree_node))
    print(Solution().isValidBST(new_node))
    
# Iterative Solution    
class Solution:
    def isValidBST(self, root):
        stack = []; prev = TreeNode(-float('inf'))
        while root != None or len(stack) != 0:
            while root != None:
                stack.append(root)
                root = root.left
            # print([r.value for r in stack])
            root = stack.pop()
            if prev != None and root != None:
                if prev.value >= root.value:
                    return False
            prev = root
            root = root.right
        return True
    
if __name__ == "__main__":
    print(Solution().isValidBST(tree_node))
    print(Solution().isValidBST(new_node))
    
# Recursive Solution
class Solution:
    
    def isValidBST(self, root: TreeNode) -> bool:
        if root == None: return True
        self.prev = TreeNode(value = -float('inf'))
        return self.inOrder(root)
    
    def inOrder(self, root):
        
        if root == None: return True
        if self.inOrder(root.left) == False: 
            return False
        if self.prev.value >= root.value: 
            return False
        self.prev = root
        return self.inOrder(root.right)
    
if __name__ == "__main__":
    print(Solution().isValidBST(tree_node))
    print(Solution().isValidBST(new_node))    
    
# Better recursive solution:
class Solution:
    
    def isValidBST(self, root: TreeNode) -> bool:
        return self.isValid(root, None, None)
    
    def isValid(self, root, minval, maxval):
        
        if root == None: return True
        if minval != None and root.value <= minval: return False
        if maxval != None and root.value >= maxval: return False
        
        return self.isValid(root.left, minval, root.value) and \
               self.isValid(root.right, root.val, maxval)
    
"""
sum of root to leaf numbers
"""
if __name__ == "__main__":
    s = BinaryTree()
    nums = [4,9,0,5,1]
    tree_node = s.insertLevelOrder(nums, None, 0, len(nums))

# Iterativ Solution
class Solution:
    
    def sumNumbers(self, root: TreeNode) -> int:
        
        stack = []; nodeSum = 0; num_list = []
        if root == None: return nodeSum
            
        while root != None or len(stack) != 0:
            while root != None:
                nodeSum = nodeSum * 10 + root.value
                stack.append((root, nodeSum))
                root = root.left
            root, nodeSum = stack.pop()
            if root.left == None and root.right == None:
                num_list.append(nodeSum)
            root = root.right

        return sum(num_list)
    
if __name__ == "__main__":
    s = Solution()
    print(s.sumNumbers(tree_node))
    
# iterative solution:
class Solution:
    
    def sumNumbers(self, root: TreeNode) -> int:
        self.result = 0
        self.dfs(root, 0)
        return self.result
    
    def dfs(self, root, nodeSum):
        
        if root == None: return
        nodeSum = nodeSum * 10 + root.value
        if root:
            self.dfs(root.left, nodeSum)
            if root.left == None and root.right == None:
                self.result += nodeSum
            self.dfs(root.right, nodeSum)
            
if __name__ == "__main__":
    s = Solution()
    print(s.sumNumbers(tree_node))