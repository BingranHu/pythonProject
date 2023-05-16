class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class twoNumAdd:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # l1 = l1.head
        # l2 = l2.head
        # l3 = SingleList()
        # carry = 0
        # while l1 is not None and l2 is not None:
        #     sum = l1.element + l2.element + carry
        #     if sum >= 10:
        #         carry = 1
        #         sum -= 10
        #     else:
        #         carry = 0
        #     l3.insert_tail(sum)
        #     l1 = l1.next_
        #     l2 = l2.next_
        # while l1 is not None:
        #     sum = l1.element + carry
        #     if sum >= 10:
        #         carry = 1
        #         sum -= 10
        #     else:
        #         carry = 0
        #     l3.insert_tail(sum)
        #     l1 = l1.next_
        # while l2 is not None:
        #     sum = l2.element + carry
        #     if sum >= 10:
        #         carry = 1
        #         sum -= 10
        #     else:
        #         carry = 0
        #     l3.insert_tail(sum)
        #     l2 = l2.next_
        # if carry == 1:
        #     l3.insert_tail(1)
        # return l3
        l3 = ListNode(0)
        cur = l3
        carry = 0
        while l1 is not None or l2 is not None:
            x = l1.val if l1 is not None else 0
            y = l2.val if l2 is not None else 0
            sum = x + y + carry
            carry = sum // 10
            cur.next = ListNode(sum % 10)
            cur = cur.next
            if l1 is not None: l1 = l1.next
            if l2 is not None: l2 = l2.next
        if carry > 0:
            cur.next = ListNode(1)
        return l3.next





