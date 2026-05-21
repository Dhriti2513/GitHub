class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        operations = []
        target_set = set(target)
        max_target = target[-1]
        
        for i in range(1, max_target + 1):
            if i in target_set:
                operations.append("Push")
            else:
                operations.append("Push")
                operations.append("Pop")
                
        return operations
