"""
计数质数

统计所有小于非负整数 n 的质数的数量。

示例 1：
输入：n = 10
输出：4
解释：小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。

示例 2：
输入：n = 0
输出：0

示例 3：
输入：n = 1
输出：0

提示：
* 0 <= n <= 5 * 106

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-primes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def countPrimes(self, n: int) -> int:
        # 线性筛法
        if n <= 2:
            return 0
        isPrimes = [1] * n  # 对应下标是否质数（1为质数，0为合数）
        primes = []  # [质数]
        for curNum in range(2, (n + 1) // 2):
            if isPrimes[curNum] == 1:
                primes.append(curNum)
            maxRate = (n - 1) // curNum
            for i in primes:
                if i > maxRate:
                    break
                isPrimes[curNum * i] = 0
                if curNum % i == 0:
                    break
        return sum(isPrimes) - 2  # 减去0, 1


if __name__ == '__main__':
    s = Solution()

    r = s.countPrimes(10)
    print(r)

    r = s.countPrimes(0)
    print(r)

    r = s.countPrimes(1)
    print(r)
