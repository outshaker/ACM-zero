# https://zerojudge.tw/ShowProblem?problemid=a165

def box():
	b={}
	b['table']=set()
	for i in range(1,10):
		b['table'].add(i)
	b['n']=0
	return b

def addn(b,i):
	if i in b['table']:
		b['table'].remove(i)
		if b['n']==0:
			b['n'] += i
		else:
			b['n'] = b['n'] *10 + i
	else:
		print(i,' not in table')

def copybox(b):
	t = {}
	t['table'] = b['table'].copy()
	t['n'] = b['n']
	return t

t1=[1,3,7,9]
t2=[2,4,6,8]
t3=[5]
choose=[t1,t2,t1,t2,t3,t2,t1,t2,t1]

boxes=[[] for i in range(10)]
for lv in range(9):
	print('choose n-th nuber: ', lv+1)
	if lv == 0:
		for x in choose[lv]:
			b=box()
			addn(b,x)
			print('add %d to empty box' % x)
			boxes[lv].append(b) #add box to boxes
		print('make %d branch' % len(boxes[lv]))
	else:
		for box in boxes[lv-1]: # choose a box
			for i in choose[lv]: # make a branch
				if i in box['table'] and (box['n'] * 10 + i) % (lv + 1) == 0:
					b=copybox(box)
					addn(b,i)
					print('add %d to box: %d' % (i,box['n']))
					boxes[lv].append(b)
				else:
					pass
		print('make %d branch' % len(boxes[lv]))

for b in boxes[8]:
	print(b['n'])

