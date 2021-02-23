
try:
    f=open('examplefil.txt','r')
    print(f.read())
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()