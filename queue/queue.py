class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    # a list?
    self.storage = []
    self.length = 0

  def enqueue(self, item):
    self.length += 1
    self.storage.insert(0, item)
  
  def dequeue(self):
    if self.length == 0:
      return None
    self.length -= 1
    return self.storage.pop()

  def len(self):
    return self.length
