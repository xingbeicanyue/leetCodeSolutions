"""
连接所有点的最小费用

给你一个points 数组，表示 2D 平面上的一些点，其中 points[i] = [xi, yi] 。
连接点 [xi, yi] 和点 [xj, yj] 的费用为它们之间的曼哈顿距离 ：|xi - xj| + |yi - yj| ，其中 |val| 表示 val 的绝对值。
请你返回将所有点连接的最小总费用。只有任意两点之间有且仅有一条简单路径时，才认为所有点都已连接。

示例 1：
        *
        |
        |
       |
       |
       |
      |
      |
      *------*
    /          \
  *              *
输入：points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
输出：20
解释：
我们可以按照上图所示连接所有点得到最小总费用，总费用为 20 。
注意到任意两个点之间只有唯一一条路径互相到达。

示例 2：
输入：points = [[3,12],[-2,5],[-4,1]]
输出：18

示例 3：
输入：points = [[0,0],[1,1],[1,0],[-1,1]]
输出：4

示例 4：
输入：points = [[-1000000,-1000000],[1000000,1000000]]
输出：4000000

示例 5：
输入：points = [[0,0]]
输出：0

提示：
* 1 <= points.length <= 1000
* -10^6 <= xi, yi <= 10^6
* 所有点 (xi, yi) 两两不同。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/min-cost-to-connect-all-points
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from queue import PriorityQueue
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = PriorityQueue()
        for i, p in enumerate(points):
            for j in range(i + 1, len(points)):
                edges.put((abs(p[0] - points[j][0]) + abs(p[1] - points[j][1]), i, j))
        disjointSet = [-1] * len(points)
        remainCount, result = len(points) - 1, 0
        while remainCount > 0:
            edge = edges.get()
            r1, r2 = self._getRoot(disjointSet, edge[1]), self._getRoot(disjointSet, edge[2])
            if r1 != r2:
                disjointSet[r2] = r1
                remainCount -= 1
                result += edge[0]
        return result

    def _getRoot(self, disjointSet: List[int], idx: int):
        """ 获取对应的根节点 """
        visiteds = []
        while disjointSet[idx] >= 0:
            visiteds.append(idx)
            idx = disjointSet[idx]
        for visited in visiteds:
            disjointSet[visited] = idx
        return idx


if __name__ == '__main__':
    s = Solution()
    r = s.minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]])
    print(r)
    r = s.minCostConnectPoints([[3, 12], [-2, 5], [-4, 1]])
    print(r)
    r = s.minCostConnectPoints([[0, 0], [1, 1], [1, 0], [-1, 1]])
    print(r)
    r = s.minCostConnectPoints([[-1000000, -1000000], [1000000, 1000000]])
    print(r)
    r = s.minCostConnectPoints([[0, 0]])
    print(r)
