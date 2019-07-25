class Heap:
  def __init__(self):
    self.storage = []

  '''`insert` adds the input value into the heap;
      This method should ensure that the inserted value is
      in the correct spot in the heap'''
  def insert(self, value):
    #Append value to the array
    self.storage.append(value)
    #Bubble the value to the proper position in the tree
    self._bubble_up(len(self.storage)-1)

  '''`delete` removes and returns the 'topmost' value from the heap;
      this method needs to ensure that the heap property is
      maintained after the topmost element has been removed.'''
  def delete(self):
    if len(self.storage) > 2:
      self._swap(0,len(self.storage)-1)
      topmost = self.storage.pop()
      self._sift_down(0)
    elif len(self.storage) == 2:
      self._swap(0,len(self.storage)-1)
      topmost = self.storage.pop()
      self._sift_down(0) #unnecessary, but needed to pass the tests..
    elif len(self.storage) == 1:
      topmost = self.storage.pop()
    else:
      topmost = None
    return topmost

  '''`get_max` returns the maximum value in the heap _in constant time_.'''
  def get_max(self):
    if self.storage[0]:
      return self.storage[0]
    return None

  '''`get_size` returns the number of elements stored in the heap.'''
  def get_size(self):
    return len(self.storage)

  '''`_bubble_up` moves the element at the specified index "up" the heap
      by swapping it with its parent if the parent's value is less than
      the value at the specified index.'''
  def _bubble_up(self, index):
    parent = self._parent(index)
    
    if parent and parent["value"] < self.storage[index]:
      self._swap(parent["index"],index)      
      self._bubble_up(parent["index"])      

  '''`_sift_down` grabs the indices of this element's children and determines
    which child has a larger value. If the larger child's value is larger
    than the parent's value, the child element is swapped with the parent.'''
  def _sift_down(self, index):
    left_child = self._left_child(index)
    right_child = self._right_child(index)
    largest_index = index
    print(f"^^Sifting Down^^ \nCurrent Value={self.storage[index]} \nLeft Child={left_child} \nRight Child={right_child} \nHeap Before={self.storage}")
    if left_child and self.storage[largest_index] < left_child["value"]:
      largest_index = left_child["index"]
    if right_child and self.storage[largest_index] < right_child["value"]:
      largest_index = right_child["index"]
    if largest_index != index:
      self._swap(index,largest_index)
      print(f"Heap After= {self.storage} \n\n")
      self._sift_down(largest_index)
    else:
      print("\n\n")

  def _parent(self,index):
    computed_index = index-1
    computed_index = computed_index//2
    if computed_index < len(self.storage) and computed_index >= 0:
      return {
        "index": computed_index,
        "value": self.storage[computed_index]
      }
    else:
      return None
  
  def _left_child(self,index):
    computed_index = 2*index+1
    if computed_index < len(self.storage) and computed_index >= 0:
      return {
        "index": computed_index,
        "value": self.storage[computed_index]
      }
    else:
      return None

  def _right_child(self,index):
    computed_index = 2*index+2
    if computed_index < len(self.storage) and computed_index >= 0:
      return {
        "index": computed_index,
        "value": self.storage[computed_index]
      }
    else:
      return None

  def _swap(self,x,y):
    self.storage[x],self.storage[y] = self.storage[y],self.storage[x]