class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class ListaDupla:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def insertAtBeginninig(self, data):
        newNode = Node(data)
        if not self.head:
            self.head = self.tail = newNode
            self.length = 1
        else:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
            self.length += 1

    def insertAtEnd(self, data):
        newNode = Node(data)
        if not self.head:
            self.head = self.tail = newNode
            self.length = 1
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
            self.length += 1
    
    def insertAtGivingPosition(self, data, pos):
        newNode = Node(data)
        current = self.head
        if not self.head:
            self.head = self.tail = newNode
            self.length = 1
        elif pos == 1:
            self.insertAtBeginninig(data)
        elif pos == self.length:
            self.insertAtEnd(data)
        else:
            count = 1
            current = self.head
            while count != pos:
                current = current.next
                count += 1
                
            proximo = current.next
            anterior = current.prev

            proximo.prev = newNode
            newNode.next = proximo
            proximo = newNode

            anterior.next = newNode
            newNode.prev = anterior
            anterior = newNode

            self.length += 1

    def removeFromBeginninig(self):
        if not self.head:
            return None
        else:
            proximo = self.head.next
            self.head.next = None
            proximo.prev = None
            self.length -= 1
    
    def removeFromEnd(self):
        if not self.tail:
            return None
        else:
            anterior = self.tail.prev
            self.tail.prev = None
            anterior.next = None
            self.length -= 1

    def removeFromGivingPosition(self, pos):
        current = self.head
        if not self.head:
            return None
        elif pos == 1:
            self.removeFromBeginninig()
        elif pos == self.length:
            self.removeFromEnd()
        else:
            count = 1
            current = self.head
            while count != pos:
                current = current.next
                count += 1
                
            proximo = current.next
            anterior = current.prev

            current.next = None
            current.prev = None

            proximo.prev = anterior
            anterior.next = proximo

            self.length -= 1
    
    def printListaDupla(self):
        current = self.head
        while current.next:
            print(current.data, end=", ")
            current = current.next
        print(current.data)


ListaDupla.insertAtBeginninig(2)
ListaDupla.insertAtBeginninig(1)
ListaDupla.insertAtEnd(3)
ListaDupla.insertAtBeginninig(0)
ListaDupla.insertAtEnd(4)
ListaDupla.insertAtGivingPosition(6, 5)
ListaDupla.printListaDupla()