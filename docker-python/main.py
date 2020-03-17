def soma (x, y):
	yield x + y


print(next(soma(3, 4)))