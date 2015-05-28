# Given a binery tree where larger numbers are at the top, design an algorithm
# to find a number in the minimum number of traversal

import Queue

class node():
  def __init__(self, item, l=None, r=None):
    self.left = l
    self.right = r
    self.item = item

def exists(root, item):
  clevel = Queue.Queue()
  nlevel = Queue.Queue()
  clevel.put(root)
  smallest = root.item
  while not clevel.empty() or not nlevel.empty():
    cur = clevel.get()
    if cur.item == item:
      return True
    else:
      if cur.left != None:
        nlevel.put(cur.left)
      if cur.right != None:
        nlevel.put(cur.right)

    smallest = min(smallest, cur.item)

    if clevel.empty():
      clevel = nlevel
      nlevel = Queue.Queue()
      if smallest < item:
        return False

  return False

a3 = node(1)
b3 = node(2)
c3 = node(3)
d3 = node(55)


a2 = node(50, a3, b3)
b2 = node(60, c3, d3)

a1 = node(70, a2, b2)

