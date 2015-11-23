import sys

class main:
  
  print("==========ular tangga==========="+"\n")
  print("1. Player vs Player"+"\n")
  print("2. Computer vs Player"+"\n")
  pilihan = raw_input("masukan pilihan: ")
  board= Board(pilihan)
  board.printMap()
  while(!board.isWin()):
    if !board.getPlayerTurn().isComputer():
      turn = board.getPlayerTurn()
      print("=========== " + turn.getName() + " Turns Now============"+"\n")
      print("1. ROLL?"+"\n")
      print("2. EXIT?"+"\n")
      board.Run(raw_input("1 ATAU 0"))
    else:
      print("=========== COMPUTER'S Turns Now============"+"\n")
      board.Run(1)
    board.printMap()
