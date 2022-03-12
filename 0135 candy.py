"""
分发糖果

n 个孩子站成一排。给你一个整数数组 ratings 表示每个孩子的评分。
你需要按照以下要求，给这些孩子分发糖果：
* 每个孩子至少分配到 1 个糖果。
* 相邻两个孩子评分更高的孩子会获得更多的糖果。
请你给每个孩子分发糖果，计算并返回需要准备的最少糖果数目。

示例 1:
输入: [1,0,2]
输出: 5
解释: 你可以分别给这三个孩子分发 2、1、2 颗糖果。

示例 2:
输入: [1,2,2]
输出: 4
解释: 你可以分别给这三个孩子分发 1、2、1 颗糖果。
     第三个孩子只得到 1 颗糖果，这已满足上述两个条件。

提示：
* n == ratings.length
* 1 <= n <= 2 * 10^4
* 0 <= ratings[i] <= 2 * 10^4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/candy
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        # 贪心
        # 从左到右遍历，如果ratings[i] > ratings[i-1]，则给i比i-1多一颗糖
        # 再从左到右遍历，如果ratings[i] > ratings[i+1]，则给i比i+1多一颗糖（如果比之前分配的少则不变）
        # 这样就可以同时满足左右两侧的要求
        candies = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        return sum(candies)


if __name__ == '__main__':
    s = Solution()

    r = s.candy([1, 0, 2])
    print(r)

    r = s.candy([1, 2, 2])
    print(r)
