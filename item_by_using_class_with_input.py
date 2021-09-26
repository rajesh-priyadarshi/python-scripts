import os

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
       
        print("")
        i_name=input("enter item name:--")
        i_rate=input("enter item rate:--")
        i_qty=input("enter item quantity:--")

        print('%20s %20s %20s %20s' %('item_name','rate','qty','total'))
        item1.get_total(i_name,int(i_rate),int(i_qty))

        
        item1.display()

if __name__=='__main__':
 main()

