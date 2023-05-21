class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        l=0
        i=0
        tmp=head
        while tmp != None:
            l+=1
            tmp=tmp.next
        tmp = head
        if l-n==0:
            return head.next
        while i<l-n-1:
            i+=1
            tmp=tmp.next
        tmp.next=tmp.next.next
        return head
