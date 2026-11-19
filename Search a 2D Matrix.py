class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = []
        
        for i in matrix:
            m.extend(i)

        return target in m
