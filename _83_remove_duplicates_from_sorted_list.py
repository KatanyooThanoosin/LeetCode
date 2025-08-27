class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        r = head
        a = head
        if not a: return head
        b = head.next
        while b:
            if a.val == b.val:
                a.next = b.next
            else:
                a = a.next
            b=b.next
        return r
