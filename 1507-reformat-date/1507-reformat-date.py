class Solution:
    def reformatDate(self, date: str) -> str:
        month=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        date=date.split(" ")[::-1]
        date[-1]=date[-1][:-2]
        date[-2]=str(month.index(date[-2])+1)
        if len(date[-2])<2:
            date[-2]="0"+date[-2]
        if len(date[-1])<2:
            date[-1]="0"+date[-1]
        return "-".join(date)
        