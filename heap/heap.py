class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(self._get_length)

  def delete(self):
    root = self.storage[0]
    self.storage[0] = self.storage[self._get_length()]

    pass

  def get_max(self):
    # get max value
    largests_ele = self.storage[0]
    # move last value to front
    self.storage[0] = self.storage[self.get_size-1]

    pass

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    while(index > (self._get_length())//2):
      parent = self._get_parent_index(index)
      if (parent < self._get_length() and self.storage[index]>self.storage[parent]):
        # swap
        self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index] 
        index = parent
      else:
        break


  def _sift_down(self, index):
    top = self.storage[0]
    larger_child
    while index < self.get_max:

      left_child = self._get_left_index(index)
      right_child = self._get_right_index(index)

      if (right_child < self.get and self.storage[left_child] < self.storage[right_child])
        larger_child = right_child
      else:
        larger_child = left_child
      if top >= self.storage[larger_child]:
        break

      self.storage[index] = self.storage[larger_child]
      index = larger_child
    self.storage[index] = top

    pass

  def _get_length(self, index):
    return len(self.storage)-1

  def _get_left_index(self, index):
    return (index*2)+1

  def _get_right_index(self, index):
    return (index*2)+2

  def _get_parent_index(self, index):
    return index-1//2

