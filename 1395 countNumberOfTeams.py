"""
统计作战单位数

n 名士兵站成一排。每个士兵都有一个独一无二的评分 rating 。
每 3 个士兵可以组成一个作战单位，分组规则如下：
* 从队伍中选出下标分别为 i、j、k 的 3 名士兵，他们的评分分别为 rating[i]、rating[j]、rating[k]
* 作战单位需满足： rating[i] < rating[j] < rating[k] 或者 rating[i] > rating[j] > rating[k] ，其中  0 <= i < j < k < n

请你返回按上述条件可以组建的作战单位数量。每个士兵都可以是多个作战单位的一部分。

示例 1：
输入：rating = [2,5,3,4,1]
输出：3
解释：我们可以组建三个作战单位 (2,3,4)、(5,4,1)、(5,3,1) 。

示例 2：
输入：rating = [2,1,3]
输出：0
解释：根据题目条件，我们无法组建作战单位。

示例 3：
输入：rating = [1,2,3,4]
输出：4

提示：
* n == rating.length
* 3 <= n <= 1000
* 1 <= rating[i] <= 10^5
* rating 中的元素都是唯一的

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-number-of-teams
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        # 思路：
        # 顺序遍历，统计之前访问过的比当前值小的值的个数，即为以当前值结尾的长度为2的递增序列个数inc2，保存下来
        # 比当前值小的值对应的inc2的总和，即为长度为3的递增序列个数，递减同理
        inc2s, dec2s = [0] * len(rating), [0] * len(rating)  # [以对应位置数据为结尾的长度为2的递增|减序列数]
        inc3 = dec3 = 0  # 长度为3的递增|减序列总数
        for i, rate in enumerate(rating):
            for j in range(i):
                if rating[j] < rate:
                    inc2s[i] += 1
                    inc3 += inc2s[j]
                else:
                    dec2s[i] += 1
                    dec3 += dec2s[j]
        return inc3 + dec3


if __name__ == '__main__':
    s = Solution()
    r = s.numTeams([2, 5, 3, 4, 1])
    print(r)
    r = s.numTeams([2, 1, 3])
    print(r)
    r = s.numTeams([1, 2, 3, 4])
    print(r)
