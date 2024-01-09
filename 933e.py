from collections import deque

class RecentCounter:

    def __init__(self):
        self.requests = deque()

    def ping(self, t: int) -> int:
        self.requests.append(t)
        # RANGE WILL END ON THE RIGHT NUMBER
        curr_range = range(t-3000, t+1)

        while self.requests[0] not in curr_range:
            self.requests.popleft()

        return len(self.requests)