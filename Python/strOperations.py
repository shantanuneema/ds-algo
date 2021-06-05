"""
check if two equally sized strings (all lower characters) are isomorphic to each other:
Gotcha: check the isomorphic property in both ways
"""

class Solution:
    def isIsomorphic(self, s, t):
        sdict = {}; tdict = {}
        for i in range(len(s)):
            if s[i] in sdict:
                if sdict[s[i]] != t[i]: return False
            else: sdict[s[i]] = t[i]
            if t[i] in tdict:
                if tdict[t[i]] != s[i]: return False
            else: tdict[t[i]] = s[i]
        return True
    
if __name__ == "__main__":
    s = Solution()
    print(s.isIsomorphic('bcdc', 'baba'))
    print(s.isIsomorphic('foo', 'bar'))
    print(s.isIsomorphic('egg', 'add'))
    
"""
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
Gotcha: single pass solution (less complicated) using set, set.remove() vs set.pop()
"""
# 2 pass solution (using a dictionary) 
class Solution:
    def longestPalindrome(self, s: str) -> int:
        if s == None or len(s) == 0: return 0
        sdict = defaultdict(int); maxLen = 0
        for char in s:
            sdict[char] += 1

        single_elem = False
        for value in sdict.values():
            rep, remainder = divmod(value, 2)
            if remainder == 1:
                single_elem = True
            maxLen += rep * 2
        return maxLen + single_elem

# Single pass Solution (using a set)
class Solution:
    def longestPalindrome(self, s: str) -> int:
        if s == None or len(s) == 0: return 0
        cSet = set(); maxLen = 0
        for char in s:
            if char in cSet:
                cSet.remove(char)
                maxLen += 2
            else:
                cSet.add(char)
        return maxLen + 1 if len(cSet) > 0 else maxLen