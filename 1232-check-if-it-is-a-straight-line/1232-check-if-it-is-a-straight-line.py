class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates)<=2:
            return True
        a=set()
        for i in range(len(coordinates)-1):
            if (coordinates[i+1][0]-coordinates[i][0])!=0:
                a.add((coordinates[i+1][1]-coordinates[i][1])/(coordinates[i+1][0]-coordinates[i][0]))
            else:
                a.add("_")
        return len(a)==1
        