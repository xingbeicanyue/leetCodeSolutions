"""
漂亮数组

对于某些固定的 N，如果数组 A 是整数 1, 2, ..., N 组成的排列，使得：

对于每个 i < j，都不存在 k 满足 i < k < j 使得 A[k] * 2 = A[i] + A[j]。

那么数组 A 是漂亮数组。

给定 N，返回任意漂亮数组 A（保证存在一个）。

示例 1：
输入：4
输出：[2,1,4,3]

示例 2：
输入：5
输出：[3,1,2,5,4]

提示：
* 1 <= N <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/beautiful-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：数组、数学、分治
"""

from typing import List


class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        # 以形如下图的树型方式构造
        #              1
        #      2               3
        #   4      6       5       7
        # 8  12  10  14  9   13  11  15
        # ...

        def createArray(root, step: int) -> List[int]:
            """ 创建以root开始，step为步长的漂亮数组 """
            if root > n:
                return []
            doubleStep = step * 2
            result = createArray(root + step, doubleStep)
            result.append(root)
            result.extend(createArray(root + doubleStep, doubleStep))
            return result

        return createArray(1, 1)


if __name__ == '__main__':
    s = Solution()

    r = s.beautifulArray(4)
    print(r)

    r = s.beautifulArray(5)
    print(r)
