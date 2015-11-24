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

