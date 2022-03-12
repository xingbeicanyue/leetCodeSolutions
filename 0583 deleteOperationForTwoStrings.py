"""
给定两个单词 word1 和 word2，找到使得 word1 和 word2 相同所需的最小步数，每步可以删除任意一个字符串中的一个字符。

示例：
输入: "sea", "eat"
输出: 2
解释: 第一步将"sea"变为"ea"，第二步将"eat"变为"ea"

提示：
* 给定单词的长度不超过500。
* 给定单词中的字符只含有小写字母。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/delete-operation-for-two-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 思路类似#72
        minDistances = list(range(len(word2) + 1))
        for i, c1 in enumerate(word1):
            lastDistance, minDistances[0] = minDistances[0], i + 1
            for j, c2 in enumerate(word2):
                minDistances[j + 1], lastDistance = min(lastDistance + (c1 != c2) * 2, minDistances[j + 1] + 1,
                                                        minDistances[j] + 1), minDistances[j + 1]
        return minDistances[-1]


if __name__ == '__main__':
    s = Solution()
    r = s.minDistance('sea', 'eat')
    print(r)
