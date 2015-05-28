# Given a binery tree print every edge that is outward facing

import Queue

class node():
  def __init__(self, item, l=None, r=None):
    self.left = l
    self.right = r
    self.item = item

def printEdge(root):
  clevel = Queue.Queue()
  nlevel = Queue.Queue()
  clevel.put((root, True))
  printNext = True
  while not clevel.empty() or not nlevel.empty():
    cur = clevel.get()
    if cur[1]:
      print cur.item

    if cur.left != None:
      nlevel.put((cur.left, nlevel.empty() or printNext)
    if cur.right != None:
      nlevel.put((cur.right, clevel.empty() == 1)

    if clevel.qsize() == 1:
      last = True

    if clevel.empty():
      clevel = nlevel
      nlevel = Queue.Queue()
      first = True



a4 = node(99)
b4 = node(99)

a3 = node(1)
c3 = node(3, a4,b4)
d3 = node(55)


b2 = node(60, c3, d3)
b3 = node(2,b2)
a2 = node(50, a3, b3)

a1 = node(70, a2)

