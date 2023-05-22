class Solution:
    def mergeKLists(self, l) -> Optional[ListNode]:
        h=ListNode()
        t=h
        while len(l)!=0:
            if l[0]==None:
                l=l[1:]
                continue
            m=l[0].val
            mi=0
            for i in range(1,len(l)):

                if l[i] and l[i].val<m:
                   mi=i
                   m=l[i].val
            t.next=ListNode(m)
            t=t.next 
            l[mi]=l[mi].next
            if l[mi]==None:l.pop(mi)
        return h.next
