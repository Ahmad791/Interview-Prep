class node:
    def __init__(self, data):
        self.data = data
        self.height = 1
        self.leftSon = None
        self.rightSon = None

#                      delete not done yet
class Tree:
    def __init__(self):
        self.root = None
        
    def rotateLeft(self, current):
        rlson=current.rightSon.leftSon
        rson=current.rightSon
        current.rightSon=rlson
        rson.leftSon=current
        return rson
    
    def rotateRight(self, current):
        lrson=current.leftSon.rightSon
        lson=current.leftSon
        current.leftSon=lrson
        lson.rightSon=current
        return lson
    
    def updateHeight(self,current):
        ld=current.leftSon.height if current.leftSon!=None else 0
        rd=current.rightSon.height if current.rightSon!=None else 0
        current.height=max(ld,rd)+1
    
    def balance(self,current):
        ld=current.leftSon.height if current.leftSon!=None else 0
        rd=current.rightSon.height if current.rightSon!=None else 0
        if rd-ld>1:
            current=self.rotateLeft(current)
        if ld-rd>1:
            current=self.rotateRight(current)
        if current.leftSon!=None:
            self.updateHeight(current.leftSon) 
        if current.rightSon!=None:
            self.updateHeight(current.rightSon)
        self.updateHeight(current)
        return current

    def recInsert(self,current,x):#recursive insert
        if(x.data>current.data):
            if current.rightSon is None:
                current.rightSon=x
            else:
                self.recInsert(current.rightSon,x)
        else:
            if current.leftSon is None:
                current.leftSon=x
            else:
                self.recInsert(current.leftSon,x)
        
        return self.balance(current)
        
                     
    def insert(self,value):
        x=node(value)
        if self.root is None:
            self.root=x
        else:
            self.root=self.recInsert(self.root, x)
    
    def recSearch(self,current,value):
        if value==current.data:
            return current
        if value>current.data:
            return self.recSearch(current.rightSon,value) if current.rightSon is not None else -1
        else:
            return self.recSearch(current.leftSon,value) if current.leftSon is not None else -1
    
    def search(self,value):
        return self.recSearch(self.root,value)
    
    def recDelete(self,current,value):# on hold for now
        if value==current.data:
            return current
        if value>current.data:
            return self.recDelete(current.rightSon,value) if current.rightSon is not None else -1
        else:
            return self.recDelete(current.leftSon,value) if current.leftSon is not None else -1
    
    def delete(self,value):
        print("input doesn't exist\n") if self.recDelete(self.root,value)==-1 else print(value," Successfully deleted")


if __name__ == '__main__':
    t=Tree()
    t.insert(1)
    t.insert(3)
    t.insert(4)
    t.insert(5)
    print(t.search(1))
    #still delete to work on