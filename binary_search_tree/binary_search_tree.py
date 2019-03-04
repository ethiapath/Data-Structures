class BinaryNode:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class BinarySearchTree:
  def __init__(self, root):
    self.root = BinaryNode(root)
    #self.value = value
    #self.left = None
    #self.right = None

  def insert(self, value):
    # current = self.root
    newNode = BinaryNode(value)
    return recInsert(self.root, newNode)

  def recInsert(self, current, newNode):
    if value < current.value:
      if current.left == None:
          current.left = newNode
          #break
      else:
          return recInsert(current.left, newNode)
          current = current.left
    else:
      if current.right == None:
          current.right = newNode
          #break
      else:
          return recInsert(current.right, newNode)
          current.right = newNode

  def contains(self, target):
    return recFind(target, self.root)

  def recFind(self, value, node):
    if node.value == value:
      return True
    if node == None:
      return False
    if value < node.value:
      return recFind(value, node.left)
    else:
      return recFind(value, node.right)


  def get_max(self):
    pass
