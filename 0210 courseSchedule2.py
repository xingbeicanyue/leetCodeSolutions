"""
课程表 II

现在你总共有 numCourses 门课需要选，记为 0 到 numCourses - 1。
给你一个数组 prerequisites ，其中 prerequisites[i] = [ai, bi] ，表示在选修课程 ai 前必须先选修 bi 。
例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示：[0,1] 。
返回你为了学完所有课程所安排的学习顺序。可能会有多个正确的顺序，你只要返回任意一种就可以了。如果不可能完成所有课程，返回一个空数组。

示例 1：
输入：numCourses = 2, prerequisites = [[1,0]]
输出：[0,1]
解释：总共有 2 门课程。要学习课程 1，你需要先完成课程 0。因此，正确的课程顺序为 [0,1] 。

示例 2：
输入：numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
输出：[0,2,1,3]
解释：总共有 4 门课程。要学习课程 3，你应该先完成课程 1 和课程 2。并且课程 1 和课程 2 都应该排在课程 0 之后。
因此，一个正确的课程顺序是 [0,1,2,3] 。另一个正确的排序是 [0,2,1,3] 。

示例 3：
输入：numCourses = 1, prerequisites = []
输出：[0]

提示：
* 1 <= numCourses <= 2000
* 0 <= prerequisites.length <= numCourses * (numCourses - 1)
* prerequisites[i].length == 2
* 0 <= ai, bi < numCourses
* ai != bi
* 所有[ai, bi] 互不相同

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/course-schedule-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from collections import deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 拓扑排序
        inDegrees = [0] * numCourses  # [节点i的入度]
        sideEnds = [[] for i in range(numCourses)]  # [起点为节点i的边的终点]
        for p in prerequisites:
            inDegrees[p[0]] += 1
            sideEnds[p[1]].append(p[0])

        result = []
        nodes = deque(i for i, inDegree in enumerate(inDegrees) if inDegree == 0)  # [入度为0的节点]
        while len(nodes) > 0:
            node = nodes.popleft()
            result.append(node)
            for sideEnd in sideEnds[node]:
                inDegrees[sideEnd] -= 1
                if inDegrees[sideEnd] == 0:
                    nodes.append(sideEnd)
        return result if len(result) == numCourses else []


if __name__ == '__main__':
    s = Solution()

    r = s.findOrder(2, [[1, 0]])
    print(r)

    r = s.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
    print(r)

    r = s.findOrder(1, [])
    print(r)
