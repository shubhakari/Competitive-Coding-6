import string
class Node:
    def __init__(self,timestamp:int,message:string):
        self.timestamp = timestamp
        self.message = message
        self.prev = None
        self.next = None
class Logger:
    def __init__(self):
        self.maxtime = 10
        self.hmap = {}
        self.head,self.tail = Node(0,""),Node(0,"")
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def shouldPrintMessage(self,timestamp:int,mssg : string):
        if mssg in self.hmap.keys():
            tempnode = self.hmap[mssg]
            if timestamp - tempnode.timestamp < self.maxtime:
                print("False")
                return False
            self.moveToHead(tempnode,timestamp)
        else:
            if len(self.hmap) > self.maxtime:
                self.removeTail()
            self.addToHead(timestamp,mssg)
        print("True")
        return True
    
    def addToHead(self,timestamp:int,mssg : string):
        newNode = Node(timestamp,mssg)
        newNode.next = self.head.next
        self.head.next = newNode
        newNode.prev = self.head
        newNode.next.prev = newNode
        self.hmap[mssg] = newNode
    
    def removeTail(self):
        self.tail.prev.next = self.tail.next
        self.tail.next.prev = self.tail.prev
        self.hmap.pop(self.tail.message)
    
    def moveToHead(self,temp:Node,timestamp:int):
        temp.timestamp = timestamp
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        temp.next = self.head.next
        temp.prev = self.head
        self.head.next = temp
        temp.next.prev = temp


logger = Logger()
logger.shouldPrintMessage(1, "foo"); 
logger.shouldPrintMessage(2,"bar"); 
logger.shouldPrintMessage(3,"foo"); 
logger.shouldPrintMessage(8,"bar"); 
logger.shouldPrintMessage(10,"foo"); 
logger.shouldPrintMessage(11,"foo"); 
