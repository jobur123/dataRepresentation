colnames = ['id','name','age']
result =[1,'Mary',21]
item = {}
for i, colnames in enumerate(colnames):
	value = result[i]
	item[colnames] = value

print(item)
