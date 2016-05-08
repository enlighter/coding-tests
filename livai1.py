import sys
import heapq
import math

Test_cases = int(sys.stdin.readline())

for i in range(Test_cases):
	no_of_participants = int(sys.stdin.readline())

	chunks = sys.stdin.readline().split(" ")
	mass = []
	if len(chunks) != no_of_participants:
		raise Exception("Inavlid Input Format")
	for chunk in chunks:
		mass.append(int(chunk))

	chunks = sys.stdin.readline().split(" ")
	velocity = []
	if len(chunks) != no_of_participants:
		raise Exception("Inavlid Input Format")
	for chunk in chunks:
		velocity.append(int(chunk))

	my_mass = int(sys.stdin.readline())

	k = int(sys.stdin.readline())

	# process
	momentums = []
	for m in heapq.nlargest(k, mass) mass:
		for v in velocity:
			momentum = m*v
			if momentum not in momentums:
				momentums.append(momentum)

	k_largest = heapq.nlargest(k, momentums)

	my_velocity = math.ceil( float( min(k_largest)/my_mass))


print(my_velocity)
