class Player:
  team_run = 0
  def __init__(self,run):
    self.run = run
    
  def hit_four(self):
    self.run += 4
    Player.team_run += 4
    
  def hit_six(self):
    self.run += 6
    Player.team_run += 6
    
sakib = Player(0)
Tamim = Player(0)

sakib.hit_six()
Tamim.hit_four()
Tamim.hit_four()
Tamim.hit_four()

print('Sakib:',sakib.run)
print('Tamim:',Tamim.run)

print('Total: ',Player.team_run)

  
    
  
    