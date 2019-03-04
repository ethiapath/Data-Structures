class Link:
  def __init__(self, data, nextNode=None, prev=None):
    self.data = data
    self.next = nextNode
    self.prev = prev

class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    # a doubly Linked list
    self.head = None
    self.tail = None
    self.length = 0

  def enqueue(self, value):
	# set Link
    newLink = Link(value)
    self.size = self.size + 1
    if self.tail == None:
      self.tail = newLink
      if self.head == None:
        self.head = newLink
    else:
      print('self.tail: ', self.tail.data)
      newLink.prev = self.tail
      self.tail.next = newLink
      self.tail = newLink

  
  def dequeue(self):
    if self.head == None:
      return None
    print('self.head: ', self.head.data)
    value = self.head.data
    self.head = self.head.next
    if self.head != None:
      self.head.prev = None
    self.size -= 1
    return value

  def len(self):
    return self.size
