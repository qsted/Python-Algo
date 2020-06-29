
'''
A sequence of numbers bi, when b1 <b2 <… <bS, 
we call this sequence ascending. 
For a given sequence (a1, a2, …, aN), 
we can get some ascending subsequences (ai1, ai2, …, aiK), 
where 1 <= i1 <i2 <… <iK <= N. For example, 
for the sequence (1, 7, 3, 5, 9, 4, 8), 
there are some ascending subsequences, 
such as (1, 7), (3, 4, 8) and so on. 
The longest length of these subsequences is 4, 
such as subsequences (1, 3, 5, 8).

Your task is to find the length of the longest ascending subsequence 
and the elements in this subsequence for a given sequence
'''
class Solution:
    def findLengthOfLCIS(self,arr):
        if not arr:
            return 0     #判断事都为空
        n = len(arr)
        m = [0] * n
        result = []
        for x in range(n - 2, -1, -1):
            for y in range(n - 1, x, -1):
                if arr[x] < arr[y] and m[x] <= m[y]:
                    m[x] += 1
            max_value = max(m)
            result = []
            for i in range(n):
                if m[i] == max_value:
                    result.append(arr[i])
                    max_value -= 1
        return result

if __name__ == "__main__":
    obj = Solution()
    st = [10, 4, 15, 8, 9, 13, 21, 33, 28, 90, 37, 40, 32, 1, 80, 20, 73, 66, 12, 36, 18]
    # st2 = [10, 9, 2, 5, 3, 7, 101, 18]
    # st3 = [1, 7, 3, 5, 9, 4, 8]
    result = obj.findLengthOfLCIS(st)
    # result2 = obj.findLengthOfLCIS(st2)
    # result3 = obj.findLengthOfLCIS(st3)
    print(result,len(result))
    # print(result2, len(result2))
    # print(result3, len(result3))
'''
[4, 8, 9, 13, 21, 33, 37, 40, 80] 9
[2, 5, 7, 101] 4
[1, 3, 5, 9] 4

'''



