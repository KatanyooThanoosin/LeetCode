class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:return head
        flag = False
        while head.next.val == head.val:
            while head.next.val == head.val:
                flag = True
                head=head.next
                if not head.next:
                    return None
            print(head)
            if flag:head=head.next
            if not head.next:return head   
        a,b = head,head.next
        while b:
            flag = False
            while b.next and b.next.val == b.val:
                b=b.next
                flag = True
            if flag:a.next=b.next
            if not flag:a=b
            b=b.next
        return head
