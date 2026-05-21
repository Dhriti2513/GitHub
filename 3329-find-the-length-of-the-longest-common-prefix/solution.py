class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        prefixes = set()
        
        for num in arr1:
            while num > 0:
                prefixes.add(num)
                num //= 10
                
        max_length = 0
        
        for num in arr2:
            while num > 0:
                if num in prefixes:
                    max_length = max(max_length, len(str(num)))
                    break
                num //= 10
                
        return max_length
