class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        length = len(prices)
        stack = []

        for i in range(length):
            while stack and prices[stack[-1]] >= prices[i]:
                prices[stack.pop()] -= prices[i]

            stack.append(i)
        
        return prices

        