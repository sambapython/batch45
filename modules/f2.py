import f1
a=1000000
def fun():
	print "this is fun in f2"
#f1.fun()
if __name__ == "__main__":
	def fun1():
		print "this is fun1 in f2"
	print "__name__:",__name__
	print "this is f2"
	fun()
	fun1()