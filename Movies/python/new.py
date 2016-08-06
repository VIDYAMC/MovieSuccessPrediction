import string
import json

fi=open('final.tsv')
st=fi.read()
list1=st.split('\n')
list1.remove('')
fi.close()

fi=open('omdb.json')
st=fi.read()
data=json.loads(st)
fi.close()

dict1={}
dict2={}
for i in data:
	dict1[i['imdbID']]=i['Genre']
	n=i['Runtime'].replace(' min','')
	dict2[i['imdbID']]=n

print len(dict1)
print len(dict2)

list2=[]
for i in list1:
	try:
		buff=i.split('\t')
		s=i.replace('\t'+buff[7]+'\t','\t'+dict1[buff[0]]+'\t')
		list2.append(s)
	except:
		list2.append(i)

list3=[]
for i in list2:
	try:
		buff=i.split('\t')
		s=i.replace(buff[3]+'\t'+buff[4]+'\t',buff[3]+'\t'+dict2[buff[0]]+'\t')
		list3.append(s)
	except:
		list3.append(i)

print len(list3)
fi=open('final1.tsv','w')
for i in list3:
	fi.write(i+'\n')
fi.close()
