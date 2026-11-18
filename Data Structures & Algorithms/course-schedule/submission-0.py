from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        unlocks = [[] for _ in range(numCourses)]
        remaining = [0] * numCourses

        for a,b in prerequisites:
            unlocks[b].append(a)
            remaining[a] += 1

        queue = deque(i for i in range(numCourses) if remaining[i] == 0)
        done = 0

        while queue:
            c = queue.popleft()
            done += 1
            for x in unlocks[c]:
                remaining[x]-=1
                if remaining[x] == 0:
                    queue.append(x)

        return done == numCourses