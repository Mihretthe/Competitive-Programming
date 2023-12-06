class Solution:
    def totalMoney(self, n: int) -> int:
        week = []
        for i in range(n):
            if len(week) >= 7:
                week.append(week[i - 7] + 1)
            else:
                if week:
                    week.append(week[-1] + 1)
                else:
                    week.append(1)
        
        
        return sum(week)
            
