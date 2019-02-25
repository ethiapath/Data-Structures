"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.max = 0

  def add_to_head(self, value):
    if value > self.max:
      self.max = value
    if self.head == None:
        newLinkNode = ListNode(value)
        self.head = newLinkNode
        # first node case
        if self.tail == None:
            self.tail = newLinkNode
    else:
        self.head.insert_before(value)
    return self.head.__dict__['value']

  def remove_from_head(self):
    if self.head == None:
        return None
    else:
        old_head = self.head
        self.head = self.head.__dict__['next']
        old_head.delete()
        return old_head.__dict__['value']

  def add_to_tail(self, value):
    if value > self.max:
      self.max = value
    if self.tail == None:
        newLinkNode = ListNode(value)
        self.tail = newLinkNode
        # first node case
        if self.head == None:
            self.head = newLinkNode
    else:
        self.tail.insert_after(value)
    return self.tail.value

  def remove_from_tail(self):
    if self.tail != None:
        old_tail = self.tail
        self.tail = self.tail.__dict__['prev']
        old_tail.delete()
        return old_tail.__dict__['value']
    else:
        return None

  def move_to_front(self, node):
    node.delete()
    self.head.insert_before(node)
    self.head = node
    return self.head.__dict__['value']

  def move_to_end(self, node):
    node.delete()
    self.tail.insert_after(node)
    self.tail = node
    return self.tail.__dict__['value']

  def delete(self, node):
    node.delete()

  def get_max(self):
    return self.max
  '''
    currentNode = self.head
    maxVal = 0
    while currentNode.next != None:
        if currentNode.value > maxVal:
            maxVal = currentNode.__dict__['value']
        currentNode = currentNode.__dict__['next']
    return maxVal
'''


dll = DoublyLinkedList(ListNode(2))
dll.add_to_head(3)
print(dll.head.value)

