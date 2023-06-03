class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:return head
        le=1
        t=head
        while t.next:
            t=t.next
            le+=1
        i=le-(k%le)
        t.next=head
        while i>0:
            t=t.next
            i-=1
        head=t.next
        t.next=None
        return head
