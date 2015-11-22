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
