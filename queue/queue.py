class Node:
  def __init__(self, value, nextNode=None):
    self.value = value
    self.next = nextNode

class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    # a list?
    # a singly linked list?
    self.head = None
    self.tail = None
    self.storage = []
    self.length = 0

  '''
  tail            head    .next
   __      __      __      __
  |  | -> |  | -> |  | -> |  |
   --      --      --      --
  '''
  def enqueue(self, item): # add to head
    self.length += 1
    if self.head == None:
      self.head = Node(item)
      if self.tail == None:
        self.tail = self.head
    else:
      self.head.next = Node(item)
      self.head = self.head.next

  '''
  temp    tail            head
   __      __      __      __
  |  | -> |  | -> |  | -> |  |
   --      --      --      --
  '''

  def dequeue(self): # remove from tail
    if self.length == 0:
      return None
    old_tail = self.tail
    self.tail = self.tail.next
    old_tail.next = None # remove ref for gc
    self.length -= 1
    return old_tail.value

  def len(self):
    return self.length