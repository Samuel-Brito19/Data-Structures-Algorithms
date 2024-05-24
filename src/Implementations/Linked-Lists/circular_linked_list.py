class Node:
    def __init__(self, element) -> None:
        self.element = element
        self.next = None

    def __str__(self):
        return f"{self.element}"

    def __repr__(self):
        return self.__str__()


class CircularLinkedList:
    def __init__(self) -> None:
        self.count = 0
        self.head = None

    def get_element_at(self, index):
        if index >= 0 and index <= self.count:
            current = self.head
            for i in range(index):
                if current is None:
                    break
                current = current.next
            return current
        return None

    def push(self, element):
        node = Node(element)
        current
        if self.head is None:
            self.head = node
        else:
            current = self.get_element_at(len(self) - 1)
            current.next = node
        node.next = self.head
        self.count += 1

    def insert(self, element, index):
        if index >= 0 and index <= self.count:
            node = Node(element)
            current = self.head
            if index == 0:
                if self.head is None:
                    # if no node in list
                    self.head = node
                    node.next = self.head
                else:
                    node.next = current
                    current = self.get_element_at(self.size() - 1)
                    # update last element
                    self.head = node
                    current.next = self.head
            else:
                previous = self.get_element_at(index - 1)
                node.next = previous.next
                previous.next = node
            self.count += 1
            return True


x = CircularLinkedList()
x.insert("Arda Guler", 8)
print(x.get_element_at(8))
