
class Conversion:
	def __init__(self):
		self.top = -1
		self.array = []
		self.output = []
		self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
	def isEmpty(self):
		return True if self.top == -1 else False

	def peek(self):
		return self.array[-1]
	def pop(self):
		if not self.isEmpty():
			self.top -= 1
			return self.array.pop()
		else:
			return "$"
	def push(self, op):
		self.top += 1
		self.array.append(op)

	def isOperand(self, ch):
		return ch.isalpha()

	def notGreater(self, i):
		try:
			a = self.precedence[i]
			b = self.precedence[self.peek()]
			return True if a <= b else False
		except KeyError:
			return False

	def infixToPostfix(self, exp):
		for i in exp:
			
			if self.isOperand(i):
				self.output.append(i)

			elif i == '(':
				self.push(i)

			elif i == ')':
				while((not self.isEmpty()) and
					self.peek() != '('):
					a = self.pop()
					self.output.append(a)
				if (not self.isEmpty() and self.peek() != '('):
					return -1
				else:
					self.pop()

			else:
				while(not self.isEmpty() and self.notGreater(i)):
					self.output.append(self.pop())
				self.push(i)

		while not self.isEmpty():
			self.output.append(self.pop())
		return ("".join(self.output))
	def postToin(self,expression):
		for i in expression:
			if self.isOperand(i):
				self.array.append(i)
			else:
				a=self.array.pop()
				b=self.array.pop()
				self.array.append("("+b+i+a+")")
		return self.array[0]
	def intopre(self,exp):
		x=list(reversed(exp))
		y="".join(x)
		z=self.infixToPostfix(y)
		b=list(reversed(z))
		c="".join(b)
		return c
	def pretoin(self,exp):
		a=list(reversed(exp))
		for i in a:
			if self.isOperand(i):
				self.array.append(i)
			else:
				self.array.append("("+self.array.pop()+i+self.array.pop()+")")
		return self.array[0]
		

if __name__ == '__main__':
	exp = "a+b*(c^d-e)^(f+g*h)-i"
	obj = Conversion()
	e="abcd^e-fgh*+^*+i-" 
	print(obj.postToin(e))
	print(obj.infixToPostfix(exp))
	print(obj.intopre(exp))
	x=obj.intopre(exp)
	print(obj.pretoin(x))