"""
Implement a clss called player that represent a cricket player .thae player class should have a method called play()which prints "the player is playing cricket".derive two classes,batsman and bowler from the player class.ovveriding the play() method in each derived class to print "the batsman is batting "anfd "the bowler is bowling",respectively. write a program to create object of both the batsman and bowler classes and call the play()method for each object
"""


#define the base class player
class Player:

  def play(self):
    print("the player is playing cricket:")


#define the derived class  batsmanclass
class Batsman(Player):

  def play(self):
    print("the batsman is batting")


#define the derived class bowler
class Bowler(Player):

  def play(self):
    print("the bowler is bowling")


#create objects of batsman and bowling
batsman = Batsman()
bowler = Bowler()
#call the play ()method for each objects
batsman.play()
bowler.play()
