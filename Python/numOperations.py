"""
check if a integer is palindrome (without converting to a string)
Gotcha: use simple airthmatic by finding reverse of the number
"""
class Solution:
    def isPalindrome(self, x):
        rev_num = 0
        chk_num = x
        while chk_num > 0:
            remainder = chk_num % 10
            rev_num = rev_num * 10 + remainder
            chk_num = chk_num // 10

        if rev_num == x: return True
        return False

if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome(1221))
    print(s.isPalindrome(-121))
    
"""
reverse an integer, ensure values out of max and min allowed range returns 0
gotcha: carefully take care of -ve sign in reversing as well as conditional statement before returning
"""
class Solution:
    def reverse(self, x):
        if x == None: return
        ifneg = True if x < 0 else False
        
        y = abs(x)
        rev_num = 0
        while y > 0:
            remainder = y % 10
            rev_num = rev_num * 10 + remainder
            y = y // 10
            
        if ifneg and rev_num < 2**31:
            return -1*rev_num
        elif rev_num < 2**31 - 1: 
            return rev_num
        else: return 0
        
if __name__ == "__main__":
    s = Solution()
    print(s.reverse(2**31-4))
    print(s.reverse(-123000))
    print(s.reverse(1234))