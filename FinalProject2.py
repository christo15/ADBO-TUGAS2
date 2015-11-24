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
class Board():
    dice = Dice()
    tile = []
    player = []
    for i in range(0,101):
        tile.append(Tile(i))
        
    def __init__(self,pilihan):
        for x in range(0,5):
            ##Snake
            idx = randint(2, 97)
            idxTo = randint(1, (idx-2))
            if  self.tile[idx].getulartangga() == None:
                self.tile[idx].setulartangga(UlarTangga(idxTo))
      
            ##Ladder
            idx2 = randint(2, 97)
            idxTo2 = randint(0, (98-idx2)) + idx2
            if  self.tile[idx2].getulartangga() == None:
                self.tile[idx2].setulartangga(UlarTangga(idxTo2))
            
        if (pilihan == "1"):
            #print(pilihan)
            self.player.append(User("P1", False))
            self.player.append(User("P2", False))
        elif  pilihan=="2":
            self.player.append(User("P1", False))
            self.player.append(User("Bot", True))
        self.player[0].setIdx(1)
        self.player[1].setIdx(1)
        self.playerTurn = self.player[0]

      
    def run(self,x):
        if  x == "1":
          temp = self.playerTurn.getIdx() + self.dice.roll()
          if  temp <= 100:
            temp = self.checkAndChange(temp)
            print(temp)
            self.playerTurn.setIdx(temp)
          else:
            temp = temp - 100;
            temp = 100 - temp;
            temp = self.checkAndChange(temp);
            self.playerTurn.setIdx(temp);
        else:
          sys.exit(0)
          
        self.changeTurn()
  
    def checkAndChange(self, temp):
        if  self.tile[temp].getulartangga() != None:
            return self.tile[temp].getulartangga().getToIndex()
        return temp
  
    def changeTurn(self):
        if self.playerTurn == self.player[0]:
          self.playerTurn = self.player[1]
        elif  self.playerTurn == self.player[1]:
          self.playerTurn = self.player[0]
  
    def printMap(self):
        for x in range(1,101):
          if  x < 10:
            print ("%d  " % x,end='')
          elif  x >= 10:
            print ("%d " % x,end='')
          elif  x == 100:
            print (x,end='')
      
          if  x != self.player[0].getIdx() and x!= self.player[1].getIdx():
            print ("%s "%"    -  ",end='')
          else:
            if(x == self.player[0].getIdx() and x == self.player[1].getIdx()):
                print ("%s " % self.player[0].getName()+"",end='')
                print ("%s " %" ",end='')
                print ("%s " % self.player[1].getName()+"",end='')
            else:
                if  x == self.player[0].getIdx():
                    print ("%s " % "  "+self.player[0].getName()+"   ",end='')
                if  x == self.player[1].getIdx():
                    print ("%s " %"  "+self.player[1].getName()+"   ",end='')
      
          if  self.tile[x].getulartangga() != None:
            if  x < 10:
              print ("%d  "  % self.tile[x].getulartangga().getToIndex(),end='')
            elif  x > 9:
              print ("%d " % self.tile[x].getulartangga().getToIndex(),end='')
          elif  self.tile[x].getulartangga() == None:
            print ("   ",end='')
      
          if  x % 5 == 0:
            print ("")

    def getPlayer(self):
        return self.player
    
    def getPlayerTurn(self):
        return self.playerTurn

    def isWin(self):
        if self.player[0].getIdx() == 100 or self.player[1].getIdx() == 100:
          if self.player[0].getIdx() == 100:
            print (self.player[0].getName() + " is The Winner")
          else:
            print (self.player[1].getName() + " is The Winner")
          print( "=================================CONGRATULATION!!!==================================")
          return True
        return False
