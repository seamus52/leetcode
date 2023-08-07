# 1) for every unoccupied cell, check if there is a higher elevation on both sides - ineffective
# 2) 
# - create map: for every row,  plot the cell if row# (in array) < value in height vector
# fill map sequentially: wall turns on fill,
# fills until edge, then removes excess (remembering the last wall)
class Solution:
    def trap(self, height: List[int]) -> int:
        m = self.gen_map(height)
        return self.rain(m)


    def rain(self, m):
        trapped_cnt = 0

        for r in range(len(m)):
            write_active = False
            last_block_pos = 0
            last_write_stretch = []
            for c in range(len(m[0])):
                if m[r][c] == 1:
                    write_active = True
                    last_block_pos = c
                    last_write_stretch = []
                if m[r][c] == 0 and write_active:
                    #m[r][c] = 3
                    trapped_cnt += 1
                    last_write_stretch.append((r,c))
                if c == len(m[0]) - 1:
                    for dr, dc in last_write_stretch:
                        #m[dr][dc] = 0
                        trapped_cnt -= 1
        # print(m)
        return trapped_cnt

        
    def gen_map(self, height):
        m = []
        for r in range(max(height)):
            m.append([])
            for c in range(len(height)):
                if height[c] > r:
                    m[r].append(1)
                else:
                    m[r].append(0)
        
        return m


    def print_map(self, m):
        for r in range(len(m)):
            for c in range(len(m[0])):
                print(m[r][c], end="")
            print()
