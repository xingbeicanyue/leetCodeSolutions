"""
替换后的最长重复字符

给你一个仅由大写英文字母组成的字符串，你可以将任意位置上的字符替换成另外的字符，总共可最多替换 k 次。
在执行上述操作后，找到包含重复字母的最长子串的长度。

注意：字符串长度 和 k 不会超过 10^4。

示例 1：
输入：s = "ABAB", k = 2
输出：4
解释：用两个'A'替换为两个'B',反之亦然。

示例 2：
输入：s = "AABABBA", k = 1
输出：4
解释：
将中间的一个'A'替换为'B',字符串变为 "AABBBBA"。
子串 "BBBB" 有最长重复字母, 答案为 4。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-repeating-character-replacement
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # 判断窗口[left, right]中s[left]是否满足要求
        # 如果满足，则更新结果，并更新右边界以尝试更大的窗口
        # 如果不满足，则同时更新左右边界再去判断，窗口不需要缩小
        # 当右边界到终点时，要考虑剩余元素为左边界的情况
        charCounts, left, right, result = defaultdict(int), 0, 0, 0
        while right < len(s):
            charCounts[s[right]] += 1
            leftCharCount = charCounts[s[left]]
            if leftCharCount + k >= right - left + 1:  # 满足要求，更新结果
                result = leftCharCount + k
            else:  # 不满足要求，更新左边界
                charCounts[s[left]] -= 1
                left += 1
            right += 1
        for i in range(left, len(s)):  # 此遍历不需要减去计数
            result = max(result, charCounts[s[i]] + k)
        return min(result, len(s))


if __name__ == '__main__':
    s = Solution()
    r = s.characterReplacement('ABAB', 2)
    print(r)
    r = s.characterReplacement('AABABBA', 1)
    print(r)
