#Time & Space: O(N*W^2)
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        reverse_of = {} # reverse of key is at value
        pp = []

        for i, word in enumerate(words):
            reverse_of[word[::-1]] = i

        for i, word in enumerate(words):
            
            # case 1) word and its reverse together are palindrome (abcd, bcda)
            if word in reverse_of and reverse_of[word] != i:
                pp.append([i, reverse_of[word]])
                
            # case 2) if one word is palindrome and the other is empty string
            # word != "" : duplicate elimination of this edge case
            if word != "" and "" in reverse_of and word == word[::-1]:
                pp.append([i, reverse_of[""]])
                pp.append([reverse_of[""], i])

            # case 3)    
            for j in range(len(word)):
                # shorter word + longer word parlindrome
                if word[j:] in reverse_of and word[:j] == word[j-1::-1]:
                    pp.append([reverse_of[word[j:]], i])
                
                # longer word + shorter word parlindrome
                if word[:j] in reverse_of and word[j:] == word[:j-1:-1]:
                    pp.append([i, reverse_of[word[:j]]])
                    
        return pp
