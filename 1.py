def pythonsum():
	a = range(10)
	b = range(10)
	c = []
	
	for i in range(len(a)):
		c.append(a[i]**2 + b[i]**3)
		
	print(c)
	
pythonsum()
