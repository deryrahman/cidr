#!/usr/bin/env python

import socket

def recv_until(conn, str):
	buf = ''
	while not str in buf:
		buf += conn.recv(1)
	return buf

def getValidSubnet(host):
	return host+'/32'

def countHosts(subnet):
	net_bits = subnet.split('/')[-1]
	return 2**(32-int(net_bits))

def isSubnetValid(subnet, host):
	net_bits = int(subnet.split('/')[-1])
	host_bits = ''.join(["{0:08b}".format(int(x)) for x in host.split('.')])
	subnet_bits = ''.join(["{0:08b}".format(int(x)) for x in subnet.split('/')[0].split('.')])
	if(host_bits[:net_bits]!=subnet_bits[:net_bits]): return 'F'
	return 'T'
	
TCP_IP = 'hmif.cf'
TCP_PORT = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

data = recv_until(s, 'NIM: ')
nim = raw_input(data)
s.send(nim + '\n')

data = recv_until(s, 'Verify NIM: ')
nim = raw_input(data)
s.send(nim + '\n')

print recv_until(s, '\n')[:-1]

# Phase 1
print "=== Phase 1 ==="
for i in range(100):
	recv_until(s, 'Host: ')
	host = recv_until(s, '\n')[:-1]
	recv_until(s, 'Subnet: ')
	valid_host = getValidSubnet(host)
	s.send(valid_host + '\n')
	print i
	print "Host: "+host
	print "Subnet: "+valid_host
print
print recv_until(s, '\n')[:-1]
print

# Phase 2
print "=== Phase 2 ==="
for i in range(100):
	recv_until(s, 'Subnet: ')
	subnet = recv_until(s, '\n')[:-1]
	recv_until(s, 'Number of Hosts: ')
	count_host = countHosts(subnet)
	s.send(str(count_host) + '\n')
	print i
	print "Subnet: "+subnet
	print "Number of Hosts: "+str(count_host)
print
print recv_until(s, '\n')[:-1]
print

# Phase 3
print "=== Phase 3 ==="
for i in range(100):
	recv_until(s, 'Subnet: ')
	subnet = recv_until(s, '\n')[:-1]
	recv_until(s, 'Host: ')
	host = recv_until(s, '\n')[:-1]
	result = isSubnetValid(subnet, host)
	s.send(result + '\n')
	print i
	print "Subnet: "+subnet
	print "Host: "+host
	print result
print
print recv_until(s, '\n')[:-1]
print

s.close()
