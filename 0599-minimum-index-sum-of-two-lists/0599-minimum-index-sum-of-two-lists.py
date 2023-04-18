class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        a=[]
        b=[]
        c=[]
        for i in list1:
            if i in list2:
                n=list((list1.index(i),list2.index(i)))
                a.append((sum(n),i))
        a.sort()
        z=a[0][0]
        for i in a:
            if i[0]==z:
                b.append(i[1])
        return b