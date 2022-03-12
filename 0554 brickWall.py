"""
砖墙

你的面前有一堵矩形的、由 n 行砖块组成的砖墙。这些砖块高度相同（也就是一个单位高）但是宽度不同。每一行砖块的宽度之和相等。

你现在要画一条自顶向下的、穿过最少砖块的垂线。如果你画的线只是从砖块的边缘经过，就不算穿过这块砖。
你不能沿着墙的两个垂直边缘之一画线，这样显然是没有穿过一块砖的。

给你一个二维数组 wall ，该数组包含这堵墙的相关信息。其中，wall[i] 是一个代表从左至右每块砖的宽度的数组。
你需要找出怎样画才能使这条线穿过的砖块数量最少，并且返回穿过的砖块数量。

示例 1：
        v
 * *-* *-* *
 *-*-* * *-*
 * *-*-* *-*
 *-* *-*-*-*
 *-*-* * *-*
 * *-*-* * *
输入：wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
输出：2

示例 2：
 v
 *
 *
 *
输入：wall = [[1],[1],[1]]
输出：3

提示：
* n == wall.length
* 1 <= n <= 10^4
* 1 <= wall[i].length <= 10^4
* 1 <= sum(wall[i].length) <= 2 * 10^4
* 对于每一行 i ，sum(wall[i]) 是相同的
* 1 <= wall[i][j] <= 2^31 - 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/brick-wall
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List
from collections import defaultdict


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        # 统计每个位置对应的垂线经过的间隔数，间隔数越大的位置穿过的砖块数越少
        height = len(wall)
        breaks = defaultdict(int)  # {坐标位置: 该位置的间隔数}
        for bricks in wall:
            pos = 0
            for i in range(len(bricks) - 1):
                pos += bricks[i]
                breaks[pos] += 1
        return height - max(breaks.values(), default=0)


if __name__ == '__main__':
    s = Solution()

    r = s.leastBricks([[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2], [1, 3, 1, 1]])
    print(r)

    r = s.leastBricks([[1], [1], [1]])
    print(r)
