class Stack (object):
  def __init__ (self):
    self.stack = []

  # add an item to the top of the stack
  def push (self, item):
    self.stack.append ( item )

  # remove an item from the top of the stack
  def pop (self):
    return self.stack.pop()

  # check what item is on top of the stack without removing it
  def peek (self):
    return self.stack[len(self.stack) - 1]

  # check if a stack is empty
  def isEmpty (self):
    return (len(self.stack) == 0)

  # return the number of elements in the stack
  def size (self):
    return (len(self.stack))
# a different implementation of the Stack class
class Stack (object):
  def __init__ (self):
    self.stack = []

  def push (self, item):
    self.stack.insert (0, item )

  def pop (self):
    return self.stack.pop(0)

  def peek (self):
    return self.stack[0]

  def isEmpty (self):
    return (len(self.stack) == 0)

  def size (self):
    return (len(self.stack))
class Queue (object):
  def __init__ (self):
    self.queue = []

  def enqueue (self, item):
    self.queue.append (item)

  def dequeue (self):
    return (self.queue.pop(0))

  def isEmpty (self):
    return (len (self.queue) == 0)

  def size (self):
    return len (self.queue)
  
class Link (object):
  def __init__ (self, data, next = None):
    self.data = data
    self.next = next

class LinkedList (object):
  def __init__ (self):
    self.first = None

  def insertFirst (self, data):
    newLink = Link (data)
    newLink.next = self.first
    self.first = newLink

  def insertLast (self, data):
    newLink = Link (data)
    current = self.first

    if (current == None):
      self.first = newLink
      return

    while (current.next != None):
      current = current.next

    current.next = newLink

  def findLink (self, data):
    current = self.first
    if (current == None):
      return None

    while (current.data != data):
      if (current.next == None):
        return None
      else:
        current = current.next

    return current

  def deleteLink (self, data):
    current = self.first
    previous = self.first

    if (current == None):
      return None

    while (current.data != data):
      if (current.next == None):
        return None
      else:
        previous = current
        current = current.next

    if (current == self.first):
      self.first = self.first.next
    else:
      previous.next = current.next

    return current