class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        a = capacity

        for i in range(len(plants)):
            if plants[i] <= a:
                steps += 1
            else:
                steps += i* 2 + 1
                a = capacity
            print(steps)
            a -= plants[i]

        return steps
