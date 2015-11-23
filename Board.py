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
    
    playerTurn = player[0]
    
    ##Snake and ladder
    for x in range(0,5):
      ##Snake
      idx = randrange(2, 97)
      idxTo = random
      
      
      
      
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  ## 139
    def getPlayer(self):
      return self.player
    
    def getPlayerTurn(self):
      return playerTurn
    
    def isWin(self):
      if player[0].getCurIdx == 100 ^| player[1].getCurIdx == 100:
        if player[0].getCurIdx == 100:
          print player[0].getName + " is The Winner"
        else:
          print player[1].getName + " is The Winner"
        print "=================================CONGRATULATION!!!=================================="
        return true
      return false
        
