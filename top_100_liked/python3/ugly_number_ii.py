from collections import deque
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        q = [deque() for _ in range(3)]
        for i in range(3):
            q[i].append(1)
        minn = None
        for i in range(n):
            minn = min(q[0][0], q[1][0], q[2][0])
            for j, v in enumerate([2, 3, 5]):
                if(q[j][0] == minn):
                    q[j].popleft()
                q[j].append(minn * v)
        return minn
