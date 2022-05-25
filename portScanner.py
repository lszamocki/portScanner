#!/usr/bin/python3

import socket
import sys

HOST = '127.0.0.1'
if len(sys.argv) == 2:
	HOST = sys.argv[1]
else:
	print("Invalid amount of arguments")
	print("Syntax: python3 scanner.py <ip>")
	
print('\n')
print('-' * 50)
print("Scanning host {}".format(HOST))
print('-' * 50)


try:

	for port in range(1, 65535):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((HOST, port))
		if result == 0:
			print('Port {} is open'.format(port))
		s.close()
except KeyboardInterrupt:
	print("\nProgram stopping")
	sys.exit()
except socket.gaierror:
	print("Host could not be resolved")
	sys.exit()
except socket.error:
	print("Couldn't connect to server")
	sys.exit() 
