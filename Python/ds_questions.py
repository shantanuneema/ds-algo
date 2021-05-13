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


