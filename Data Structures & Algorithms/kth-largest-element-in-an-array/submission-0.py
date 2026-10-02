class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        res = [-num for num in nums]
        heapq.heapify(res)

        for i in range(k-1):
            heapq.heappop(res)

        return -res[0]

        
        