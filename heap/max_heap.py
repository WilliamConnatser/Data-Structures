class Heap:
  def __init__(self):
    self.storage = []

  '''`insert` adds the input value into the heap;
      This method should ensure that the inserted value is
      in the correct spot in the heap'''
  def insert(self, value):
    #Append value to the array
    self.storage.append(value)
    #Bubble up the tree
    index = len(self.storage)-1
    self._bubble_up(index)

  '''`delete` removes and returns the 'topmost' value from the heap;
      this method needs to ensure that the heap property is
      maintained after the topmost element has been removed.'''
  def delete(self):
    topmost = self.storage[0]
    self.storage = self.storage[1:]
    self._sift_down(0)
    return topmost

  '''`get_max` returns the maximum value in the heap _in constant time_.'''
  def get_max(self):
    return self.storage[0]

  '''`get_size` returns the number of elements stored in the heap.'''
  def get_size(self):
    return len(self.storage)

  '''`_bubble_up` moves the element at the specified index "up" the heap
      by swapping it with its parent if the parent's value is less than
      the value at the specified index.'''
  def _bubble_up(self, index):
    if self._parent(index) and self._parent(index) < self.storage[index]:
      parent_index = index-1//2  
      self.storage[index, parent_index] = self.storage[parent_index,index]
      self._bubble_up(parent_index)
      self._sift_down(index) #Not sure if needed?

  '''`_sift_down` grabs the indices of this element's children and determines
    which child has a larger value. If the larger child's value is larger
    than the parent's value, the child element is swapped with the parent.'''
  def _sift_down(self, index):
    if self._left_child(index) and self._left_child(index) > self.storage[index]:
      left_child_index = 2*index+1
      self.storage[index],self.storage[left_child_index] = self.storage[left_child_index],self.storage[index]
      self._sift_down(left_child_index)
      self._bubble_up(index) #Not sure if needed?
    elif self._right_child(index) and self._right_child(index) > self.storage[index]:
      right_child_index = 2*index+2
      self.storage[index],self.storage[right_child_index] = self.storage[right_child_index],self.storage[index]
      self._sift_down(right_child_index)
      self._bubble_up(index) #Not sure if needed?

  def _parent(self, index):
    index = index-1//2
    if index >= 0 and index <= len(self.storage)-1:
      return self.storage[index]
    return None

  #Returns left child
  def _left_child(self, index):
    index = 2*index+1
    if index >= 0 and index <= len(self.storage)-1:
      return self.storage[index]
    return None

  #Returns right child
  def _right_child(self, index):
    index = 2*index+2
    if index >= 0 and index <= len(self.storage)-1:
      return self.storage[index]
    return None
