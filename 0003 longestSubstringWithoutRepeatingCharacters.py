"""
无重复字符的最长子串

给定一个字符串，请你找出其中不含有重复字符的最长子串的长度。

示例 1:
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
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是子串的长度，"pwke" 是一个子序列，不是子串。

示例 4:
输入: s = ""
输出: 0

提示：
* 0 <= s.length <= 5 * 10^4
* s 由英文字母、数字、符号和空格组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 方法1：动态规划
        # 遍历字符串，记录每个字符最后出现的下标
        # 对于每个下标i，若该字符之前最后出现的下标为j，则以i为结尾的最长子串M(i) = min(i-j, M(i-1)+1)
        lastPosDict = {}  # {字符: 最后出现的下标}
        result = curRes = 0
        for i, c in enumerate(s):
            curRes = min(i - lastPosDict.get(c, -1), curRes + 1)
            result = max(result, curRes)
            lastPosDict[c] = i
        return result

        # 方法2：滑动窗口
        # 记录窗口中的字符集合，移动右指针，若当前字符在窗口中则移动左指针直至该字符不在窗口中
        # 优化：如果记录了每个字符最后出现的下标，则可以直接将左指针跳跃至该下标+1处，不必循环并维护字符集合
        # 优化后的结果与动态规划相同
        # result = -1  # 为了减少计算，遍历过程中result的值比最终结果少1
        # lastPosDict = {}  # {字符: 最后出现的下标}
        # left = 0
        # for right, c in enumerate(s):
        #     if c in lastPosDict:  # 当前字符在窗口中，右移左指针
        #         left = max(left, lastPosDict[c] + 1)
        #     result = max(result, right - left)
        #     lastPosDict[c] = right
        # return result + 1


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
