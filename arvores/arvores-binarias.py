class Node:
  def __init__(self, data):
    self.data = data
    self.left = next
    self.right = None
    self.isLeft = False
  
  def setLeft(self, data):
    self.left = Node(data)
    self.isLeft = True

  def setRight(self, data):
    self.right = None(data)
    self.isLeft = False

  
class BinTree():

  def __init__(self, root = None):
    self.root = root

  def preOrder(self, root):
    if root == None:
      return
    print(root.data, sep="-->", end="-->")
    self.preOrder(root.left)
    self.preOrder(root.right)

  def inOrder(self, root):
    if root == None:
      return
    self.inOrder(root.left)
    print(root.data, sep="-->", end="-->")
    self.inOrder(root.right)

  def postOrder(self, root):
      if root == None:
        return
      self.postOrder(root.left)
      self.postOrder(root.right)
      print(root.data, sep="-->", end="-->")
  
  

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