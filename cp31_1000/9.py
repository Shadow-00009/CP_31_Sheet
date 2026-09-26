import math

t = int(input())

for i in range(t):

	n = int(input())

	ans_a = 1
	ans_b = n - 1

	for fac in range(2, int(math.sqrt(n)) + 1):
		if n % fac == 0:
			ans_a = n // fac
			ans_b = n - ans_a
			break

	print(ans_a, ans_b)