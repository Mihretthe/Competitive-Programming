class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        previous = self.getRow(rowIndex - 1)
        the_before = previous[:]

        
        for i in range(1, len(the_before)):
            the_before[i] += previous[i - 1]        
        the_before.append(1)

        return the_before

            
