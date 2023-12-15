class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        hashmap = defaultdict(int)
        for start, end in paths:
            hashmap[start] = end

        

        for i, j in paths:
            if j not in hashmap:
                return j



        
