"""
字符串的排列

给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。
换句话说，第一个字符串的排列之一是第二个字符串的子串。

示例1:
输入: s1 = "ab" s2 = "eidbaooo"
输出: True
解释: s2 包含 s1 的排列之一 ("ba").

示例2:
输入: s1= "ab" s2 = "eidboaoo"
输出: False

注意：
1. 输入的字符串只包含小写字母
2. 两个字符串的长度都在 [1, 10,000] 之间

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutation-in-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：双指针、Sliding Window
"""

from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        missCharCounter = defaultdict(int)  # 未匹配的字符及个数
        for c in s1:
            missCharCounter[c] += 1
        missCount = len(s1)  # 未匹配的字符个数
        leftIdx = 0  # 滑动窗口的左侧下标
        for c in s2:
            missCharCounter[c] -= 1
            if missCharCounter[c] >= 0:
                missCount -= 1
                if missCount == 0:
                    return True
            else:
                while leftIdx < len(s2):
                    missCharCounter[s2[leftIdx]] += 1
                    leftIdx += 1
                    if s2[leftIdx - 1] == c:
                        break
                    missCount += 1
        return False


if __name__ == '__main__':
    s = Solution()
    r = s.checkInclusion('ab', 'eidbaooo')
    print(r)
    r = s.checkInclusion('ab', 'eidboaoo')
    print(r)
