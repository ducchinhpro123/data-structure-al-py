class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def get_stack(self):
        return self.items

    def isEmpty(self):
        return self.items == []

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]

    def __len__(self):
        return len(self.items)


# Problem example of Stack
def is_match(top, paren):
    if top == "(" and paren == ")":
        return True
    elif top == "[" and paren == "]":
        return True
    elif top == "{" and paren == "}":
        return True
    else:
        return False


def is_paren_balanced(paren_string):
    s = Stack()
    is_balanced = True
    index = 0
    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        if paren in "[{(":
            s.push(paren)
        else:
            if s.isEmpty():
                is_balanced = False
                break
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False
                    break

        index += 1
    if s.isEmpty() and is_balanced:
        return True
    else:
        return False


def reverse_string(string):
    s = Stack()
    result = ""
    for letter in string:
        s.push(letter)

    while not s.isEmpty():
        result += s.pop()
    return result


# Another example convert integer to binary equivalent number
def convert_int_to_bin(dec_num):
    if dec_num == 0:
        return 0
    s = Stack()
    bin_num = ""

    # push bit to stack
    while dec_num > 0:
        s.push(dec_num % 2)
        dec_num //= 2

    # reverse bit -> get result
    while not s.isEmpty():
        bin_num += str(s.pop())

    return bin_num
