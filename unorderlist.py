from structures import UnorderedList

mylist = UnorderedList()
mylist.add('zhang')
mylist.add('yi')
mylist.add('ju')

a = mylist.search('zhang')
b = mylist.size()
c = mylist.head.getData()
print(a)
print(b)
print(c)
mylist.all()