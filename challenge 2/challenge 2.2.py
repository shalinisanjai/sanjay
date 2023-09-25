#Define the base calss palyer
class player:
    def play(self):
         print("The palyer is playing cricket.")

#Define the derived calss Batsman
class Batsman(player):
    def paly(self):
      print("The batsman is batting.")

#Define the derived calss Bowler
class Bowler(player):
    def paly(self):
      print("The bolwer is bowling.")

#Create objects of Batsman and Bowler calsses
batsman = Batsman()
bowler=Bowler()

# Call the paly()method for each object
batsman.paly()
bowler.paly()

