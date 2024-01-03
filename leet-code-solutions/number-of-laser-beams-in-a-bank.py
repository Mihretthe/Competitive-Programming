class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        count = 0
        contain = [bank[0].count('1')]


        for i in range(1,len(bank)):
            row = bank[i]
            c = row.count("1")
            count += (contain[-1] * c)
            if c > 0:
                contain.append(c)
            
        return count