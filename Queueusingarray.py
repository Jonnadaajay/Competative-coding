class MyQueue:
    def __init__(self):
         self.Q=[]
    
    #Function to push an element x in a queue.
    def push(self, x):
         self.Q.append(x)
         
         #add code here
     
    #Function to pop an element from queue and return that element.
    def pop(self): 
         if len(self.Q)==0:
            return -1
         return self.Q.pop(0)
