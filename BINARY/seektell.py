import pickle
stu = {}
f =open("stu.dat","rb") 
try:
	while True:
		stu = pickle.load(f)
		print(stu)
except EOFError:
	f.close()
