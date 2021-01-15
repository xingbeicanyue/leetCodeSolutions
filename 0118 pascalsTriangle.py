"""
杨辉三角

给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:
输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/pascals-triangle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：数组
"""

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        result = [[1] * (i + 1) for i in range(numRows)]
        for i in range(2, numRows):
            for j in range(1, i):
                result[i][j] = result[i - 1][j - 1] + result[i - 1][j]
        return result


if __name__ == '__main__':
    s = Solution()
    r = s.generate(5)
    print(r)
