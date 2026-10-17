class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        path = set()

        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        def dfs(crs):
            if crs in path:
                return False
            if preMap[crs] == []:
                return True
            path.add(crs)
            for prereq in preMap[crs]:
                if not dfs(prereq):
                    return False
            preMap[crs] = []
            path.remove(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True        