# time: O(n)
# space: O(1)
class Solution:
    def trap(self, height: List[int]) -> int:
        # if len(height) <= 2:
        #     return 0
        
        water = 0 
        l = 1
        r = len(height) - 1
        
        lmax = height[0]
        rmax = height[-1]
        
        while l <= r:
            # check lmax and rmax for current l, r positions
            lmax = max(height[l], lmax)
            rmax = max(height[r], rmax)
            
            #fill water upto lmax at pos l and move l to right
            if lmax <= rmax:
                water += lmax - height[l]
                l += 1      
            #fill water upto rmax at pos r and move r to left
            else:
                water += rmax - height[r]
                r -= 1
                
        return water

