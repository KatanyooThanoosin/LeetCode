class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, h1, h2):
        h = None
        if h1==None and h2==None:return None
        elif h1==None:return h2
        elif h2==None:return h1
        elif h1.val<h2.val:
            h=ListNode(h1.val)
            h1=h1.next
        else:
            h=ListNode(h2.val)
            h2=h2.next
        tmp = h
        while h1 or h2:
            if not h1:
                tmp.next=h2
                h2=None
            elif not h2:
                tmp.next=h1
                h1=None  
            elif h1.val<h2.val:
                tmp.next=ListNode(h1.val)
                tmp = tmp.next
                h1=h1.next
            else:
                tmp.next=ListNode(h2.val)
                tmp = tmp.next
                h2=h2.next
        return h
