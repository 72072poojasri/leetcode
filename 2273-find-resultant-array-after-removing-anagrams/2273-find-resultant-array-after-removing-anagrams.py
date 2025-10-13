class Solution:
    def removeAnagrams(self, words):
        stack = []
        
        for word in words:
            if stack and sorted(stack[-1]) == sorted(word):
                continue  # delete the current word (skip pushing)
            stack.append(word)
        
        return stack