days={'January':31,'February':28,'March':31,'April':30,'May':31,'June':30,'July':31,'August':31,'September':30,'October':31,'November':30,'December':31}
month=input('Enter a month: ')
print(month,'has',days[month],'days')
l=list(days)
l.sort()
print(l)
print([x[0] for x in days.items() if x[1]==31])
print([c for c in days if days[c]==31])
l=list(days.items())
l=[(i[1],i[0])for i in l]
l.sort()
print(l)
s=input('Enter month: ')
for c in days:
	if c[0:2]==s:
		print(days[c])
for c in days:
	print(c[1:2])