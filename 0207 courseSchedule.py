"""
课程表

你这个学期必须选修 numCourse 门课程，记为 0 到 numCourse-1 。
在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们：[0,1]
给定课程总量以及它们的先决条件，请你判断是否可能完成所有课程的学习？

示例 1:
输入: 2, [[1,0]]
输出: true
解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。

示例 2
输入: 2, [[1,0],[0,1]]
输出: false
解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成课程 0；并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。

提示：
1. 输入的先决条件是由边缘列表表示的图形，而不是邻接矩阵。
2. 你可以假定输入的先决条件中没有重复的边。
3. 1 <= numCourses <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/course-schedule
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees, afters = [0] * numCourses, [[] for _ in range(numCourses)]
        for p in prerequisites:
            indegrees[p[0]] += 1
            afters[p[1]].append(p[0])
        canVisits = [i for i, indegree in enumerate(indegrees) if indegree == 0]
        while canVisits:
            numCourses -= 1
            curCourse = canVisits.pop()
            for after in afters[curCourse]:
                indegrees[after] -= 1
                if indegrees[after] == 0:
                    canVisits.append(after)
        return numCourses == 0


if __name__ == '__main__':
    s = Solution()
    r = s.canFinish(2, [[1, 0]])
    print(r)
    r = s.canFinish(2, [[1, 0], [0, 1]])
    print(r)
