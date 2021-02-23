"""
f=open('examplefile.txt','r')
print(f.name)
print(f.mode)
"""
with open('examplefile.txt','r') as f:
    for line in f:
        print(line)
 # f_contents=f.readline()
  #print(f_contents)
#print(f.read())
f.close()

# f=open('examplefile2.txt','a')
# f.write('hi all frinds i am not good for everything \n')
# print("write in file succesfully")
