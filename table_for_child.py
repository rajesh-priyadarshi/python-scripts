print ("Progroam for table")
def table(number):
    for each in range(1,11):
        tot= each*number
        print(f'{number} * {each} = {tot}' )

num=input("enter a number")
num1= table(int(num))


