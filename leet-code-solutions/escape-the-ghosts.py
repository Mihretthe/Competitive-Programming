class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        my = abs(target[0]) + abs(target[1])

        for i,j in ghosts:
            if abs(target[0] - i) + abs(target[1] - j) <= my:
                return False
        
        return True