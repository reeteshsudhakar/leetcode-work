from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = {i : [] for i in range(numCourses)}
        
        for course, prereq in prerequisites:
            d[course].append(prereq)
        
        vs = set()
        
        def dfs(course: int) -> bool:
            if course in vs: return False
            if d[course] == []: return True
            
            vs.add(course)
            
            for neighbor in d[course]:
                if not dfs(neighbor):
                    return False
            vs.remove(course)
            d[course] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i): return False
        return True