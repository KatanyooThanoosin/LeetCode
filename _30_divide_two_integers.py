class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        a=0
        c=0
        x=abs(dividend)
        y=abs(divisor)
        ne = -1 if (dividend<0 and divisor>0) or (dividend>0 and divisor<0) else 1
        while x>=y:
            c=1
            d=y
            while x>=d:
                a+=c
                c+=c
                x-=d
                d+=d
        return max(min(2147483647,a*ne),-2147483648)
