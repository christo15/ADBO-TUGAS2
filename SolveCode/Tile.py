import UlarTangga
import User

class Tile():
    user = User[2]
    index=0
    ulartangga = UlarTangga()
  
    def __init__(self, index):
        self.index = index
  
    def setuser(self, user):
        if self.user[0] == null:
            self.user[0] = user
        elif self.user[0] != null:
            self.user[1] = user
  
    def getulartangga(self):
        return self.ulartangga
  
    def setulartangga(self, ulartangga):
        self.ulartangga = ulartangga
  
    def getuser1(self):
        return self.user[0]
  
    def getuser2(self):
        return self.user[1]
    
    def getindex(self):
        print self.index
        
    def removeuser(self,nama):
        if self.user[0]!=null:
            if self.user[0].getname()==nama:
                self.user[0]=null
        elif self.user[1]!=null:
               if self.user[1].getname()==nama:
                   self.user[1]=null
                
