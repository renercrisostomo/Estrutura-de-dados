class Node:
  def __init__(self, data=None, next=None):
    self.data = data
    self.next = next

  def setData(self, data):
    self.data = data
  
  def getData(self):
    return self.data
  
  def setNext(self, next):
    self.next = next

  def getNext(self):
    return self.next
  
  def hasNext(self):
    return self.next != None
  
class LinkedList(object):

  def __init__(self):
    self.length = 0
    self.head = None


  def setHead(self, Node):
    self.head = Node

  def getHead(self):
    return self.head
  
  def insertAtBeginning(self, data):
    newNode = Node()
    newNode.data = data
    if self.length == 0:
      self.head = newNode
    else:
      newNode.next = self.head
      self.head = newNode
    self.length += 1

  def insertAtGivenPosition(self, pos, data):
    if pos > self.length or pos < 0:
      return None
    else:
      if pos == 0:
        self.insertAtBeginning(data)
      else:
        if pos == self.length:
          self.insertAtEnd(data)
        else:
          newNode = Node()
          newNode.data = data
          count = 1
          current = self.head
          while count < pos-1:
            count +=1
            current = current.next
          newNode.next = current.next
          current.next = newNode
          self.length +=1


  def insertAtEnd(self, data):
    newNode = Node()
    newNode.data = data
    if ( self.length == 0 ):
      self.head = newNode
      self.length +=1
      return
    current = self.head
    while current.next != None:
      current = current.next
    current.next = newNode
    self.length +=1

  def deleteAtPosition(self,pos):
    count = 0
    currentNode = self.head
    previousNode = self.head

    if pos > self.length or pos <0:
      return None
    else:
      while currentNode.next!=None or count <pos:
        count = count+1
        if count == pos:
          previousNode.next=currentNode.next
          self.length-=1
          return
        else:
          previousNode=currentNode
          currentNode=currentNode.next


  def deleteFromBeginning(self):
    if self.length != 0:
      self.head = self.head.next
      self.length -=1

  def deleteFromEnd(self):
    if self.length != 0:
      currentNode = self.getHead()
      previousNode = self.getHead()
      while currentNode.next != None:
        previousNode = currentNode
        currentNode = currentNode.next
      previousNode.next = None
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

  def getNodeAtPosition(self, index):
    if self.length != 0:
      current = self.head
      i = 0
      while ( (current != None) and (i < index) ):
        current = current.next
        i += 1
      return current
    else:
      return None

  def getNodeAtPositionFromTail(self, index):
    if self.length != 0:
      current = slow = self.head
      
      count = 0
      while (count < index):
        current = current.next
        count += 1
        if current == None:
          print("slow está fora da lista")
          return slow.data
      while ( (current.next != None) ):
        current = current.next
        slow = slow.next
      print("valor de slow: %s"%(slow.data))
      
      return slow.data

  def printReverse(self, head):
    if head != None:
      self.printReverse(head.next)
      print(f"{head.data}", end=", ")

  def insertInOrder(self, data):
    if self.length == 0:
      self.insertAtBeginning(data)
    current = self.head
    count = 0
    previousNode = None
    while ( (current != None) and (current.data <= data) ):
      previousNode = current
      current = current.next
      count += 1
    else: 
      self.insertAtGivenPosition(count, data)
  
  def moveToHead(self, data):
    
    currentNode = self.head
    previousNode = self.head

    if self.length:
      while currentNode.next!=None:
        previousNode=currentNode
        currentNode=currentNode.next
        if currentNode.data == data: # corrigir e testar
          previousNode.next=currentNode.next

          return
  
  # def temCiclo(self): fazer e testar
  # def invert(self): fazer e testar

  # faltei a aula

  def invertDoisADois(self):

    curr = self.head
    while curr != None and curr.next != None:
      aux = curr.data
      curr.data = curr.next.data
      curr.next.data = aux
      curr = curr.next.next

  # def removeDuplicado(self):

  # def isPalindromo(self):




          

lista = LinkedList()
lista.insertAtEnd(1)
lista.insertAtEnd(2)
lista.insertAtEnd(3)
lista.insertAtEnd(4)
lista.insertAtEnd(5)
lista.insertAtEnd(6)

lista.print()
# lista.getNodeAtPositionFromTail(70)
# lista.printReverse(lista.head)
# lista.insertInOrder(6)
# lista.invertDoisADois()
lista.removeDuplicado()
lista.print()