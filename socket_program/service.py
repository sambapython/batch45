"""
take hostname and port number
wait for client request
if the client sends a request then need to aceept that.
need to process that. 
need to send a response back to the client
"""
import logging
logging.basicConfig(level=logging.WARN, 
	filename="log.txt",
	format="%(asctime)s==>%(levelname)s==>%(message)s",
	)
import socket
s=socket.socket()
logging.info("created socket instance")
hostname=socket.gethostname()
logging.debug("host name of the service:%s"%hostname)
port=8890
logging.debug("port of the service:%s"%port)
try:
	s.bind((hostname, port))
	logging.info("bindgin completed")
	while True:
		try:
			s.listen(6)
			logging.info("waiting for the clinet request")
			service_msg = "server running in %s:%s"%(hostname, port)
			print service_msg
			logging.debug(service_msg)
			client_obj, clinet_info= s.accept()
			logging.debug("request came from: %s"%clinet_info[0])
			ack= "Hello fire fox ... How are you doing?"
			logging.info("sending ack:%s"%ack)
			client_obj.send(ack)
			req_data=client_obj.recv(12)
			logging.debug("Client data: %s"%req_data)
			resp = "EVEN" if int(req_data)%2==0 else "ODD"
			logging.debug("Sending the result: %s"%resp)
			client_obj.send(resp)
		except Exception as err:
			client_obj.send(err.message)
			logging.error(err.message)
except Exception as err:
	print err
	logging.error(err.message)
finally:
	s.close()
	logging.info("closing the socket")
