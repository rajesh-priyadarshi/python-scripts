# program for append elements in list 

subjects =[] # empty list defined

cont='y'

while cont == "y" or cont=='Y':

    sub=input ("enter your subjects:---")
    subjects.append(sub)
    cont=input("do you wish to continue Y/N:- ")

print(subjects)


