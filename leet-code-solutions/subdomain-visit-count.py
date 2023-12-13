class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        hashmap = defaultdict(int)

        for domain in cpdomains:
            n, link = domain.split()
            n = int(n)
            
            for l in range(len(link) - 1, -1, -1):
                if link[l] == ".":
                    key = link[l + 1:]
                    hashmap[key] += n
            hashmap[link] += n
        ans = []

        for key, value in hashmap.items():
            ans.append(f"{value} {key}")

        return ans

                


