import string

fi=open('actor_dict.tsv')
st=fi.read()
list1=st.split('\n')
list1.remove('')
fi.close()

dict1={}
for i in list1:
	buff=i.split('\t')
	dict1[buff[0].lower().replace(' ','')]=buff[1]

fi=open('final.tsv')
st=fi.read()
list2=st.split('\n')
list2.remove('')
fi.close()

list3=[]
for i in list2:
	buff1=i.split('\t')
	buff2=buff1[2].split(',')
	n=0
	max_i=0
	nochange=True
	for b in buff2:
		try:
			n=float(dict1[b.lower().replace(' ','')])
			nochange=False
			if n > max_i:
				max_i=n
		except:
			nochange=True
	if nochange == False:
		s=i.replace(buff1[2],str(max_i))
	else:
		s=i
	list3.append(s)

fi=open('final2.tsv','w')
for i in list3:
	fi.write(i+'\n')
fi.close()

