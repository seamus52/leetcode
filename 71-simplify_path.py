# time: O(n) - processing every inout element only 1x
# space: O(1) - we're rendering the output only
class Solution:
    def simplifyPath(self, path: str) -> str:
        canonical = []
        for i, d in enumerate(path.split("/")[1:]):
            if d:
                canonical.append(d)

            if d == ".":
                canonical.pop()
            
            if d == ".." and canonical:
                canonical.pop()
                if canonical:
                    canonical.pop()

        return "/" + "/".join(canonical)

