import socket
import threading
from queue import Queue

# configuration
target = "127.0.0.1" # <-- Replace with target your target IP address
queue = Queue()
open_ports = []
threads = 100 # number of concurrent threads

def port_scan(port):
	try:
		# create socket object
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		# set timeout to prevent hanging forever
		s.settimeout(0.5)

		# connect_ex() returns 0 if connection successful, error if connection fails
		# connect_ex expects one tuple as an argument, hence the double parenthesis
		result = s.connect_ex((target, port))

		if result == 0:
			open_ports.append(port)
			return True
		else:
			return False

	except Exception as e:
		return False
	finally:
		s.close()

def worker():
	while not queue.empty():
		# get next port from queue
		port = queue.get()

		# scan port if open
		if port_scan(port):
			print(f"[*] Port {port} is OPEN")

		# tell the queue that task is complete
		queue.task_done()

def main():
	print(f"Starting scan on target: {target}")
	print("-" * 40)

	# define ports to scan
	ports_to_scan = range(1, 1023)

	for port in ports_to_scan:
		queue.put(port)

	# create and start threads
	thread_list = []
	for _ in range(threads):
		t = threading.Thread(target=worker)
		thread_list.append(t)
		t.start()

	# wait for the queue to be empty
	queue.join()

	print("-" * 40)
	print(f"Scan finished. Open ports: {open_ports}")

if __name__ == "__main__":
	main()

