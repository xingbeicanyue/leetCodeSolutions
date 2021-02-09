"""
最长回文子串

给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。

示例 2：
输入: "cbbd"
输出: "bb"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：字符串、动态规划
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Manacher算法
        s = '#' + '#'.join(s) + '#'
        resultLen, resultSIdx = -1, -1
        radius = []  # 每个下标为中心的臂长
        lastPalindromeCenterIdx, lastPalindromeEndIdx = -1, -1  # 最右回文中心|右端下标
        for i, c in enumerate(s):
            if i < lastPalindromeEndIdx:
                startRadius = min(radius[lastPalindromeCenterIdx * 2 - i], lastPalindromeEndIdx - i) + 1
            else:
                startRadius = 1
            leftIdx, rightIdx = i - startRadius, i + startRadius
            while leftIdx >= 0 and rightIdx < len(s) and s[leftIdx] == s[rightIdx]:
                leftIdx -= 1
                rightIdx += 1
            leftIdx, rightIdx, curLen = leftIdx + 1, rightIdx - 1, rightIdx - leftIdx - 2

            if rightIdx > lastPalindromeEndIdx:
                lastPalindromeCenterIdx, lastPalindromeEndIdx = i, rightIdx
            radius.append(curLen // 2)
            if curLen > resultLen:
                resultLen, resultSIdx = curLen, leftIdx
        return ''.join(s[i] for i in range(resultSIdx, resultSIdx + resultLen + 1) if i % 2 == 1)


if __name__ == '__main__':
    s = Solution()
    r = s.longestPalindrome('babad')
    print(r)
    r = s.longestPalindrome('cbbd')
    print(r)
