import random
import Tile
import User
import Dice

class Board :
  tile = Tile[101]
  player = User[2]
  dice = Dice()
  playerTurn = User()
  rnd = Random()
  
  def __init__(self,pilihan):
    for x in range(0,101): 
      tile[x]= Tile(x)
    if  pilihan==1:
      player[0]=User("P1", false)
      player[1]=User("P2", false)
    elif  pilhan==2:
      player[0]=User("P1", false)
      player[1]=User("Bot", true)
    
    tile[1].setUser(player[0])
    tile[1].setUser(player[1])
    
    self.playerTurn = player[0]
    
    ##Snake and ladder
    for x in range(0,5):
      ##Snake
      idx = random.randint(2, 97)
      idxTo = random.randint(0, idx-2)
      if  tile[idx].getUlarTangga == None:
        tile[idx].setUlarTangga(UlarTangga(idxTo))
      
      ##Ladder
      idx2 = random.randint(2, 97)
      idxTo2 = random.randint(0, 98-idx2) + idx2
      if  tile[idx2].getUlarTangga == None:
        tile[idx2].setUlarTangga(UlarTangga(idxTo2))
  
  
  def run(self,x):
    if  x == 1:
      temp=playerTurn.getCurIdx + dice.roll
      if  temp <= 100:
        temp=checkAndChange(temp)
        tile[playerTurn.getCurIdx].removeUser(playerTurn.getName)
        tile[temp].setUser(playerTurn)
        playerTurn.setCurIdx(temp)
      else:
        tile[playerTurn.getCurIdx()].removeUser(playerTurn.getName());
        temp = temp - 100;
        temp = 100 - temp;
        temp = self.checkAndChange(temp);
        tile[temp].setUser(playerTurn);
        playerTurn.setCurIdx(temp);
    else:
      sys.exit(0)
      
    self.changeTurn
  
  def checkAndChange(self, temp):
    if  tile[temp].getUlarTangga != None:
      return tile[temp].getUlarTangga.getToIndex
    return temp
  
  def changeTurn(self):
    if playerTurn == player[0]:
      self.playerTurn = player[1]
    elif  playerTurn == player[1]:
      self.playerTurn = player[0]
  
  def printMap(self):
    for x in range(1,100):
      if  x < 10:
        print i+"  "
      elif  x >= 10:
        print i+" "
      elif  x == 100:
        print i+""
      
      if  tile[x].getUser1 == None & tile[x].getUser2 == None:
        print "   -  "
      else:
        if  tile[x].getUser1 != None:
          print tile[x].getUser1.getName + " "
        if  tile[x].getUser2 != None:
          print tile[x].getUser2.getName + " "
      
      if  tile[x].getUlarTangga != null:
        if  x < 10:
          print tile[x].getUlarTangga.getToIndex + "   "
        elif  x > 9:
          print tile[x].getUlarTangga.getToIndex + " "
      elif  tile[x].getUlarTangga == None:
        print "   "
      
      if  x % 5 == 0:
        print "\n"
  
