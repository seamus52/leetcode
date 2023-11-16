# time: O(num of nonzeros)
# space: O(num of nonzeros)
# theorectically this solution should be more efficient that list procesing
# but measurements demonstrate that it is not
class SparseVector:
    def __init__(self, nums: List[int]):
        self.nonzeros = {}
        for i, n in enumerate(nums):
            if n != 0:
                self.nonzeros[i] = n

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        p = 0
        for i, n in self.nonzeros.items():
            if i in vec.nonzeros:
                p += self.nonzeros[i] * vec.nonzeros[i]
        return p
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
