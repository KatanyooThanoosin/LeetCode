class Solution:
    def reverseKGroup(self, head, k):
        a=ListNode()
        x=ListNode()
        f=None
        t=a
        y=x
        c=0
        while head:
            if c<k:
                b=ListNode(head.val)
                b.next=x.next
                x.next=b
                if c==0:y=y.next
                c+=1
                f=x.next
                head=head.next
            if c==k:
                c=0
                t.next=x.next
                t=y
                x.next=None
                y=x
        print(f)
        while c!=0 and f:
            t.next=ListNode(f.val,t.next)
            f=f.next
        return a.next
