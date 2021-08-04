import pickle
stu = {}
stuf = open('stu.dat','wb')
ans = 'y'
while ans == 'y':
	rno  = int (input("Rollno"))
	name = input ("Name:")
	marks= float(input("Marks:"))
	stu['rno'] =rno
	stu['name']=name
	stu['marks']=marks
	pickle.dump(stu,stuf)
	ans= input("enter y/n:")
stuf.close()
#/home/kavi/seekbin.py
