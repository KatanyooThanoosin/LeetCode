class Solution:
    def swapPairs(self, head): 
        if head==None or head.next==None:return head
        t=head
        head=head.next
        t.next=head.next
        head.next=t
        while t.next!=None:
            if t.next.next==None:break
            a=t.next
            t.next=a.next
            a.next=t.next.next
            t.next.next=a
            t=a
        return head
