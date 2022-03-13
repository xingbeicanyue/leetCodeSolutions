"""
计数二进制子串

给定一个字符串 s，统计并返回具有相同数量 0 和 1 的非空（连续）子字符串的数量，并且这些子字符串中的所有 0 和所有 1 都是成组连续的。
重复出现（不同位置）的子串也要统计它们出现的次数。

示例 1：
输入：s = "00110011"
输出：6
解释：6 个子串满足具有相同数量的连续 1 和 0 ："0011"、"01"、"1100"、"10"、"0011" 和 "01" 。
注意，一些重复出现的子串（不同位置）要统计它们出现的次数。
另外，"00110011" 不是有效的子串，因为所有的 0（还有 1 ）没有组合在一起。

示例 2：
输入：s = "10101"
输出：4
解释：有 4 个子串："10"、"01"、"10"、"01" ，具有相同数量的连续 1 和 0 。

提示：
* 1 <= s.length <= 10^5
* s[i] 为 '0' 或 '1'

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-binary-substrings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # 方法1：
        # 统计连续相同数字的长度，01等长子串个数为相邻两个长度的较小者
        # 例如 000011100 统计为 4,3,2，子串个数为 min(4,3)+min(3,2)=5
        preNumCount, curNumCount, result = 0, 1, 0
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                curNumCount += 1
            else:
                result += min(preNumCount, curNumCount)
                preNumCount, curNumCount = curNumCount, 1
        return result + min(preNumCount, curNumCount)

        # 方法2：动态规划
        # equal01Lens = [0] * len(s)  # [以对应下标结尾的01等长子串长度+1]
        # for i in range(1, len(s)):
        #     if s[i] != s[i - 1]:
        #         equal01Lens[i] = 3
        #     else:
        #         lastLen = equal01Lens[i - 1]
        #         if i - lastLen >= 0 and s[i] != s[i - lastLen]:
        #             equal01Lens[i] = lastLen + 2
        # return sum(len_ > 0 for len_ in equal01Lens)


if __name__ == '__main__':
    s = Solution()

    r = s.countBinarySubstrings('00110011')
    print(r)

    r = s.countBinarySubstrings('10101')
    print(r)
