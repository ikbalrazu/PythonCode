'''
num1=int(input("Enter first value: "))
num2=int(input("Enter second value: "))
powerful = max(num1,num2)
notposerful=min(num1,num2)
print(f"The sum of {num1} + {num2}={num1+num2}")
print(f"here max value is {powerful}")
print(f"here min value is {notposerful}")
'''
#relational operator > < = == != >= <=


'''
replace split join string fuction
'''
name="iqbal raju"
old="iqbal"
new="md"
funtionofreplace=name.replace(old,new)
replacefuntion=name.replace("iqbal","mohammad")
print(name)
print(funtionofreplace)
print(replacefuntion)

#join string function
message = ("what's","your","name")
joinfun=' '.join(message)
print(joinfun)

note="my name is iqbal"
notesplit=note.split()
print(notesplit)
funtionofjoin=' '.join(notesplit)
print(funtionofjoin)