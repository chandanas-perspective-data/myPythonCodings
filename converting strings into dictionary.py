str='varsha=12,shruthi=25,kalyani=21'
lst=[]
for x in str.split(','):
	y=x.split('=')
	lst.append(y)
	d=dict(lst)
	d1={}
	for k,v in d.items():
		d1[k]=int(v)
		print(d1)

