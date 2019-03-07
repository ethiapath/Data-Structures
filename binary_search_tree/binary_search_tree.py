import time
class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    # print('inserting:', value)
    
    if (value < self.value):
      if (self.left):
        self.left.insert(value)
      else:
        self.left = BinarySearchTree(value)
    else:
      if (self.right):
        self.right.insert(value)
      else:
        self.right = BinarySearchTree(value)

  def contains(self, target):
    if (self.value == target):
      # print('found', target)
      return True
    # print('searching for', target)
    # print('contain rec', self.value, 'target', target, 'left', self.left.value, 'right', self.right.value)
    if (target < self.value):
      if (self.left is None):
        return False
      else:
        return self.left.contains(target)
    else:
      if (self.right is None):
        return False
      else:
        return self.right.contains(target)

  def inOrder(self):
    if self.left != None:
      self.left.inOrder()
    print(self.value)
    # time.sleep(0.5)
    if self.right != None:
      self.right.inOrder()

  def preOrder(self):
    print(self.value)
    if self.left != None:
      self.left.inOrder()
    if self.right != None:
      self.right.preOrder()

  def get_max(self):
    if self.right != None:
      return self.right.get_max()
    else:
      return self.value