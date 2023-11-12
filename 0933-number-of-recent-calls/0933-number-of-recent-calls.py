class RecentCounter:

    def __init__(self):
        self.counter = []

    def ping(self, t: int) -> int:
        self.counter.append(t)
        for i in range(len(self.counter)):
            if self.counter[i] >= (t - 3000):
                n = len(self.counter)
                self.counter = self.counter[i:]
                return n - i


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)