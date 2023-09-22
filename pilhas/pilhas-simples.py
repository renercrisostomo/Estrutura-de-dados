class Node:
  def __init__(self, data=None, next=None):
    self.data = data
    self.next = next
  
class Stack():

  def __init__(self):
    self.length = 0
    self.head = None
  
  def push(self, data):
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

# def ExpresaoParaPosfixa():

def calcular(c, op1, op2):
  if c == '+': return op1 + op2
  elif c == '-': return op1 - op2
  elif c == '*': return op1 * op2
  elif c == '/': return op1 / op2

def resultadoExpressaoPosfixa(posfixa):
  pilha = Stack()
  for c in posfixa:
    if c in '+-*/':
      op1 = pilha.pop()
      op2 = pilha.pop()
      pilha.push(calcular(c, op1, op2))
    else:
      pilha.push(int(c))

def transform(c, op1, op2):
  return ['(', op1, c, op2, ')']

def posfixaParaInfixa(posfixa):
  pilha = Stack()
  for c in posfixa:
    if c in '+-*/':
      op1 = pilha.pop()
      op2 = pilha.pop()
      pilha.push(transform(c, op1, op2))
    else:
      pilha.push(c)

posfixa = '59+'
print(resultadoExpressaoPosfixa(posfixa))
print(posfixaParaInfixa(posfixa))

# pilha = Stack()
# pilha.push([3,4,5])

# pilha.print()
# pilha.pop()
# pilha.print()