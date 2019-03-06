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
    self.length = 0
    # self.max = 0

  def add_to_head(self, value):
    # if value > self.max.value:
    #   self.max = value
    # if self.length == 0:
    #   self.head = self.tail = ListNode(value)
    if self.head == None:
      self.head = ListNode(value)
      if self.tail == None:
        self.tail = self.head

    else:
      self.head.insert_before(value)
      self.head = self.head.prev
    self.length += 1

  def remove_from_head(self):
    if self.head == None:
      return None

    # is_max = False
    # if self.head.value == self.max:
    #   is_max = True

    old_head = self.head
    if self.head.next:
      self.head = self.head.next
    head_value = old_head.value
    old_head.delete()
    # if is_max:
    #   self.max = _get_max_node_linear().value
    self.length -= 1
    return head_value


  def add_to_tail(self, value):
    # if value > self.max:
    #   self.max = value
    if self.length == 0:
      self.head = self.tail = ListNode(value)
    else:
      self.tail.insert_after(value)
      self.tail = self.tail.next
    self.length += 1

  def remove_from_tail(self):
    if self.tail == None:
      return None
    # is_max = False
    # if self.head.value == self.max:
    #   is_max = True
    tail_value = self.tail.value
    if self.tail.prev:
      self.tail = self.tail.prev
    if self.tail.next:
      self.tail.next.delete()
    # if is_max:
    #   self.max = _get_max_node_linear().value
    self.length -= 1
    return tail_value

  def move_to_front(self, node):
    node.delete()
    self.add_to_head(node.value)

  def move_to_end(self, node):
    node.delete()
    self.add_to_tail(node.value)

  def delete(self, node):

    pass
    
  def _get_max_node_linear(self):
    # get max becomes O(n)
    current_node = self.head
    max_node = ListNode(0)
    while current_node:
      if current_node.value > max_node.value:
        max_node = current_node
      current_node = current_node.next
    return max_node

  def get_max(self):
    # get max becomes O(n)
    return self._get_max_node_linear().value
