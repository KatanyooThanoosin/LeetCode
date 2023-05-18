class Solution:
    def reverse(self, x: int) -> int:
        if x==0:return x
        sign = int(x/abs(x))
        s = 0
        for i in str(int(x/sign))[::-1]:
            s*=10
            s+=int(i)
        s*=sign
        if (-2)**31<=s<=2**31-1:
            return s
        else : return 0
