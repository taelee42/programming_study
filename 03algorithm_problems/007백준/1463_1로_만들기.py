data = int(input())
d = [0] * (data + 1)

for i in range(2, data + 1):
	d[i] = d[i - 1] + 1
	if i % 3 == 0:
		d[i] = min(d[i // 3] + 1, d[i])
	if i % 2 == 0:
		d[i] = min(d[i // 2] + 1, d[i])
	

print(d[data])
	
