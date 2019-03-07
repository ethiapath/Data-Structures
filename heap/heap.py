# import time
class Heap:
  def __init__(self, compare):
    self.storage = []
    self.length = 0
    self.compare = compare

  def insert(self, value):
    self.storage.append(value)
    self.length += 1
    self._bubble_up(len(self.storage)-1)

  def delete(self):
    # print('start delete', self.storage)
    # time.sleep(0.1)
    self._swap(0, len(self.storage)-1)
    # print(self.storage)
    max = self.storage.pop()
    self.length -= 1
    # print(self.storage)
    self._sift_down(0)
    return max

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    parent = self._get_parent_index(index)

    if self.compare(self.storage[index], self.storage[parent]):
      self._swap(parent, index)

    if parent <= 0:
      return
    else:
      self._bubble_up(parent)
    '''
    parent = self._get_parent_index(index)
    while(self._has_parent(index) and self._get_parent(index) < self.storage[index]):
      parent = self._get_parent_index(index)
      self._swap(index, self._get_parent_index(index))
      # self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index] 
      index = parent
    '''

  def _sift_down(self, index):
    # time.sleep(0.1)
    child = self._get_left_index(index)
    if child > len(self.storage)-1:
      return
    # print('index:', index, 'value:', self.storage[index], 'heap:', self.storage)
    # if right child exists then if it's greater set it as child
    # left = True
    if (child + 1 <= len(self.storage)-1) and self.compare(self.storage[child+1], self.storage[child]):
      child += 1
    
    # if not left:
    #   print('go right')
    # else:
    #   print('go left')

    if self.storage[index] < self.storage[child]:
      self._swap(index, child)
      self._sift_down(child)
    else:
      return

    '''
    while(self._has_left(index)):
      if self._get_right_child(index) > self._get_left_child(index):
        larger_child = self._get_right_index(index)
      else:
        larger_child = self._get_left_index(index)

      if self.storage[index] > self.storage[larger_child]:
        return
        break
      else:
        self._swap(index, larger_child)
        index = larger_child
    '''

  def _swap(self, a, b): # a and b are indexes
    self.storage[a],self.storage[b] = self.storage[b],self.storage[a]

  def _get_left_index(self, index):
    return (index*2)+1

  def _get_right_index(self, index):
    return (index*2)+2

  def _get_parent_index(self, index):
    return (index-1)//2

  def _has_left(self, index):
    return self._get_left_index(index) < self.length

  def _has_right(self, index):
    return self._get_right_index(index) < self.length

  def _has_parent(self, index):
    return self._get_parent_index(index) >= 0

  def _get_left_child(self, index):
    return self.storage[self._get_left_index(index)]

  def _get_right_child(self, index):
    return self.storage[self._get_right_index(index)]

  def _get_parent(self, index):
    return self.storage[self._get_parent_index(index)]