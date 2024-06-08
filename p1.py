class Node :
    def __init__ (self,d = None,l = None) :
        self.data = d
        self.link = l

class linklist :
    def __init__ (self):
        self.first = Node()
        self.first.link = self.first

    def deleteprime (self) :
        q = self.first
        p = q.link
        while p != self.first :
            flag=True
            for i in range(2,p.data//2):
                if p.data%i==0:
                    flag=False
                    break
            if flag :
                q.link = p.link
            else :
                q = p
            p = p.link
        
    def printList (self) :
        p = self.first.link
        while p != self.first :
            print(p.data)
            p = p.link
            
    def mergeSort (self,l1 , l2) :
        last = self.first 
        p = l1.first.link
        q = l2.first.link
        while p!=l1.first and q != l2.first:
            if p.data < q.data :
                last.link = p
                last = p
                p = p.link
            else :
                last.link = q
                last = q
                q = q.link
        else :
            if p != l1.first :
                last.link=p
                while(p.link!=l1.first) :
                    p=p.link
                last=p
            else :
                last.link=q
                while(q.link!=l2.first):
                    q=q.link
                last=q
            last.link=self.first
    def insert(self,x):
        p=Node(x,self.first.link)     
        self.first.link=p
        
        
# l1=linklist()
# l2=linklist()
# l3=linklist()
# for i in range(8,1,-1) :
#     l1.insert(i)
#     l2.insert(i*2)
# l3.mergeSort(l1,l2)
# l3.printList()

       
class Stack(linklist) :
    def __init__ (self):
        self.top = Node()

    def push(self,x) :
        q = Node(x,self.top.link)
        self.top.link = q

    def pop(self) :
        if not self.top.link:
            return None
        x = self.top.link.data
        self.top.link = self.top.link.link
        return x

class Queue (linklist) :
    def __init__ (self) :
        self.front = Node()
        self.rear = self.front
    
    def addItem (self,x) :
        q = Node(x)
        self.rear.link = q
        self.rear = q
        
    def deleteItem (self) :
        if not self.front.link :
            return None
        x=self.front.link.data
        self.front.link=self.front.link.link
        if self.front.link==0 :
            self.rear=self.front
        return x
# s1=Stack()
# for i in range(1,9):
#     s1.push(i)
# for i in range(1,9) :
#     print (s1.pop())
# q1=Queue()
# for i in range(2,8):
#     q1.addItem(i)
# for i in range(2,8):
#     print (q1.deleteItem())