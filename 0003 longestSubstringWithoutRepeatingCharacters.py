"""
给定一个字符串，请你找出其中不含有重复字符的最长子串的长度。

示例 1:
输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是子串的长度，"pwke" 是一个子序列，不是子串。

示例 4:
输入: s = ""
输出: 0

提示：
* 0 <= s.length <= 5 * 10^4
* s 由英文字母、数字、符号和空格组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：哈希表、双指针、字符串、Sliding Window
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sIdx, result = 0, 0
        lastPosDict = {}  # {字符: 最后出现的下标}
        for i, c in enumerate(s):
            if c in lastPosDict and lastPosDict[c] >= sIdx:
                result = max(result, i - sIdx)
                sIdx = lastPosDict[c] + 1
            lastPosDict[c] = i
        return max(result, len(s) - sIdx)


if __name__ == '__main__':
    s = Solution()
    r = s.lengthOfLongestSubstring('abcabcbb')
    print(r)
    r = s.lengthOfLongestSubstring('bbbbb')
    print(r)
    r = s.lengthOfLongestSubstring('pwwkew')
    print(r)
    r = s.lengthOfLongestSubstring('')
    print(r)
