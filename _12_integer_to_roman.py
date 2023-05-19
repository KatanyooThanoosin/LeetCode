class Solution:
    def intToRoman(self, num: int) -> str:
        s="M"*(int(num/1000))
        num%=1000
        if num>=900:
            s+="CM"
            num-=900
        elif num>=500:
            s+="D"
            num-=500
        elif num>=400:
            s+="CD"
            num-=400
    
        s+="C"*int(num/100)
        num%=100
        if num>=90:
            s+="XC"
            num-=90
        elif num>=50:
            s+="L"
            num-=50
        elif num>=40:
            s+="XL"
            num-=40
        
        s+="X"*int(num/10)
        num%=10
        if num>=9:
            s+="IX"
            num-=9
        elif num>=5:
            s+="V"
            num-=5
        elif num>=4:
            s+="IV"
            num-=4
        return s+("I"*num)
