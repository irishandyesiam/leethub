class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
#         iterate through half the integer (length?)
#         reverse iterate half through integer (length?)
#         compare to each other
#         if same (true) return "x is a palindrome"
#         else: false
        return False if x < 0 else x == int(str(x)[::-1])
            
            