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
    self.length = 1 if node is not None else 0

  def __len__(self):
    return self.length

  '''
    add_to_head
    Needs to handle two cases:
      1- List head == None
      2- List head != None
  '''
  def add_to_head(self, value):
    if self.head == None:
      node = ListNode(value)
      self.head = node
      self.tail = node
    else:
      self.head.insert_before(value)
      self.head = self.head.prev
    self.increment_len()

  '''
    remove_from_head
    Needs to handle 3 cases:
      1- List length == 0
      2- List length == 1
      3- List length > 1
  '''
  def remove_from_head(self):
    removed = None
    if self.head:
      removed = self.head.value
      if self.length == 1:
        self.head = None
        self.tail = None
      else:
        self.head.delete()
      self.decrement_len()
    return removed

  '''
    add_to_tail
    Needs to handle 2 cases:
      1- List length == 0
      2- List length >= 1
  '''
  def add_to_tail(self, value):
    if not self.tail:
      node = ListNode(value)
      self.head = node
      self.tail = node
    else:
      self.tail.insert_after(value)
      self.tail = self.tail.next
    self.increment_len()

  '''
    remove_from_tail
    Needs to handle 2 cases:
      1- List length == 0
      2- List length == 1
      3- List length > 1
  '''
  def remove_from_tail(self):
    removed = None
    if self.tail:
      removed = self.tail.value
      if self.length == 1:
        self.head = None
        self.tail = None
      else:
        self.tail.delete()
      self.decrement_len()
    return removed

  '''
    move_to_front
      Need to cover 2 possible conditions:
      1- Make sure the list length !== 0
      2- Make sure the node is not already in the front
  '''
  def move_to_front(self, node):
    if self.head and self.head != node:
      node.delete()
      self.head.insert_before(node.value)
      self.head = self.head.prev

  '''
    move_to_end
    Need to cover 2 possible conditions:
      1- Make sure the list length !== 0
      2- Make sure the node not already in the end
  '''
  def move_to_end(self, node):
    if self.tail and self.tail != node:
      node.delete()
      self.tail.insert_after(node.value)
      self.tail = self.tail.next

  '''
    delete
    Need to cover 5 possible conditions:
      1- List length == 0
      2- List length == 1
      3- Deleting the head node
      4- Deleting the tail node
      5- Deleting neither the head or the tail node (a node in the middle of the list)
  '''
  def delete(self, node):
    if self.head != None:
      if self.length == 1:
        self.head = None
        self.tail = None
      elif self.head == node:
        self.head = self.head.next
      elif self.tail == node:
        self.tail = self.tail.prev
      self.decrement_len()
  
  '''
    get_max
    Need to cover 2 conditions:
      1- List length == 0
      2- List length >= 1
  '''
  def get_max(self):
    if self.head:
      cursor = self.head # Cursor starts at the head. 
      max_value = cursor.value
      while cursor != self.tail:
        cursor = cursor.next
        if max_value < cursor.value: # Check if the new cursor location value is bigger.
          max_value == cursor.value
      return max_value
    return None

  def increment_len(self):
    self.length += 1
  
  def decrement_len(self):
    self.length -= 1