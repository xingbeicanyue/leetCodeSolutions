"""
杨辉三角 II

给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:
输入: 3
输出: [1,3,3,1]

进阶：
你可以优化你的算法到 O(k) 空间复杂度吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/pascals-triangle-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # 优先降低空间复杂度，只用长度为rowIndex+1的列表
        # 其实每个位置的值都有公式，不需要双层循环
        result = [1] * (rowIndex + 1)
        for i in range(2, rowIndex + 1):
            for j in range(-i, -1):
                result[j] += result[j + 1]
        return result


if __name__ == '__main__':
    s = Solution()
    r = s.getRow(3)
    print(r)
