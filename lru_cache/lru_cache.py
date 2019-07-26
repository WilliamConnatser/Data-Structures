from doubly_linked_list import DoublyLinkedList
from doubly_linked_list import ListNode

class LRUCache:
  def __init__(self, limit=10):
    self.limit = limit
    self.cache = {}


  """
  Retrieves the value associated with the given key. Also
  needs to move the key-value pair to the top of the order
  such that the pair is considered most-recently used.
  Returns the value associated with the key or None if the
  key-value pair doesn't exist in the cache. 
  """
  def get(self, key):
    if key in self.cache.keys():
      #If in cache
      current = self.keyChain.head
      while current.value != key:
        current = current.next
      self.keyChain.move_to_end(current)
      return self.cache[key]
    else:
      #If not in cache
      return None

  """
  Adds the given key-value pair to the cache. The newly-
  added pair should be considered the most-recently used
  entry in the cache. If the cache is already at max capacity
  before this entry is added, then the oldest entry in the
  cache needs to be removed to make room. Additionally, in the
  case that the key already exists in the cache, we simply 
  want to overwrite the old value associated with the key with
  the newly-specified value. 
  """
  def set(self, key, value):
    if len(self.cache.keys()) == 0:
      #If this is the first item in cache
      self.keyChain = DoublyLinkedList(ListNode(key))
      self.cache[key] = value
    elif key in self.cache.keys():
      #Else If this key is already in cache
      self.cache[key] = value
      current = self.keyChain.head
      while current.value != key:
        current = current.next
      self.keyChain.move_to_end(current)
    elif len(self.cache.keys()) == self.limit:
      #Else If the cache is at its limits
      del self.cache[self.keyChain.head.value]
      self.keyChain.remove_from_head()
      self.keyChain.add_to_tail(key)
      self.cache[key] = value

    else:
      #Else Neither of the above conditions are true
      #IE. Not first item in cache, key not already in cache, and the cache has not reached the limit
      self.keyChain.add_to_tail(key)
      self.cache[key] = value