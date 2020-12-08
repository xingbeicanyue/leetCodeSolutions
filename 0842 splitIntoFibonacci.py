"""
给定一个数字字符串 S，比如 S = "123456579"，我们可以将它分成斐波那契式的序列 [123, 456, 579]。
形式上，斐波那契式序列是一个非负整数列表 F，且满足：
* 0 <= F[i] <= 2^31 - 1，（也就是说，每个整数都符合 32 位有符号整数类型）；
* F.length >= 3；
* 对于所有的0 <= i < F.length - 2，都有 F[i] + F[i+1] = F[i+2] 成立。
另外，请注意，将字符串拆分成小块时，每个块的数字一定不要以零开头，除非这个块是数字 0 本身。
返回从 S 拆分出来的任意一组斐波那契式的序列块，如果不能拆分则返回 []。

示例 1：
输入："123456579"
输出：[123,456,579]

示例 2：
输入: "11235813"
输出: [1,1,2,3,5,8,13]

示例 3：
输入: "112358130"
输出: []
解释: 这项任务无法完成。

示例 4：
输入："0123"
输出：[]
解释：每个块的数字不能以零开头，因此 "01"，"2"，"3" 不是有效答案。

示例 5：
输入: "1101111"
输出: [110, 1, 111]
解释: 输出 [11,0,11,11] 也同样被接受。
 
提示：
* 1 <= S.length <= 200
* 字符串 S 中只含有数字。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/split-array-into-fibonacci-sequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：贪心算法、字符串、回溯算法
"""


class Solution:
    def splitIntoFibonacci(self, S: str) -> list:
        if len(S) < 3:
            return []
        for i in range(1, min((len(S) - 1) // 2, 10) + 1):  # 最多10位，并且不会超过字符串长度的一半，下同
            if S[0] == '0' and i > 1:
                continue
            number1 = int(S[:i])
            leftCount = len(S) - i
            for j in range(1, min(leftCount - i, leftCount // 2, 10) + 1):
                if S[i] == '0' and j > 1:
                    continue
                number2 = int(S[i:i+j])
                result = self.checkFibonacci(S, number1, number2, i+j)
                if result:
                    return result
        return []

    def checkFibonacci(self, S: str, number1: int, number2: int, sIdx: int) -> list:
        """ 检查是否符合斐波那契数列
        :param S: 待检查的数字字符串
        :param number1: 斐波那契数列第一项
        :param number2: 斐波那契数列第二项
        :param sIdx: 从该下标开始检查，即该下标开始为第三项
        :returns: 返回斐波那契数列，若不符合则返回空列表
        """
        result = [number1, number2]
        while sIdx < len(S):
            nextNumber = number1 + number2
            if nextNumber >= 2147483648:
                return []
            nextNumberStr = str(nextNumber)
            if not S[sIdx:].startswith(nextNumberStr):
                return []
            result.append(nextNumber)
            sIdx += len(nextNumberStr)
            number1, number2 = number2, nextNumber
        return result


if __name__ == '__main__':
    s = Solution()
    result = s.splitIntoFibonacci('123456579')
    print(result)
    result = s.splitIntoFibonacci('11235813')
    print(result)
    result = s.splitIntoFibonacci('112358130')
    print(result)
    result = s.splitIntoFibonacci('0123')
    print(result)
    result = s.splitIntoFibonacci('1101111')
    print(result)
