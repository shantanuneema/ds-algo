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
    
if __name__ == "__main__":
    s = Solution    
    print(s.find_bigrams("Have free hours and love children? \
    Drive kids to school, soccer practice and other activities."))


"""
Given a list of timestamps in sequential order, return a list of lists grouped by week (7 days) 
Use the first timestamp as the starting point

Gotcha: instead of differnce in days, note the question ask the days in same week 
(e.g. Feb 1st and 2nd are in same week but Feb 5th in next week though they are under 7 days difference)
"""

import datetime

class Solution:

    def weekly_aggregate(self, ts):

        if ts == None or len(ts) == 0: return -1
        output = [[ts[0]]]; count = 0
     
        for idx in range(1, len(ts)):
            if self.WkNum(ts[idx]) == self.WkNum(ts[idx - 1]):
                output[count].append(ts[idx])
            else:
                count += 1
                output.append([ts[idx]])

        return output

    def WkNum(self, time_text):
        t = datetime.datetime.strptime(time_text, "%Y-%m-%d")
        wk = (t - datetime.datetime(t.year, 1, 1)).days // 7 + 1
        return wk
    
ts = ['2019-01-01', 
      '2019-01-02',
      '2019-01-08', 
      '2019-02-01', 
      '2019-02-02',
      '2019-02-05']

if __name__ == "__main__":
    s = Solution()
    print(s.weekly_aggregate(ts))
