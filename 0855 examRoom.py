"""
在考场里，一排有 N 个座位，分别编号为 0, 1, 2, ..., N-1 。

当学生进入考场后，他必须坐在能够使他与离他最近的人之间的距离达到最大化的座位上。
如果有多个这样的座位，他会坐在编号最小的座位上。(另外，如果考场里没有人，那么学生就坐在 0 号座位上。)

返回 ExamRoom(int N) 类，它有两个公开的函数：
其中，函数 ExamRoom.seat() 会返回一个 int （整型数据），代表学生坐的位置；
函数 ExamRoom.leave(int p) 代表坐在座位 p 上的学生现在离开了考场。
每次调用 ExamRoom.leave(p) 时都保证有学生坐在座位 p 上。

示例：
输入：["ExamRoom","seat","seat","seat","seat","leave","seat"], [[10],[],[],[],[],[4],[]]
输出：[null,0,9,4,2,null,5]
解释：
ExamRoom(10) -> null
seat() -> 0，没有人在考场里，那么学生坐在 0 号座位上。
seat() -> 9，学生最后坐在 9 号座位上。
seat() -> 4，学生最后坐在 4 号座位上。
seat() -> 2，学生最后坐在 2 号座位上。
leave(4) -> null
seat() -> 5，学生最后坐在 5 号座位上。
 
提示：
* 1 <= N <= 10^9
* 在所有的测试样例中 ExamRoom.seat() 和 ExamRoom.leave() 最多被调用 10^4 次。
* 保证在调用 ExamRoom.leave(p) 时有学生正坐在座位 p 上。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/exam-room
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：Ordered Map
"""

from bisect import bisect_left


class ExamRoom:

    def __init__(self, N: int):
        self._n = N
        self._seats = []  # [有人坐下的位置]

    def seat(self) -> int:
        seats = self._seats
        if len(seats) == 0:
            seats.append(0)
            return 0
        # 找到距离最远且最靠左的位置
        if seats[0] == 0:
            bestDist, bestIdx = 0, -1
        else:
            bestDist, bestIdx = self._seats[0], 0
        for i in range(1, len(seats)):
            curDist = (seats[i] - seats[i - 1]) // 2
            if curDist > bestDist:
                bestDist, bestIdx = curDist, seats[i - 1] + curDist
        if seats[-1] < self._n - 1:
            curDist = self._n - 1 - seats[-1]
            if curDist > bestDist:
                bestDist, bestIdx = curDist, self._n - 1
        # 更新数据
        seats.insert(bisect_left(seats, bestIdx), bestIdx)
        return bestIdx

    def leave(self, p: int) -> None:
        self._seats.remove(p)


if __name__ == '__main__':
    examRoom = ExamRoom(10)
    r = list()
    r.append(None)
    r.append(examRoom.seat())
    r.append(examRoom.seat())
    r.append(examRoom.seat())
    r.append(examRoom.seat())
    r.append(examRoom.leave(4))
    r.append(examRoom.seat())
    print(r)
