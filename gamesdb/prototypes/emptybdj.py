# encoding: utf-8

class Obj(object):
	def __init__(self):
		self.x = 123
		self.y = 456
		
	def __iter__(self):
		return iter([self.x, self.y])
		
	def __repr__(self):
		return "x = {}, y = {}".format(self.x, self.y)
	
	
def demo1():
	"""
	 Demo of simple iteration
	"""
	objects = ["Knife", "Pen", "Tablet"]
	print(iter(objects))
	
	a = iter(objects)
	print(next(a))
	print(next(a))
	print(next(a))
	print(help(a))
	
def demo2():
	"""
	Более сложный вариант, когда какой-то обьект возвращает что-то итерируемое
	"""
	o = Obj()
	# print(iter(o))
	try:
		oi = iter(o)
		while True:
			print(next(oi))
			print(next(oi))
	except StopIteration:
		print("Nothing to iterate!")
		
	print("Done!")
	
def welder():
	a = list(range(1,10))
	print(a)
	
	for i in a:
		print(i)
		yield i
		
if __name__ == "__main__":
	print(help(welder()))
	
	print("Under yield")
	#yield 
	
