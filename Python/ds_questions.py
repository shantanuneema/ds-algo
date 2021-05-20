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
    
"""
Find ID of the person with biggest tip
"""

class Solution:
    def biggestTip(user_ids, tips):
        max_tip = 0
        for user, tip in zip(user_ids, tips):
            if tip > max_tip:
                max_tip = tip
                highestUser = user
        return highestUser
    
if __name__ == "__main__":
    s = Solution()
    print(s.biggestTip([103, 105, 105, 107, 106, 103, 102, 108, 107, 103, 102],
                       [2, 5, 1, 0, 2, 1, 1, 0, 0, 2, 2]))

"""
Given a list of stock prices in ascending order by datetime, 
write a function that outputs the max profit by buying and selling at a specific interval
"""

class Solution:
    def get_max_profit(self, stock_prices, dts):
        minPrice = stock_prices[0]; maxProfit = 0
        buyTime = dts[0]
        for i in range(len(stock_prices)):
            if stock_prices[i] < minPrice:
                minPrice = stock_prices[i]
                buyTime = dts[i]
            if stock_prices[i] - minPrice > maxProfit: 
                maxProfit = stock_prices[i] - minPrice
                sellTime = dts[i]
        
        try: 
            answer = (maxProfit, buyTime, sellTime)
        except:
            answer = None
            
        return answer
        
if __name__ == "__main__":
    s = Solution()
    print(s.get_max_profit([10,5,20,32,25,12],
                           ['2019-01-01', 
                           '2019-01-02',
                           '2019-01-03',
                           '2019-01-04',
                           '2019-01-05',
                           '2019-01-06']))
 
    print(s.get_max_profit([10,5],
                           ['2019-01-01', 
                           '2019-01-02']))   
    print(s.get_max_profit([5,10,4],
                           ['2019-01-01', 
                           '2019-01-02',
                           '2019-01-03']))  
    
"""
We have a list of existing ids that we have already scraped. 
Let's say we also have two lists, one of names and another of urls 
that correspond to the names in another list with the id of the names in the url
"""

class Solution:
    def newResumes(self, existing_ids, names, urls):
        ids = set(existing_ids)
        output = []
        for name, url in zip(names, urls):
            currID = int(url.split("/")[2])
            if not currID in ids:
                output.append((name, currID))
                
        return output
        
if __name__ == "__main__":
    s = Solution()
    print(s.newResumes([15234, 20485, 34536, 95342, 94857],
    ['Calvin', 'Jason', 'Cindy', 'Kevin'],
    ['domain.com/resume/15234', 
     'domain.com/resume/23645', 
     'domain.com/resume/64337', 
     'domain.com/resume/34536']))
