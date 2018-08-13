from timeit import timeit

git = int


def gt():
	for i in range(4):
		git('7')


def lt():
	lint = int
	for i in range(4):
		lint('7')


def it():
	for i in range(4):
		int('7')


if __name__ == '__main__':
	print(timeit('gt()', 'from __main__ import gt', number=100000)/100000, 'global import')
	print(timeit('lt()', 'from __main__ import lt', number=100000)/100000, 'local import')
	print(timeit('it()', 'from __main__ import it', number=100000)/100000, 'direct call')
