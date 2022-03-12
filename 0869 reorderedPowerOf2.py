"""
重新排序得到 2 的幂

给定正整数 N ，我们按任何顺序（包括原始顺序）将数字重新排序，注意其前导数字不能为零。
如果我们可以通过上述方式得到 2 的幂，返回 true；否则，返回 false。

示例 1：
输入：1
输出：true

示例 2：
输入：10
输出：false

示例 3：
输入：16
输出：true

示例 4：
输入：24
输出：false

示例 5：
输入：46
输出：true

提示：
* 1 <= N <= 10^9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reordered-power-of-2
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from collections import Counter


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        # 统计n的各字符数量，依次遍历2的幂并统计该数字各字符数量，比对一致则成功
        nStr = str(n)
        digitCount = len(nStr)
        nCounter = Counter(nStr)
        num = 1
        numStr = '1'
        while len(numStr) <= digitCount:
            if len(numStr) == digitCount and Counter(numStr) == nCounter:
                return True
            num *= 2
            numStr = str(num)
        return False


if __name__ == '__main__':
    s = Solution()

    r = s.reorderedPowerOf2(1)
    print(r)

    r = s.reorderedPowerOf2(10)
    print(r)

    r = s.reorderedPowerOf2(16)
    print(r)

    r = s.reorderedPowerOf2(24)
    print(r)

    r = s.reorderedPowerOf2(46)
    print(r)
