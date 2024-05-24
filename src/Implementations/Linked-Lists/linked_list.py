class Node:
    def __init__(self, element) -> None:
        self.element = element
        self.next = None

    def __str__(self):
        return f"{self.element}"

    def __repr__(self):
        return self.__str__()


class LinkedList:
    def __init__(self) -> str:
        self.count = 0
        self.head = None

    def push(self, element):
        node = Node(element)
        if self.head == None:
            self.head = node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = node
        self.count += 1

    def get_element_at(self, index):
        if index >= 0 and index <= self.count:
            current = self.head
            for i in range(index):
                if current is None:
                    break
                current = current.next
            return current
        return None

    def insert(self, element, index):
        if index >= 0 and index <= self.count:
            node = Node(element)
            if index == 0:
                current = self.head
                node.next = current
                self.head = node
            else:
                previous = self.get_element_at(index - 1)
                current = previous.next
                node.next = current
                previous.next = node
            self.count += 1
            return True
        return False

    def remove_at(self, index):
        if index >= 0 and index <= self.count:
            current = self.head
            if index == 0:
                self.head = current.next
            else:
                previous = self.get_element_at(index - 1)
                current = previous.next
                previous.next = current.next
            self.count += 1
            return current.element
        return None

    def remove(self, element):
        index = self.index_of(element)
        return self.remove_at(index)

    def index_of(self, element):
        current = self.head
        for i in range(self.size()):
            if current != None and element == current.element:
                return i
            current = current.next
        return -1

    def size(self):
        return self.count

    def clear(self):
        self.head = None
        self.count = 0


x = LinkedList()
x.push("Eze")
x.push("Rio")
x.push(10)

print(x.get_element_at(2))
print(x.index_of("Eze"))
