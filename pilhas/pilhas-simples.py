class Node:
  def __init__(self, data=None, next=None):
    self.data = data
    self.next = next
  
class Stack():

  def __init__(self):
    self.length = 0
    self.head = None
  
  def add(self, data):
    count = 0
    dataLength = (len(data) if type(data) == list else 1)
      
    while count < dataLength:
      newNode = Node()
      newNode.data = (data[count] if type(data) == list else data)
      if self.length == 0:
        self.head = newNode
      else:
        newNode.next = self.head
        self.head = newNode
      self.length += 1
      count += 1

  def pop(self):
    if self.length != 0:
      self.head = self.head.next
      self.length -= 1

  def print(self):
    if self.length != 0:
      pos = 0
      current = self.head
      while current != None:        
        print("Node %d has value %s"%(pos, current.data))
        pos += 1
        if pos == self.length : return
        current = current.next

pilha = Stack()

pilha.add([3,4,5])

pilha.print()
pilha.pop()
pilha.print()