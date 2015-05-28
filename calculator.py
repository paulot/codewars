class Calculator(object):

  operations = {
    '+': (lambda a,b: a+b, 10),
    '-': (lambda a,b: a-b, 10),
    '*': (lambda a,b: a*b, 20),
    '/': (lambda a,b: a/b, 20)
  }

  def evaluate(self, string):
    self.tokens = string.split(' ')
    self.token = self.getToken()
    return self.calc()

  def getToken(self):
    elem = self.tokens.pop(0)
    try:
      return int(elem)
    except ValueError:
      return elem


  def calc(self, prec = 0):
    print self.tokens
    left = self.token
    if len(self.tokens) == 0:
      return left
    self.token = self.getToken()

    while prec < self.operations[self.token][1]:
      op = self.token
      self.token = self.getToken()
      left = self.operations[op][0](left, self.calc(self.operations[op][1]))
    return left

