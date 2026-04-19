import socket
import threading
from queue import Queue

target = "127.0.0.1" # Replace with target IP
queue = Queue()
open_ports = []
threads = 100

def port_scan(port):
	try:
		# create socket object
		socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		# set timeout to prevent hanging forever
		socket.settimeout(1)

		# connect_ex() returns 0 if connection successful, error if connection fails
		# connect_ex expects one tuple as an argument, hence the double parenthesis
		result = socket.connect_ex((target, port))

		if result == 0:
			return True
		else:
			return False

	except Exception as e:
		return False
	finally:
		socket.close()

def worker():
	while not queue.empty():
		# get next port from queue
		port = queue.get()
	
		# scan port if open
		if port_scan(port):
			print(f"[*] Port {port} is OPEN")

		# tell the queue that task is complete
		queue.task_done()

def fill_queue(port_list):
	for port in port_list:
		queue.put(port)


