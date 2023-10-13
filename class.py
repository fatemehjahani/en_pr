class userik :
  def __init__(self,username,password):
    self.username = username
    self.password = password
  def printname(self):
    print(self.username,self.password)  



class buyer(userik):
  def __init__(self,username,password,adres,codemeli):
    userik.__init__(self,username,password)
    self.adres = adres
    self.codemeli = codemeli


p1 = buyer("fatemeh", "123456","tohid","0372174957")
print(p1.username)
print(p1.password)
print(p1.adres)
print(p1.codemeli)