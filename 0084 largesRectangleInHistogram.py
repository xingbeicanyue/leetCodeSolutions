"""
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
求在该柱状图中，能够勾勒出来的矩形的最大面积。
           __
        __|  |
       |  |  |
       |  |  |   __
  __   |  |  |__|  |
 |  |__|  |  |  |  |
 |_2|_1|_5|_6|_2|_3|

以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。
           __
        __|  |
       |//|//|
       |//|//|   __
  __   |//|//|__|  |
 |  |__|//|//|  |  |
 |__|__|//|//|__|__|

图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。

示例:
输入: [2,1,5,6,2,3]
输出: 10

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/largest-rectangle-in-histogram
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：栈、数组
"""

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        length = len(heights)
        if length == 0:
            return 0
        # 计算每根柱子向左/右拓展的范围（保持柱子高度不变）
        lefts, rights = [-1] * length, [length] * length  # 可以不需要rights
        limits = []  # 单调递增的栈，记录不同高度的边界下标
        for i in range(length):
            while limits:
                if heights[i] <= limits[-1][0]:
                    rights[limits.pop()[1]] = i
                else:
                    lefts[i] = limits[-1][1]
                    break
            limits.append((heights[i], i))
        return max((rights[i] - lefts[i] - 1) * heights[i] for i in range(len(heights)))


if __name__ == '__main__':
    s = Solution()
    r = s.largestRectangleArea([2, 1, 5, 6, 2, 3])
    print(r)
