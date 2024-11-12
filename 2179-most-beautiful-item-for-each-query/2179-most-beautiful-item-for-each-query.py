class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        
        hashmap = defaultdict(lambda : 0)
        prices = []
        for price, beauty in items:
            prices.append(price)
            hashmap[price] = max(hashmap[price], beauty)
        prices.sort()

        for i in range(1, len(prices)):
            hashmap[prices[i]] = max(hashmap[prices[i - 1]], hashmap[prices[i]])

        answer = []
        for price in queries:
            index = bisect_left(prices, price)
            if index >= len(prices):
                index -= 1
            if index == 0 and prices[index] > price:
                answer.append(0)
                continue
            elif prices[index] > price:
                index -= 1

            

            answer.append(hashmap[prices[index]])

        return answer