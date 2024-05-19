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


x = LinkedList()
x.push("Nazismo")
x.push("Rio")


print(x.get_element_at(1))
