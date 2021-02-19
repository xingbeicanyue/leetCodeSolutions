"""
编辑距离

给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。
你可以对一个单词进行如下三种操作：
* 插入一个字符
* 删除一个字符
* 替换一个字符

示例 1：
输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')

示例 2：
输入：word1 = "intention", word2 = "execution"
输出：5
解释：
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')

提示：
* 0 <= word1.length, word2.length <= 500
* word1 和 word2 由小写英文字母组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/edit-distance
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：字符串、动态规划
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        lastDistances = list(range(len(word2) + 1))
        for i, c1 in enumerate(word1):
            curDistances = [i + 1]
            for j, c2 in enumerate(word2):
                curDistances.append(min(lastDistances[j] + (c1 != c2), lastDistances[j + 1] + 1, curDistances[-1] + 1))
            lastDistances = curDistances
        return lastDistances[-1]


if __name__ == '__main__':
    s = Solution()
    r = s.minDistance('horse', 'ros')
    print(r)
    r = s.minDistance('intention', 'execution')
    print(r)
