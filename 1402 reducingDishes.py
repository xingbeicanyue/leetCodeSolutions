"""
做菜顺序

一个厨师收集了他 n 道菜的满意程度 satisfaction ，这个厨师做出每道菜的时间都是 1 单位时间。
一道菜的「喜爱时间」系数定义为烹饪这道菜以及之前每道菜所花费的时间乘以这道菜的满意程度，也就是 time[i]*satisfaction[i]。
请你返回做完所有菜「喜爱时间」总和的最大值为多少。
你可以按任意顺序安排做菜的顺序，你也可以选择放弃做某些菜来获得更大的总和。

示例 1：
输入：satisfaction = [-1,-8,0,5,-9]
输出：14
解释：去掉第二道和最后一道菜，最大的喜爱时间系数和为 (-1*1 + 0*2 + 5*3 = 14) 。每道菜都需要花费 1 单位时间完成。

示例 2：
输入：satisfaction = [4,3,2]
输出：20
解释：按照原来顺序相反的时间做菜 (2*1 + 3*2 + 4*3 = 20)

示例 3：
输入：satisfaction = [-1,-4,-5]
输出：0
解释：大家都不喜欢这些菜，所以不做任何菜可以获得最大的喜爱时间系数。

示例 4：
输入：satisfaction = [-2,5,-1,0,3,-3]
输出：35

提示：
* n == satisfaction.length
* 1 <= n <= 500
* -10^3 <= satisfaction[i] <= 10^3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reducing-dishes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from bisect import bisect_left
from typing import List


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        # 贪心算法：从大到小依次添加直到无法提升满意总和
        satisfaction.sort()
        if len(satisfaction) == 0 or satisfaction[-1] <= 0:
            return 0
        pos = bisect_left(satisfaction, 0)
        value = sum(satisfaction[i] * (i + 1 - pos) for i in range(pos, len(satisfaction)))
        step = sum(satisfaction[pos:])
        for i in range(pos - 1, -1, -1):
            step += satisfaction[i]
            if step <= 0:
                break
            value += step
        return value


if __name__ == '__main__':
    s = Solution()
    r = s.maxSatisfaction([-1, -8, 0, 5, -9])
    print(r)
    r = s.maxSatisfaction([4, 3, 2])
    print(r)
    r = s.maxSatisfaction([-1, -4, -5])
    print(r)
    r = s.maxSatisfaction([-2, 5, -1, 0, 3, -3])
    print(r)
