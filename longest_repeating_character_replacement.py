# using 2 pointers: r, l
# Time: O(n)
# Space: O(1)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        freq = defaultdict(int) # defaultdict(int) returns 0 by default, even for nonexistent keys
        max_length = 0
        
        for r in range(len(s)):
            # If a character is not in the frequency dict, this inserts it with a value of 1
            # If a character is in the dict, we simply add one.
            freq[s[r]] += 1
            
            # We only care about the MAXIMUM of the seen values.
            # Get the length of the current substring, then subtract the MAXIMUM frequency. See if this is <= K for validity.
            cur_length = r - l + 1
            if cur_length - max(freq.values()) > k: # if we have replaced > K letters, then it's time to slide the window
                # decrement frequency of char at left pointer, then increment pointer
                freq[s[l]] -= 1
                l += 1
            else: # if we have replaced <= K letters, record a new maxLen
                max_length = max(max_length, cur_length)
                
        return max_length    

