#Hash set

s= set()
print(s)

#Add item into Set - O(1)
s.add(1)
s.add(2)
s.add(3)

print(s)

#Lookup if item in set - O(1)

if 1 in s:
    print(True)
    s.remove(3)
print(s)    




















#Interview Definition
#A hash table is a data structure that stores key-value pairs and uses a hash function to map keys to indices, providing average O(1) time for search, insertion, and deletion.


#hashable:only mutable

