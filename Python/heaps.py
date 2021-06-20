from typing import List

"""
Description: Find Kth largest element in an unsorted array
"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        from heapq import heappush, heappop
        result = []
        for num in nums:
            heappush(result, num)
            if len(result) > k:
                heappop(result)
        return result[0]
    
if __name__ == "__main__":
    s = Solution()
    print(s.findKthLargest([3,2,1,5,6,4], 2))
    
# using maxHeap
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        from heapq import heappush, heappop
        maxVal = float('inf')
        maxHeap = []
        for num in nums:
            heappush(maxHeap, -1 * num)
            if len(maxHeap) > len(nums) - k:
                maxVal = min(maxVal, -1 * heappop(maxHeap))
                
        return maxVal
    
if __name__ == "__main__":
    s = Solution()
    print(s.findKthLargest([3,2,1,5,6,4], 2))