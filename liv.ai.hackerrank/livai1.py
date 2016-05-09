import sys
import heapq
import math

Test_cases = int(sys.stdin.readline())
if Test_cases < 1 or Test_cases > math.pow(10,3):
	raise Exception("Inavlid Input Format")


for i in range(Test_cases):
	no_of_participants = int(sys.stdin.readline())
	if no_of_participants < 1 or no_of_participants > math.pow(10,6):
		raise Exception("Inavlid Input Format")

	chunks = sys.stdin.readline().split(" ")
	mass = []
	if len(chunks) != no_of_participants:
		raise Exception("Inavlid Input Format")
	for chunk in chunks:
		if int(chunk) < 1 or int(chunk) > math.pow(10,7):
			raise Exception("Inavlid Input Format")
		mass.append(int(chunk))

	chunks = sys.stdin.readline().split(" ")
	velocity = []
	if len(chunks) != no_of_participants:
		raise Exception("Inavlid Input Format")
	for chunk in chunks:
		if int(chunk) < 1 or int(chunk) > math.pow(10,7):
			raise Exception("Inavlid Input Format")
		velocity.append(int(chunk))

	my_mass = int(sys.stdin.readline())

	k = int(sys.stdin.readline())

	# process
	momentums = []
	for m in heapq.nlargest(k, mass):
		for v in heapq.nlargest(k, velocity):
			momentum = m*v
			if momentum not in momentums:
				momentums.append(momentum)

	k_largest = heapq.nlargest(k, momentums)

	my_velocity = math.ceil( float( min(k_largest)/my_mass))
	print(my_velocity)
