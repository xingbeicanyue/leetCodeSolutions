"""
最长公共子序列

给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列的长度。如果不存在公共子序列，返回 0 。

一个字符串的子序列是指这样一个新的字符串：
它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。

例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。

示例 1：
输入：text1 = "abcde", text2 = "ace"
输出：3
解释：最长公共子序列是 "ace" ，它的长度为 3 。

示例 2：
输入：text1 = "abc", text2 = "abc"
输出：3
解释：最长公共子序列是 "abc" ，它的长度为 3 。

示例 3：
输入：text1 = "abc", text2 = "def"
输出：0
解释：两个字符串没有公共子序列，返回 0 。

提示：
* 1 <= text1.length, text2.length <= 1000
* text1 和 text2 仅由小写英文字符组成。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-common-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 动态规划
        # 设S[i][j]为text1[:i]与text2[:j]的最长公共子序列长度
        # 如果text1[i] == text2[j]则S[i][j] = S[i-1][j-1]，否则S[i][j] = max(S[i-1][j], S[i][j-1])
        csLens = [int(text1[0] == text2[0])]
        for i in range(1, len(text2)):
            csLens.append(1 if csLens[-1] == 1 else int(text2[i] == text1[0]))
        for i in range(1, len(text1)):
            csLens2 = [1 if csLens[0] == 1 else int(text1[i] == text2[0])]
            for j in range(1, len(text2)):
                csLens2.append(csLens[j - 1] + 1 if text1[i] == text2[j] else max(csLens[j], csLens2[j - 1]))
            csLens = csLens2
        return csLens[-1]


if __name__ == '__main__':
    s = Solution()

    r = s.longestCommonSubsequence('abcde', 'ace')
    print(r)

    r = s.longestCommonSubsequence('abc', 'abc')
    print(r)

    r = s.longestCommonSubsequence('abc', 'def')
    print(r)
