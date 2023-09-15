from singly_linked_list.SinglyLinkedList import SinglyLinkedList


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        new_node = Node(data)
        cur = self.head
        if not self.head:
            self.head = new_node
            self.head.next = new_node
        else:
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
        self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head

    def remove(self, key):
        if self.head:
            if self.head.data == key:
                cur = self.head
                while cur.next != self.head:
                    cur = cur.next
                if self.head == self.head.next:
                    self.head = None
                else:
                    cur.next = self.head.next
                    self.head = self.head.next
            else:
                cur = self.head
                prev = None
                while cur.next != self.head:
                    prev = cur
                    cur = cur.next
                    if cur.data == key:
                        prev.next = cur.next
                        cur = cur.next

    def remove_node(self, node):
        if self.head == node:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            if self.head == self.head.next:
                self.head = None
            else:
                cur.next = self.head.next
                self.head = self.head.next
        else:
            cur = self.head
            prev = None
            while cur.next != self.head:
                prev = cur
                cur = cur.next
                if cur == node:
                    prev.next = cur.next
                    cur = cur.next

    def josephus_circle(self, step):
        cur = self.head

        length = len(self)
        while length > 1:
            count = 1
            while count != step:
                cur = cur.next
                count += 1
            print("KILL:" + str(cur.data))
            self.remove_node(cur)
            cur = cur.next
            length -= 1

    def __len__(self):
        count = 0
        cur = self.head
        while cur:
            cur = cur.next
            count += 1
            if cur == self.head:
                break
        return count

    def print_list(self):
        cur = self.head
        while cur:
            print(f"{cur.data} -> ", end="")
            if cur.next == self.head:
                print(f"{self.head.data}\n")
                break
            cur = cur.next

    def split_list(self):
        size = len(self)
        if size == 0:
            return None
        if size == 1:
            return self.head

        mid = size // 2
        count = 0
        prev = None
        cur = self.head
        while cur and count < mid:
            count += 1
            prev = cur
            cur = cur.next
        prev.next = self.head

        split_llist = CircularLinkedList()
        while cur.next != self.head:
            split_llist.append(cur.data)
            cur = cur.next

        split_llist.append(cur.data)

        self.print_list()
        split_llist.print_list()

    def is_circular_linked_list(self, input_list):
        cur = input_list.head
        while cur:
            if cur.next == input_list.head:
                return True
            cur = cur.next
        return False


circularLinkedList = CircularLinkedList()
circularLinkedList.append(1)
circularLinkedList.append(2)
circularLinkedList.append(3)
circularLinkedList.append(4)

circularList2 = CircularLinkedList()
singlyList = SinglyLinkedList()
singlyList.append(1)
singlyList.append(2)
singlyList.append(3)
print(circularList2.is_circular_linked_list(circularLinkedList))
