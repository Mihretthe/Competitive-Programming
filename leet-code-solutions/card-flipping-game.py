class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        can  = set()
        cant = set()

        for front, back in zip(fronts, backs):
            if front == back:
                if front in can:
                    can.remove(front)
                    
                cant.add(front)
                continue
            if front not in cant:
                can.add(front)
            if back not in cant:
                can.add(back)

        if can:
            can = list(can)
            can.sort()
            return can[0]

        return 0
                