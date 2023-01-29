class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        t=None
        c=0
        i=l1
        j=l2
        while i!=None or j!=None or c!=0:
            if i==None:a=0
            else:
                a=i.val
                i=i.next
            if j==None:b=0
            else:
                b=j.val
                j=j.next
            s=a+b+c
            c=int(s/10)
            s=s%10
            t=ListNode(s)if t==None else ListNode(s,t)
        l=None
        while t!=None:
            l=ListNode(t.val,l)
            t=t.next
        return l
