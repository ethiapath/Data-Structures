class link:
  def __init__(self, data, nextNode, prev):
    self.data = data
    self.next = nextNode
    self.prev = prev

class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    # a doubly linked list
    self.head = None
    self.tail = None
    self.length = 0

  def enqueue(self, link):
    # set link 
    link.prev = self.HEAD
    self.head.next = link
    self.head = link
    self.length += 1
    pass
  
  def dequeue(self):
    value = self.TAIL.data
    self.TAIL = self.TAIL.prev
    self.length -= 1
    return value
    pass

  def len(self):
    return self.length
    pass
