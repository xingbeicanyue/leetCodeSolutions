"""
Z 字形变换

将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。
比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：
P   A   H   N
A P L S I I G
Y   I   R
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。
请你实现这个将字符串进行指定行数变换的函数：
string convert(string s, int numRows);

示例 1：
输入：s = "PAYPALISHIRING", numRows = 3
输出："PAHNAPLSIIGYIR"

示例 2：
输入：s = "PAYPALISHIRING", numRows = 4
输出："PINALSIGYAHRPI"
解释：
P     I    N
A   L S  I G
Y A   H R
P     I

示例 3：
输入：s = "A", numRows = 1
输出："A"

提示：
* 1 <= s.length <= 1000
* s 由英文字母（小写和大写）、',' 和 '.' 组成
* 1 <= numRows <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zigzag-conversion
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：字符串
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        length, step = len(s), (numRows - 1) * 2
        resultChars = [s[i] for i in range(0, length, step)]
        for i in range(1, numRows - 1):
            off = step - i * 2
            for j in range(i, length, step):
                resultChars.append(s[j])
                if j + off < length:
                    resultChars.append(s[j + off])
        for i in range(numRows - 1, length, step):
            resultChars.append(s[i])
        return ''.join(resultChars)


if __name__ == '__main__':
    s = Solution()
    r = s.convert('PAYPALISHIRING', 3)
    print(r)
    r = s.convert('PAYPALISHIRING', 4)
    print(r)
    r = s.convert('A', 1)
    print(r)
