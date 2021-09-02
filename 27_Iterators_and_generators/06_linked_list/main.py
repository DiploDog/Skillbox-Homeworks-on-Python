class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def __str__(self):
        if self.first is not None:
            current = self.first
            out = '[' + str(current.value) + ' '
            while current.next is not None:
                current = current.next
                out += str(current.value) + ' '
            return out + ']'
        return '[]'

    def get(self, key):
        length = 0
        current = None
        if self.first is not None:
            current = self.first
            while key != length or current.next is not None:
                current = current.next
                length += 1
            if key == length: current = current.value
        return current

    def clear(self):
        self.__init__()

    def append(self, x):
        self.length += 1
        if self.first is None:
            self.last = self.first = Node(x, None)
        else:
            self.last.next = self.last = Node(x, None)

    def remove(self, i):
        if self.first is None:
            return
        curr = self.first
        count = 0
        if i == 0:
            self.first = self.first.next
            return
        while curr is not None:
            if count == i:
                if curr.next is None:
                    self.last = curr
                old.next = curr.next
                break
            old = curr
            curr = curr.next
            count += 1


my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)