print "f1 in current working directory"
a=100
def fun():
	print "this is fun in f1"


def fun1():
	print "this is fun1 in f1"
if __name__ == "__main__":
	print "__name__:",__name__
	print "this is f1"
	fun()
	fun1()