class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        
        # for each l < len(arr)
        for n in range(len(arr)):
            # find max until l
            n_th_max = max(arr[:len(arr) - n])
            # find index of max until l
            n_th_max_idx = arr.index(n_th_max) + 1
            # reverse subarray until max idx until l
            arr[:n_th_max_idx] = reversed(arr[:n_th_max_idx])
            # append idx of reversal
            res.append(n_th_max_idx)
            
            # also reverse array section after n
            arr[:len(arr) - n] = reversed(arr[:len(arr) - n])
            # append idx of reversal
            res.append(len(arr) - n)
        
        return res
