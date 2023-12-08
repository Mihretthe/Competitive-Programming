class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        hashmap = {}

        for path in paths:
            single = path.split()
            dir = single[0] + "/"
            for i in single[1:]:
                idx = i.index("(")
                file = i[idx:-1]
                if file in hashmap:
                    hashmap[file].append(dir + i[:idx]) 
                else:
                    hashmap[file] = [dir + i[:idx]]
        ans = []
        for i in hashmap:
            if len(hashmap[i]) > 1:
                ans.append(hashmap[i])

        return ans