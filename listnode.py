class ListNode:
    def __init__(self, element, next = None):
        self.element = element
        self.next_ = next

class SingleList:
    def __init__(self):
        self.head = None

    def insert_head(self, ele):
        node = ListNode(ele)
        if self.head == None:
            self.head = node
        else:
            node.next_ = self.head
            self.head = node
    def insert_tail(self, ele):
        node = ListNode(ele)
        if self.head is None:
            self.head = node
        else:
            cur = self.head
            while cur.next_ is not None:
                cur = cur.next_
            cur.next_ = node
    def insert_general(self, pos:int, ele):
        node = ListNode(ele)
        if pos == 0:
            node.next_ = self.head
            self.head = node
        else:
            curNum = 0
            cur = self.head
            while curNum < pos - 1:
                cur = cur.next_
                curNum += 1
            node.next_ = cur.next_
            cur.next_ = node
    def length(self):
        count = 0
        cur = self.head
        while cur is not None:
            cur = cur.next_
            count += 1
        return count

    def delete(self, pos):
        if pos == 0:
            self.head = self.head.next_
        else:
            cnt = 0
            cur = self.head
            while cnt < pos - 1 :
                cnt += 1
                cur = cur.next_
            cur.next_ = cur.next_.next_



if __name__ == '__main__':
    s = SingleList()
    s.insert_head(1)
    s.insert_head(2)
    s.insert_head(3)
    s.insert_head(4)
    s.insert_head(5)
    s.insert_head(6)
    s.insert_head(7)
    print(s.length())
    print(s.head.next_.element)


