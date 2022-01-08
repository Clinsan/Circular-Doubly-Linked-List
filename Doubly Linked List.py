
class student:
    def __init__(self,pnr,student_name,email,age,gender,grade):
        self.pnr=pnr
        self.student=student_name
        self.email=email
        self.age=age
        self.gender=gender
        self.grade=grade
    def printinfo(self):
        print(self.pnr,self.student,self.email,self.student,self.email,self.age,self.gender,self.grade)
res1=student(1,'rahul','xxxx@gmail.com',19,'male','A')
res2=student(2,'Domnic','xxxxx@gmail.com',18,'male','B')
res3=student(3,'Abk','xxxx@gmail.com',29,'male','A')
res4=student(4,'harsh','xxxxx@gmail.com',19,'male','B')
res5=student(5,'Sonam','xxxxxx@gmail.com',22,'male','C')
res6=student(6,'Parth','xxxxxxx@gmail.com',26,'male','F')
res7=student(7,'Trigger','xxxxxxx@gmail.com',33,'male','B')
res8=student(8,'Ricin','xxxxxx@gmail.com',43,'male','D')
res9=student(9,'mahale','xxxxxxx@gmail.com',25,'male','E')
res10=student(10,'Tejas','xxxxxxx@gmail.com',18,'male','B')
lis=[res1,res2,res3,res4,res5,res6,res7,res8,res9,res10]

#CREATION OF DOUBLY LINKED LIST
class Element():
   def __init__(self,key,pred,succ):
       self.key = key
       self.pred = pred
       self.succ = succ
class myList():
   def __init__(self,head,tail):
        self.head = head
        self.tail = tail

   def insert(self, value):
       element = Element(value, None, None)
       if self.head == None:
            self.head = element
            self.head.succ=self.head.pred=element
            self.tail=self.head
       elif self.head==self.tail :
           self.head.pred=element
           element.succ=self.head
           self.head.succ = element
           element.pred = self.head
           self.tail=element
           #the below lines will show that LL is circular;it will print the predecessor and successor of the  the first anbd last element
        #    print("*****************************")
        #    print("predecessor of first element:")
        #    self.head.pred.key.printinfo()
        #    print("successor of last element:")
        #    self.tail.succ.key.printinfo()
        #    print("*****************************")

       else:
           self.head.pred=element
           element.succ=self.head
           element.pred=self.tail
           self.tail.succ=element
           self.tail=element
        #the below lines will show that LL is circular;it will print the predecessor and successor of the  the first anbd last element
        #    print("*****************************")
        #    print("predecessor of first element:")
        #    self.head.pred.key.printinfo()
        #    print("successor of last element:")
        #    self.tail.succ.key.printinfo()
        #    print("*****************************")
   def printElements(self):
       x = self.head
       if (x==None):
           print("LIST EMPTY")
       else:
           print("LINKED LIST:")
           while (x.succ!=self.head):
               (x.key.printinfo(), ",")
               x = x.succ
           x.key.printinfo()
   def search(self, searchValue):
        var = self.head
        if (var==None):
            print("LIST EMPTY")
        else:
            while var != None and var.key != searchValue:
                var = var.succ
            return var
   def delete(self, x):
        a=theList.search(x)
        if a==self.head:
            self.tail.succ=self.head.succ
            self.head.succ.pred=self.tail
            self.head=self.head.succ
        elif a==self.tail:
            self.tail.pred.succ = self.head
            self.head.pred = self.tail.pred
            self.tail = self.tail.pred
        else:
            a.pred.succ=a.succ
            a.succ.pred=a.pred

theList = myList(None,None)
i=0
while True:
    print("Select your option \n1-insert\n"
                  "2-delete\n"
                  "3-search\n"
                  "4-iterate\n"
                  "5-exit\n")
    ans=int(input())
    if ans==1:
        for j in range(0,len(lis)):
            theList.insert(lis[i])
            i=i+1
        theList.printElements()
    elif ans==2:
        ab=int(input("Enter Prn"))
        if ab>=11:
            print("invalid Prn")
        else:

            theList.delete(lis[ab-1])
            theList.printElements()
    elif ans==3:
        ab = int(input("Enter Prn"))
        if ab>=11:
            print("invalid Prn")
        else:
            a=theList.search(lis[ab-1])
            a.key.printinfo()
    elif ans==4:
        theList.printElements()
    elif ans==5:
        break
    else:
        print("enter a valid input")