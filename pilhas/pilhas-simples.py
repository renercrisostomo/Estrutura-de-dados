class Node:
  def __init__(self, data=None, next=None):
    self.data = data
    self.next = next
  
class Stack(list):

  def __init__(self, list):
    self.length = 0
    self.head = None
  
  def add(self, data):
    newNode = Node()
    newNode.data = data
    if self.length == 0:
      self.head = newNode
    else:
      newNode.next = self.head
      self.head = newNode
    self.length += 1

  def pop(self):
    if self.length != 0:
      self.head = self.head.next
      self.length -=1

  def print(self):
    if self.length != 0:
      pos = 0
      current = self.head
      while current != None:        
        print("Node %d has value %s"%(pos, current.data))
        pos +=1
        if pos == self.length : return
        current = current.next

pilha = Stack()

pilha.print()
pilha.print()