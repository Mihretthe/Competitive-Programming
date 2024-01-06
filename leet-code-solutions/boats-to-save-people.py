class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats=0
        l=0
        r=len(people)-1
        while l<=r:
            if l==r:
                boats+=1
                break
            elif people[l]+people[r]<=limit:
                l+=1
                r-=1
                boats+=1
            else:
                r-=1
                boats+=1
        return boats