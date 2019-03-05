class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    print('inserting:', value)
    if value >= self.value:
      if self.right == None:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)
    else:
      if self.left == None:
        self.left = BinarySearchTree(value)
      else:
        self.left.insert(value)

  def contains(self, target):
    if self.value == target:
      print('found', target)
      return True

    print('contain rec', self.value, 'target', target, 'left', self.left.value, 'right', self.right.value)

    if target >= self.value:
      if self.right == None:
        return False
      else:
        self.right.contains(target)
    else:
      if self.left == None:
        return False
      else:
        self.left.contains(target)

  def inOrder(self):
    if self.left != None:
      self.left.inOrder()
    print(self.value)
    if self.right != None:
      self.right.inOrder()

  def get_max(self):
    if self.right == None:
      return self.value
    else:
      self.right.get_max()