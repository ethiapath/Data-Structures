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

  def _print(self):
      outstr = ''
      if self.prev:
        outstr += str(self.prev.value) + ' <-prev | '
      outstr += 'current_node: ' + str(self.value)
      if self.next:
        outstr += ' | next-> ' + str(self.next.value)
      print(outstr)

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 0
    if node != None:
      self.length += 1
    # self.max = 0

  def add_to_head(self, value):
    if self.length == 0:
      self.head = self.tail = ListNode(value)

    else:
      print('adding', value, 'to head')
      self.head.insert_before(value)
      self.head = self.head.prev
    self.length += 1


  def add_to_tail(self, value):
    # if value > self.max:
    #   self.max = value
    if self.length == 0:
      self.head = self.tail = ListNode(value)

    else:
      print('adding', value, 'to tail')
      self.tail.insert_after(value)
      self.tail = self.tail.next
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

  def remove_from_tail(self):
    if self.tail == None:
      return None
    # is_max = False
    # if self.head.value == self.max:
    #   is_max = True
    old_tail = self.tail
    if self.tail.prev:
      self.tail = self.tail.prev
    if self.tail.next:
      self.tail.next.delete()
    tail_value = old_tail.value
    # if is_max:
    #   self.max = _get_max_node_linear().value
    self.length -= 1
    return tail_value

  def move_to_front(self, node):
    if node == self.head:
      return
    if node == self.tail:
      self.tail = self.tail.prev
    node.delete()
    self.add_to_head(node.value)

  def move_to_end(self, node):
    if node == self.tail:
      return
    if node == self.head:
      self.head = self.head.next
    node.delete()
    self.add_to_tail(node.value)

  def delete(self, node):

    pass
    
  def _get_max_node_linear(self):
    # get max becomes O(n)
    current_node = self.head
    max_node = ListNode(0)
    while current_node:
      current_node._print()
      if current_node.value > max_node.value:
        max_node = current_node
      current_node = current_node.next
    return max_node

  def get_max(self):
    # get max becomes O(n)
    return self._get_max_node_linear().value

  def _print(self):
    print('head:', self.head.value, 'tail:', self.tail.value)
    current_node = self.head
    while current_node != None:
      current_node._print()
      current_node = current_node.next
      '''
      outstr = ''
      if current_node.prev:
        outstr += str(current_node.prev.value) + ' <-prev | '
      outstr += 'current_node: ' + str(current_node.value)
      if current_node.next:
        outstr += ' | next-> ' + str(current_node.next.value)
      print(outstr)
      '''