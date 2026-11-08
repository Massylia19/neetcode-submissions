class MyHashMap:

    def __init__(self):
        #[2, 3, 5, 1, 2] a =[0,0] [1, 3]  a[1] = 3
        #[[1, 1], [2, 3]] [1, 1]
        #O(n^2)
        #a = {3: 8, 1: 4}  = == == = =. a[1] = 4
        #[9, 2] [7, 0] [1,2, None, None] [4, 6]
        self.liste = [None]
        self.length = len(self.liste)
        

    def put(self, key: int, value: int) -> None:
        # verify if we have the space to add a new pair
        if key >= self.length:
            diff = key - self.length + 1
            while diff:
                self.liste.append(None) 
                diff -= 1
            self.liste[key] = value
            self.length = len(self.liste)
            return
        
        self.liste[key] = value



        

    def get(self, key: int) -> int:
        
        if key < self.length and self.liste[key] != None: 
            return self.liste[key]

        return -1 

        
        
   #[None, 1, 2] 
    def remove(self, key: int) -> None:
        #print(self.liste)
        if key >= self.length:
            return

        self.liste[key] = None
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)