class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        r = len(people) - 1
        boats_needed = 0

        while l <= r:
            if people[l] + people[r] > limit:
                boats_needed += 1
                r -= 1
            else:
                boats_needed += 1
                l += 1
                r -= 1

        return boats_needed


