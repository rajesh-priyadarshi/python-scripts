import os
class cal:
    def add(self,num1,num2):
        self.add=num1+num2
        return None
    def sub(self,num1,num2):
        self.sub=num1-num2
    
    def display_add(self):
        print(self.add)
        return None

    def display_sub(self):
        print(self.sub)
        return None

def main():
  val1=cal()
  val2=cal()

  val1.add(5,3)
  val2.add(8,2)

  val1.display_add()
  val2.display_add()

  val1.sub(5,3)
  val2.sub(8,2)

  val1.display_sub()
  val2.display_sub()



if __name__=='__main__':
  main()
