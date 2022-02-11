"""
直线上最多的点数

给你一个数组 points ，其中 points[i] = [xi, yi] 表示 X-Y 平面上的一个点。求最多有多少个点在同一条直线上。

示例 1：
输入：points = [[1,1],[2,2],[3,3]]
输出：3

示例 2：
输入：points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
输出：4

提示：
* 1 <= points.length <= 300
* points[i].length == 2
* -10^4 <= xi, yi <= 10^4
* points 中的所有点互不相同

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/max-points-on-a-line
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：几何、数组、哈希表、数学
"""

from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # 从右往左依次取点作为原点，剩余的点按照斜率排序，可以与原点连成一条线的点必然相邻
        # 该点计算完成后从数据中剔除，继续取最右侧的点作为下一个原点
        # 时间复杂度：O(n^2*lg(n))
        result = 0
        originPts = sorted(points)
        originPt = originPts.pop(-1)
        while len(originPts) > result:
            sortedPts = [(pt[0] - originPt[0], pt[1] - originPt[1]) for pt in originPts]
            sortedPts.sort(key=lambda x: x[1] / x[0] if x[0] != 0 else 100000)
            maxCount = curCount = 1
            for i in range(len(sortedPts) - 1):
                if sortedPts[i][0] * sortedPts[i + 1][1] == sortedPts[i][1] * sortedPts[i + 1][0]:
                    curCount += 1
                else:
                    maxCount, curCount = max(maxCount, curCount), 1
                    if len(sortedPts) <= i + result:
                        break
            result = max(result, maxCount, curCount)
            originPt = originPts.pop(-1)
        return result + 1


if __name__ == '__main__':
    s = Solution()

    r = s.maxPoints([[1, 1], [2, 2], [3, 3]])
    print(r)

    r = s.maxPoints([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]])
    print(r)
