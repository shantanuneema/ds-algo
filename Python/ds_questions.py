"""
Write a function that can take a string and return a list of bigrams.

Example:

sentence = "Have free hours and love children? 
Drive kids to school, soccer practice 
and other activities."

Gotcha: expected output have all lower case letters
"""


class Solution:
    def find_bigrams(sentence):
        words = sentence.lower().split(" ")
        output = [(words[i], words[i + 1]) for i in range(len(words) - 1)]
        return output

s = Solution    
print(s.find_bigrams("Have free hours and love children? \
Drive kids to school, soccer practice and other activities."))

"""
Given a list of stop words, write a function that takes a string and returns a string stripped of the stop words

Gotcha: use of set (to avoid search each word again and again, help to reduce run-time by using O(1) space)
"""

class Solution:
    
    def filter_stopwords(self, stopwords, paragraph):
        
        if paragraph == None or len(paragraph) == 0: return None
        stopwords_set = set(stopwords)
        words = paragraph.split(" ")
        stripped = [word for word in words if word not in stopwords_set]
        
        return " ".join(stripped)
        
stopwords = ['I', 'as', 'to', 'you', 'your', 'but', 'be', 'a']

paragraph = 'I want to figure out how I can be a better data scientist'
if __name__ == "__main__":
    s = Solution()
    print(s.filter_stopwords(stopwords, paragraph))
    
"""
Given two strings, string1 and string2, find out if string1 is a subsequence of string2

Gotcha: look for optimal solution (e.g. 2 pointers)
"""
 
class Solution:
    
    def ifSubseq(self, string1, string2):
        
        if string1 == None or string2 == None: return None
        
        p1 = 0; p2 = 0; matched = 0
        while p1 < len(string1) and p2 < len(string2):
            if string1[p1] == string2[p2]:
                p1 += 1; p2 += 1
                matched += 1
            else: p2 += 1
            
        return matched == len(string1)
        
string1 = 'abc'
string2 = 'asbsc'
string3 = 'acedb'
        
if __name__ == "__main__":
    s = Solution()
    print(s.ifSubseq(string1, string2))
    print(s.ifSubseq(string1, string3))
    
"""
Given a string, return the first recurring character in it, or None if there is no recurring chracter

Gotcha: use of set (for O(n) traversal)
"""
    
class Solution:

    def first_reoccur(self, inp):
        hashset = set()
        for item in list(inp):
            if item in hashset:
                return item
            else:
                hashset.add(item)

        return None

if __name__ == "__main__":
    s = Solution()
    print(s.first_reoccur("interviewquery"))
    print(s.first_reoccur("interv"))
    
"""
count number of lines in a large file

Gotcha: use with, instead of loading the file (efficient solution)
"""

class Solution:
    def count_lines(self, file_path):
        count = 0
        with open(file_path, 'r') as log_file:
            for line in log_file:
                count += 1

        return count
    
if __name__ == "__main__":
    s = Solution()
    print(s.count_lines(file_path))
    
    
