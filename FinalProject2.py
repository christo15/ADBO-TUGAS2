import sys
from random import randint

class Dice(object):
  
	def roll(self):
		return randint(0,5) + 1

class User:
  curIdx = 1
  def __init__(self,name,computer):
      self.name=name
      self.computer=computer
      if computer==True:
          self.name="comp"
          curIdx=1
          self.set=True
    
  def getSet(self):
      return self.set
    
  def getName(self):
    return self.name
    
  def setCurIdx(self,curIdx):
    self.curIdx=curIdx
    
  def getCurIdx(self):
    return self.curIdx
    
  def isComputer(self):
    return self.computer

class UlarTangga(object):
	def __init__(self, toIndex):
		self._toIndex = toIndex

	def getToIndex(self):
		return self._toIndex



class Tile():
    index=0
    user = []
    ulartangga = None
    def __init__(self, index):
        self.index = index
  
    def seterUser(self, User):
        if len(self.user)<2:
            self.user.append(User)
  
    def getulartangga(self):
        return self.ulartangga
  
    def setulartangga(self, ulartangga):
        self.ulartangga = ulartangga
  
    def getuser1(self):
        return self.user[0]
  
    def getuser2(self):
        return self.user[1]
    
    def getindex(self):
        print (self.index)
        
    def removeuser(self,nama):
        if self.user[0]:
            if self.user[0].getName()==nama:
                self.user.remove(self.user[0])
        elif self.user[1]:
               print("hskdhflaskdfasdflhsdfhalsdhf")
               if self.user[1].getName()==nama:
                   self.user[1].remove(self.user[1])
