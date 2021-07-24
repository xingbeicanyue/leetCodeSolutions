"""
H 指数

给你一个整数数组 citations，其中 citations[i] 表示研究者的第 i 篇论文被引用的次数。计算并返回该研究者的 h指数。

h 指数的定义：h 代表“高引用次数”（high citations），
一名科研人员的 h 指数是指他（她）的 （n 篇论文中）总共有 h 篇论文分别被引用了至少 h 次。
且其余的 n - h 篇论文每篇被引用次数不超过 h 次。

例如：某人的 h 指数是 20，这表示他已发表的论文中，每篇被引用了至少 20 次的论文总共有 20 篇。

提示：如果 h 有多种可能的值，h 指数是其中最大的那个。

示例 1：
输入：citations = [3,0,6,1,5]
输出：3
解释：给定数组表示研究者总共有 5 篇论文，每篇论文相应的被引用了 3, 0, 6, 1, 5 次。
     由于研究者有 3 篇论文每篇至少被引用了 3 次，其余两篇论文每篇被引用不多于 3 次，所以她的 h 指数是 3。

示例 2：
输入：citations = [1,3,1]
输出：1

提示：
* n == citations.length
* 1 <= n <= 5000
* 0 <= citations[i] <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/h-index
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：数组、计数排序、排序
"""

from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # 反向排序，遍历，找到遍历数量<=数字的最大值
        # 时间复杂度：O(lg(n))
        sortedNumbers = sorted(citations, reverse=True)
        for i, number in enumerate(sortedNumbers):
            if i + 1 > number:
                return i
        return len(sortedNumbers)


if __name__ == '__main__':
    s = Solution()

    r = s.hIndex([3, 0, 6, 1, 5])
    print(r)

    r = s.hIndex([1, 3, 1])
    print(r)
