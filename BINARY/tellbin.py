import pickle
stu = {}
found = False
fin = open ('stu.dat','rb')
try:

	while True:
		rpos = fin.tell()
		stu = pickle.load(fin)
		if stu['rno']==2:
			stu['Name']='Vincy'
			fin.seek(rpos)
			pickle.dump(stu,fin)
			found = True
except EOFError:
	if found == False:
		print("Sorry not found")
	else:
		print("Record updated")
		fin.close()
