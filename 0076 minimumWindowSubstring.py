"""
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。
如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。

注意：
* t 中可能有重复字符，子串至少需要相应数量的字符才能涵盖。
* 如果 s 中存在这样的子串，我们保证它是唯一的答案。

示例 1：
输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"

示例 2：
输入：s = "a", t = "a"
输出："a"

提示：
* 1 <= s.length, t.length <= 10^5
* s 和 t 由英文字母组成

进阶：你能设计一个在 o(n) 时间内解决此问题的算法吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-window-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：哈希表、双指针、字符串、Sliding Window
"""

from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 滑动窗口
        if len(s) < len(t):
            return ''
        minSubstrSIdx, minLen_2 = -1, len(s)
        leftIdx = 0
        missCount = len(t)  # 未匹配的字符数
        missCharCounter = defaultdict(int)  # 还需匹配的字符计数（过匹配为负数）
        for c in t:
            missCharCounter[c] += 1
        for rightIdx, c in enumerate(s):
            missCharCounter[c] -= 1
            missCount -= missCharCounter[c] >= 0
            if missCount == 0:  # 已经完全匹配，但可能有过匹配的字符，移动左指针
                while missCount == 0:
                    missCount += missCharCounter[s[leftIdx]] >= 0
                    missCharCounter[s[leftIdx]] += 1
                    leftIdx += 1
                if rightIdx - leftIdx < minLen_2:
                    minSubstrSIdx, minLen_2 = leftIdx - 1, rightIdx - leftIdx
        return s[minSubstrSIdx: minSubstrSIdx + minLen_2 + 2] if minSubstrSIdx >= 0 else ''


if __name__ == '__main__':
    s = Solution()
    r = s.minWindow('ADOBECODEBANC', 'ABC')
    print(r)
    r = s.minWindow('a', 'a')
    print(r)
