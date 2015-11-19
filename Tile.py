class Tile:
  
  def __init__(self,index):
    user = user_array[2]
    self.index = index
    ulartangga = ulartangga()
  
  def setUser(self,user):
    if self.user[0]==null:
      self.user[0] = user
    else if self.user[0] != null:
      self.user[1] = user
  
  def getUlarTangga(self):
    return self.ulartangga
  
  def setUlarTangga(self,ulartangga):
    self.ulartangga=ulartangga
  
  def getUser1(self):
    return self.user[0]
  
  def getUser2(self):
    return self.user[1]
  
  
