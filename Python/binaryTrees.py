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
            self.inhelper_asc(self.inhelper_asc(root.left))
            self.result.append(root.value)
            self.inhelper_asc(self.inhelper_asc(root.right))
    
    def inhelper_desc(self, root):
        if root:
            self.inhelper_desc(self.inhelper_desc(root.right))
            self.result.append(root.value)
            self.inhelper_desc(self.inhelper_desc(root.left))
            
    def prehelper_asc(self, root):
        if root:
            self.result.append(root.value)
            self.prehelper_asc(self.prehelper_asc(root.left))
            self.prehelper_asc(self.prehelper_asc(root.right))
    
    def prehelper_desc(self, root):
        if root:
            self.result.append(root.value)
            self.prehelper_desc(self.prehelper_desc(root.right))
            self.prehelper_desc(self.prehelper_desc(root.left))
            
    def posthelper_asc(self, root):
        if root:
            self.posthelper_asc(self.posthelper_asc(root.left))
            self.posthelper_asc(self.posthelper_asc(root.right))
            self.result.append(root.value)
    
    def posthelper_desc(self, root):
        if root:
            self.posthelper_desc(self.posthelper_desc(root.right))
            self.posthelper_desc(self.posthelper_desc(root.left))
            self.result.append(root.value)

print(Solution().in_order(tree_node))
print(Solution().in_order(tree_node, ascending = False))
print(Solution().pre_order(tree_node))
print(Solution().pre_order(tree_node, ascending = False))
print(Solution().post_order(tree_node))
print(Solution().post_order(tree_node, ascending = False))