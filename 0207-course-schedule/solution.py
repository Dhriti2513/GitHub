class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adj = [[] for _ in range(numCourses)]
        for dest, src in prerequisites:
            adj[src].append(dest)
            
        visit = [0] * numCourses
        
        def has_cycle(course):
            if visit[course] == 1:
                return True
            if visit[course] == 2:
                return False
                
            visit[course] = 1
            
            for neighbor in adj[course]:
                if has_cycle(neighbor):
                    return True
                    
            visit[course] = 2
            return False

        for i in range(numCourses):
            if visit[i] == 0:
                if has_cycle(i):
                    return False
                    
        return True
