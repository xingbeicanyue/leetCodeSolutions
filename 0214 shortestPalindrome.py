"""
最短回文串

给定一个字符串 s，你可以通过在字符串前面添加字符将其转换为回文串。找到并返回可以用这种方式转换的最短回文串。

示例 1：
输入：s = "aacecaaa"
输出："aaacecaaa"

示例 2：
输入：s = "abcd"
输出："dcbabcd"

提示：
* 0 <= s.length <= 5 * 104
* s 仅由小写英文字母组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shortest-palindrome
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：字符串
"""


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # 类似KMP，对s的逆序列匹配s，求最后的匹配
        # 计算nexts
        nexts, nextIdx = [0] * (len(s) + 1), 0
        for i in range(1, len(s)):
            if s[i] == s[nextIdx]:
                nexts[i + 1] = nextIdx = nextIdx + 1
            else:
                nexts[i + 1] = nextIdx = int(s[i] == s[0])
        # 匹配
        reversedS = s[::-1]
        sIdx, rsIdx = 0, 0
        while rsIdx < len(reversedS):
            if s[sIdx] == reversedS[rsIdx]:
                sIdx += 1
                rsIdx += 1
            elif sIdx == 0:
                rsIdx += 1
            else:
                sIdx = nexts[sIdx]
        # 添加前缀并返回
        return reversedS[0: len(reversedS) - sIdx] + s


if __name__ == '__main__':
    s = Solution()
    r = s.shortestPalindrome('aacecaaa')
    print(r)
    r = s.shortestPalindrome('abcd')
    print(r)
