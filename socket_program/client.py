import logging
logging.basicConfig(level=logging.WARN, 
	filename="log.txt",
	format="%(asctime)s==>%(levelname)s==>%(message)s",
	)
import socket
s=socket.socket()
hostname="khyaathipython"
port=8890
try:
	s.connect((hostname,port))
	ack=s.recv(1024)
	print ack
	number=raw_input("Enter number:")
	s.send(number)
	res = s.recv(10)
	print "result=",res
except Exception as err:
	print err
finally:
	s.close()
