class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
#         sperate each string in list
#         interate through each char in string
#         compare to each other
#         return the matching 
#         string = []
#         for x in strs:
#             string = x
#             print(type(string))
         
        if not strs:
            return ""
            
        for i, letter_group in enumerate(zip(*strs)):
            if len(set(letter_group)) > 1:
                return strs[0][:i]
        else:
            return min(strs)
            