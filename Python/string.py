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