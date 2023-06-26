class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        tlen=0
        slen=-1
        i=j=0
        re=[]
        while j<len(words):
            while j<len(words) and slen+len(words[j])+1<=maxWidth:
                slen+=len(words[j])+1
                tlen+=len(words[j])
                j+=1
            if j==len(words):
                t=" ".join(words[i:])
                re.append(t+(" "*(maxWidth-len(t))))
                return re
            if j-i==1:
                re.append(words[i]+(" "*(maxWidth-tlen)))
                i=j
            else:
                s=" "*((maxWidth-tlen)//(j-i-1))
                c=(maxWidth-tlen)%(j-i-1)
                t=words[i]
                i+=1
                print(tlen)
                while i<j:
                    if c>0:
                        t+=" "
                        c-=1
                    t+=s+words[i]
                    i+=1
                re.append(t)
            tlen=0
            slen=-1
            j+1
        return re
