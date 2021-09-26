import os
print('%20s %20s %20s %20s' %('item_name','rate','qty','total'))

class item:
    def get_total(self,item_name,rate,qty):
        self.item_name=item_name
        self.rate=rate
        self.qty=qty
        self.total= rate*qty
    
    def display(self):
        print('%20s %20d %20d %20d' %(self.item_name, self.rate, self.qty, self.total))
        return None

def main():
        item1=item()
        item2=item()
       
        item1.get_total('apple',100,5)
        item2.get_total('banana',60,4)

        
        item1.display()
        item2.display()

if __name__=='__main__':
 main()

