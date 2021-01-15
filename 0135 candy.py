"""
分发糖果

老师想给孩子们分发糖果，有 N 个孩子站成了一条直线，老师会根据每个孩子的表现，预先给他们评分。
你需要按照以下要求，帮助老师给这些孩子分发糖果：
* 每个孩子至少分配到 1 个糖果。
* 相邻的孩子中，评分高的孩子必须获得更多的糖果。

那么这样下来，老师至少需要准备多少颗糖果呢？

示例 1:
输入: [1,0,2]
输出: 5
解释: 你可以分别给这三个孩子分发 2、1、2 颗糖果。

示例 2:
输入: [1,2,2]
输出: 4
解释: 你可以分别给这三个孩子分发 1、2、1 颗糖果。
     第三个孩子只得到 1 颗糖果，这已满足上述两个条件。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/candy
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：贪心算法
"""

from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        if len(ratings) <= 1:
            return len(ratings)
        result = 1
        lastValue = 1  # 上一个孩子获得的糖果数
        descendStartIdx = -1  # 单调递减区间开始下标，负数表示当前不是单调递减区间
        descendStartValue = -1  # 单调递减区间开始的糖果数
        for i in range(1, len(ratings)):
            curTrend = ratings[i] - ratings[i - 1]
            if curTrend == 0:
                lastValue = 1
                result += lastValue
                descendStartIdx = -1
            elif curTrend > 0:
                lastValue += 1
                result += lastValue
                descendStartIdx = -1
            else:
                if descendStartIdx < 0:
                    descendStartIdx = i - 1
                    descendStartValue = lastValue
                if lastValue == 1:  # 需要降低但已无法降低，需增加当前递减区间的每个值（除了首项）
                    result += (i - descendStartIdx)
                    if descendStartValue - 1 < i - descendStartIdx:  # 递减区间的首项也需增加
                        result += 1
                        descendStartValue += 1
                else:
                    lastValue = 1
                    result += lastValue
        return result


if __name__ == '__main__':
    s = Solution()
    r = s.candy([1, 0, 2])
    print(r)
    r = s.candy([1, 2, 2])
    print(r)
