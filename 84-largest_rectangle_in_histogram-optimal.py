# time: O(n^3)
# space: O(1)
# solution uses monotonic stack
# x coordinate represented by heights array index
# y coordinate represented by heights[x]
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # init x coordinate as -1
        stack = [-1]
        # add zero as dummy tail: prevents out of index situation for first pop
        heights.append(0)
        # area of rectangle
        max_rect = 0
        
        # scan each x coordinate and y coordinate
        for x, y in enumerate(heights):
            # while current height is lower than previous
            while heights[stack[-1]] > y:
            # update rectangle area from previous heights
                # get height
                h = heights[stack.pop()]
                # compute width
                w = x - stack[-1] - 1 
                # update maximal area
                max_rect = max(max_rect, h * w)
            # push current x coordinat into stack
            stack.append(x)
            
        return max_rect
