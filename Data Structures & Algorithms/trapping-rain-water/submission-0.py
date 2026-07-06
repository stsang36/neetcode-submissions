class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)

        left = 0
        right = n - 1

        lmax = height[left]
        rmax = height[right]

        res = 0

        while left < right:

            if lmax > rmax:

                right -= 1
                rmax = max(rmax, height[right])
                res += rmax - height[right]
                
            elif lmax <= rmax:
                left += 1
                lmax = max(lmax, height[left])
                res += lmax - height[left]
                

        return res 


        