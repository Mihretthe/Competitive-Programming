class RecentCounter:

    def __init__(self):
        self.counter = deque()
        

    def ping(self, t: int) -> int:
        self.counter.appendleft(t)
        while self.counter and self.counter[-1] < (t - 3000):
            self.counter.pop()

        return len(self.counter)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)