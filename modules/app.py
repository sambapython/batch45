#fun()--> get an error
'''
import f1
print "calling in app *"
f1.fun()
'''
'''
from f1 import fun
fun()
'''
'''
import f1
print fun()
'''
'''
import f1
f1.fun()
print f1.a
'''
'''
import f1
f1.fun1()
'''
'''
import f1,f2
f2.fun()
print f2.a
f1.fun()
print f1.a
'''
'''
import f2
f2.f1_file.fun()
'''
'''
import f2
import f1
f2.fun()
f2.f1.fun()
print f2.a
print f2.f1.a
print f1.a
'''
'''
from f1 import a, fun
from f2 import fun as f2_fun
print a
fun()
f2_fun()
'''
'''
from f3 import fun
fun()
'''
'''
import sqlite3
import f1
'''
'''
import sys
print sys.path
import f1
f1.fun()
'''
'''
import sys
#sys.path.append("/home/khyaathi-python")
sys.path.insert(0,"/home/khyaathi-python")
#sys.path.reverse()
print sys.path
import f1
f1.fun()
'''
#import empty
#from empty import file1
'''
import empty
empty.file1.fun()
'''
'''
import empty
empty.file1.fun()
'''
'''
from empty import file1
file1.fun()
'''
'''
import empty
import empty
import empty
'''
'''
from empty import file1
file1.fun()
'''
'''
from empty.file1 import fun
fun()
'''
from empty import file2

