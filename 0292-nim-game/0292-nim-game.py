class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # varible to hold HEAP
        # command to remove 1 to 3 stones
        # check remaining stones in HEAP, n == 0 end game
        # keep track of players turn
        # return turn if I can win game
        # return false if I cannot win game
        # remove 3 until cannot remove 3 anymore
        # then remove 2 until cannot remove 2 anymore
        # then remove 1 until cannot remove 1 anymore
        # HINT start with 5 stones
        # if HEAP is one, remove one
        # if HEAP is two, remove two
        # if HEAP is three, remove three
        # if HEAP is four, ????? I will always lose. if n = 4 return false (n%4)
        # if HEAP is five, remove one 
    
        # if n%4 == 0:
        #     return False
        # else:
        #     return True
        
        return n%4
          
        