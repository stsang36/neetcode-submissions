class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        n_piles = len(piles)
        left = 1
        right = max(piles)
        res = right

        while left <= right:
            
            mid = left + (right - left) // 2
            
            duration = 0
            for p in piles:
                duration += math.ceil(p / mid)
            
            if duration <= h:
                res = min(res, mid)
                right = mid - 1
            else:
                left = mid + 1


        return res






        