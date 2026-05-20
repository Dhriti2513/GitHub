class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        n = len(A)
        C = []
        seen = set()
        common_count = 0
        
        for i in range(n):
            if A[i] in seen:
                common_count += 1
            else:
                seen.add(A[i])
                
            if B[i] in seen:
                common_count += 1
            else:
                seen.add(B[i])
                
            C.append(common_count)
            
        return C
