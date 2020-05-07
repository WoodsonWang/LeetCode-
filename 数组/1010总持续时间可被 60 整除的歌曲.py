from typing import List

'''
在Python中，None、空列表[]、空字典{}、空元组()、0等一系列代表空和无的对象会被转换成False。除此之外的其它对象都会被转化成True。
'''
class Solution1:
    '''运行时间超时'''
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = 0
        for i in range(len(time)):
            for j in range(i + 1, len(time)):
                if (time[i] + time[j]) % 60 == 0:
                    count += 1
                    print(time[i], time[j])
        return count

# 运行成功
class Solution2:
    '''使用余数法
        remainder 余数

    '''
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = 0
        dic = {}
        for t in time:
            r = t%60
            if dic.get(r) is not None:
                dic[r] += 1
            else:
                dic[r] = 1
        for i in range(1,31):
            if dic.get(i) and dic.get(60-i):
                if i == 0 or i == 30:
                    count += (dic.get(i)*(dic.get(i)-1)) // 2
                else:
                    count += dic.get(i) * dic.get(60-i)
        if dic.get(0):
            count += (dic.get(0)*(dic.get(0)-1)) // 2
        return count


if __name__ == '__main__':


    sol = Solution2()
    print(sol.numPairsDivisibleBy60(time=[60,120,60]))
