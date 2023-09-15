class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur

    def add_after_node(self, key, data):
        cur = self.head
        while cur:
            if cur.next is None and cur.data == key:
                self.append(data)
                return
            elif cur.data == key:
                new_node = Node(data)
                nxt = cur.next
                cur.next = new_node
                new_node.next = nxt
                new_node.prev = cur
                nxt.prev = new_node
                return
            cur = cur.next

    def add_before_node(self, key, data):
        cur = self.head
        while cur:
            if cur.prev is None and cur.data == key:
                self.prepend(data)
                return
            elif cur.data == key:
                new_node = Node(data)
                prev_node = cur.prev
                prev_node.next = new_node
                new_node.prev = prev_node
                new_node.next = cur
                cur.prev = new_node
                return
            cur = cur.next

    def delete_node(self, node):
        cur = self.head
        while cur:
            if cur == node and cur == self.head:
                # Case 1:
                if not cur.next:
                    cur = None
                    self.head = None
                    return

                # Case 2:
                else:
                    nxt = cur.next
                    cur.next = None
                    nxt.prev = None
                    cur = None
                    self.head = nxt
                    return

            elif cur == node:
                # Case 3:
                if cur.next:
                    nxt = cur.next
                    prev = cur.prev
                    prev.next = nxt
                    nxt.prev = prev
                    cur.next = None
                    cur.prev = None
                    cur = None
                    return

                # Case 4:
                else:
                    prev = cur.prev
                    prev.next = None
                    cur.prev = None
                    cur = None
                    return
            cur = cur.next

    def reverse(self):
        tmp = None
        cur = self.head
        while cur:
            tmp = cur.prev
            cur.prev = cur.next
            cur.next = tmp
            cur = cur.prev
        if tmp:
            self.head = tmp.prev

    def remove_duplicates(self):
        hmap = dict()
        cur = self.head
        while cur:
            if cur.data in hmap:
                nxt = cur.next
                self.delete_node(cur)
                cur = nxt
            else:
                hmap[cur.data] = 1
                cur = cur.next

    def pairs_with_sum(self, sum_val):
        pairs = []
        cur = self.head
        if not cur:
            return pairs
        nxt = cur.next
        while nxt and cur:
            if cur.data + nxt.data == sum_val:
                pairs.append("(" + str(cur.data) + "," + str(nxt.data) + ")")
            if nxt.next is None:
                cur = cur.next
                nxt = cur
            nxt = nxt.next
        return pairs

    def print_list(self):
        cur = self.head
        boolean = True
        while cur:
            print(f"{'Prev <-' if boolean else ''} "
                  f"{cur.data} {'-> None' if cur.next is None else '⇄'}", end="")

            cur = cur.next
            boolean = False


doublyList = DoublyLinkedList()
# doublyList.append(1)
# doublyList.append(2)
# doublyList.append(3)
# doublyList.append(4)
# doublyList.append(5)

print(doublyList.pairs_with_sum(5))

doublyList.print_list()
