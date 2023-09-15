class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        self.size += 1
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        # insert at the end of the list
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("The node doesn't exist")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        self.size += 1

    def delete_node(self, data):
        curr_node = self.head
        if curr_node and curr_node.data == data:
            self.head = curr_node.next
            curr_node = None
            self.size -= 1
            return
        prev = None
        while curr_node and curr_node.data != data:
            prev = curr_node
            curr_node = curr_node.next
        if curr_node is None:
            return

        prev.next = curr_node.next
        curr_node = None
        self.size -= 1

    def delete_at_pos(self, pos):
        if self.head:
            curr_node = self.head
            if pos == 0:
                head = curr_node.next
                curr_node = None
                self.size -= 1
                return

            prev = None
            count = 0
            while curr_node and count != pos:
                prev = curr_node
                curr_node = curr_node.next
                count += 1

            if curr_node is None:
                return
            prev.next = curr_node.next
            curr_node = None
            self.size -= 1

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    def print_list(self):
        cur_node = self.head
        while cur_node:
            if cur_node.next is None:
                print(f"{cur_node.data} -> None", end='\n')
                return
            print(f"{cur_node.data} -> ", end='')
            cur_node = cur_node.next

    def swap_node(self, key_1, key_2):
        if key_1 == key_2:
            return

        prev_1 = None
        curr_1 = self.head
        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next

        prev_2 = None
        curr_2 = self.head
        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next

        if not curr_1 or not curr_2:
            return

        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2

        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1

        curr_1.next, curr_2.next = curr_2.next, curr_1.next

    def reverse_iterative(self):
        prev = None
        curr = self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev

    def reverse_recursive(self):
        def _reverse_recursive(curr, prev):
            if not curr:
                return prev

            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            return _reverse_recursive(curr, prev)

        self.head = _reverse_recursive(curr=self.head, prev=None)

    def merge_sorted(self, llist):
        p = self.head
        q = llist.head
        s = None
        new_head = None
        if not p:
            return
        if not q:
            return

        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s
        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        if p:
            s.next = p
        if q:
            s.next = q
        self.head = new_head
        return self.head

    def remove_duplicate(self):
        cur = self.head
        prev = None
        dub_values = dict()
        while cur:
            if cur.data in dub_values:
                prev.next = cur.next
                self.size -= 1
                cur = None

            else:
                dub_values[cur.data] = 1
                prev = cur
            cur = prev.next

    def count_occurences_iterative(self, n):
        count = 0
        cur = self.head
        while cur:
            if cur.data == n:
                count += 1
            cur = cur.next
        return count

    def count_occurences_recursive(self, n):
        cur = self.head

        def inner_count_recursive(node, data):
            if not node:
                return 0
            if node.data == data:
                return 1 + inner_count_recursive(node.next, data)
            else:
                return inner_count_recursive(node.next, data)

        return inner_count_recursive(cur, n)

    def rotate(self, k):
        if self.head and self.head.next:
            p = self.head
            q = self.head
            prev = None
            count = 0
            while p and count < k:
                prev = p
                p = p.next
                count += 1
            p = prev
            while q:
                prev = q
                q = q.next
            q = prev

            q.next = self.head
            self.head = p.next
            p.next = None

    def print_nth_from_last(self, n, method=1):
        if method == 1:
            cur = self.head
            total_len = self.get_size()
            while cur:
                if total_len == n:
                    print(f"{n}th to the last node is: {cur.data}")
                    return cur.data
                total_len -= 1
                cur = cur.next
            if cur is None:
                return

        elif method == 2:
            p = self.head
            q = self.head
            if n > 0:
                count = 0
                while q:
                    count += 1
                    if count >= n:
                        break
                    q = q.next
                if not q:
                    print(f"{n} is greater than the number of nodes in list.")
                    return
                while p and q.next:
                    p = p.next
                    q = q.next
                print(p.data)
                return p.data
            else:
                return None

    def is_palindrome(self, method=1):
        # solution 1 using string
        if method == 1:
            s = ""
            p = self.head
            while p:
                s += p.data
                p = p.next
            return s == s[::-1]

        # solution 2:using stack
        elif method == 2:
            s = []
            p = self.head
            while p:
                s.append(p.data)
                p = p.next
            p = self.head
            while p:
                data = s.pop()
                if data != p.data:
                    return False
                p = p.next
            return True
        elif method == 3:
            if self.head:
                p = self.head
                q = self.head
                prev = []

                # move q pointer to the last node of the list
                i = 0
                while q:
                    prev.append(q.data)
                    q = q.next
                    i += 1

                count = 1
                while count <= i // 2 + 1:
                    if prev[-count] != p.data:
                        return False
                    p = p.next
                    count += 1
                return True
            else:
                return True

    def move_tail_to_head(self):
        p = self.head
        prev = None
        while p.next:
            prev = p
            p = p.next

        prev.next = None
        p.next = self.head
        self.head = p

    def sum_two_list(self, llist):
        result = SinglyLinkedList()
        p = self.head
        q = llist.head
        carry = 0
        while p or q:
            x = p.data if p else 0
            y = q.data if q else 0

            _sum = x + y + carry
            carry = _sum // 10

            result.append(_sum % 10)
            if p:
                p = p.next
            if q:
                q = q.next
        if carry > 0:
            result.append(carry)
        return result


# llist = SinglyLinkedList()
# llist.append(5)
# llist.append(6)
# llist.append(3)
#
# llist_2 = SinglyLinkedList()
# llist_2.append(8)
# llist_2.append(4)
# llist_2.append(2)
#
# list_3 = llist.sum_two_list(llist_2)
# list_3.print_list()
