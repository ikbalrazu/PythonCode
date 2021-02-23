
"""
subject=["Bangla","English","Math","Social Science","Science","ICT"]
subject.append("DB")
subject.insert(2,"OS")
subject.remove("Bangla")
subject.sort()
print(subject)
print(subject[3],subject[2])
print(len(subject))

num=[10,9,12,11,20,12,12,12]
print(num)
#num.sort()
#num.reverse()
#num.pop()
#num.pop()
#num.clear()
#indexno=num.index(10)
co=num.count(12)

print(co)
"""
#dictionary

dictionaryExample={"name" : "iqbal", "id" : "162-35-1703", "department" : "Software Eng."}
#dictionaryExample["name"]="Raju"
#print(dictionaryExample['department'])
for x in dictionaryExample:
    print(dictionaryExample[x])