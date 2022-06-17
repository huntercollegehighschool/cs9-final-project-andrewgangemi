"""
Andrew Gangemi
CS3 Final Project - Choose Your Own Adventure
'Stranded'
"""

start = input("Welcome to 'Stranded', a game about trying to escape a deserted island. Would you like to play? Enter 'y' to begin: ")
while start not in ['y', 'Y']:
      print("Ok, goodbye. You can always change your mind! \n")
      start = input("Welcome to Stranded, a game about trying to escape a deserted island. Would you like to play? Enter 'y' to begin: ")
if start == 'y' or start == 'Y':
  print("\nLet's get started. \n")
def fire():
  print ("\n You hastily start a fire using survival skills from a time long ago. You cannot quite remember how it is you were able to do it, but it comes like second nature.")
  print ("\n To your relief, the helicopter pilot spots the smoke and begins to lower. A ladder is thrown out of the back and you eagerly climb up it.")
  print ("\nAfter thanking your saviors you look out the window and watch the spot you were in just moments before become fully submerged by the tsunami.")
  print ("\n You are mortified, but you are alive.")
  print ("\n~ YOU WIN ~")
def sos():
  print ("\nYou try to spell out SOS in sticks and rocks on the ground, but it is no use. You cannot do so fast enough.")
  print ("\nYou have only completed half of an S when you hear the helicopter's sound become quieter and quieter.")
  print ("\nThe rushing water grows closer. There is nothing left for you to do.")
  print ("\n~ GAME OVER ~")
def shake():
  print("\nYou shake the tree and watch a coconut fall out of the tree. It lands right in your hands and you crack it against a nearby rock, digging into the meat.You feel well nourished, and almost at peace when you see a wall of water in the distance.")
  print ("\nThere is a tsunami headed your way! You look around, failing to find any form of higher ground you could seek salvation in. You begin to panic when you hear helicopter blades whirring above you.")
  print ("\nYou desperately look for a way to signal the helicopter. You notice a pile of sticks and rocks on the ground. Do you want to try to spell out SOS in the sand or try to make a fire?")
  choice7 = input("\n Enter S to spell out SOS  or F to make a fire: ")
  while choice7 not in ['S', 's', 'F', 'f']:
    print("\nPlease enter a valid input.\n")
    choice7 == input("\n Enter S to open the scroll  or F to make a fire: ")
  if choice7 == 'S' or choice7 == 's':
    sos()
  elif choice7 == 'F' or choice7 == 'f':
    fire()
def falsefire():
  print ("\nYou try to gather the sticks and rocks but because of your ankle's condition it is no use. You are mortified to watch the helicopter fly right over you, not noticing your pathetic attempt of a signal.")
  print ("\nCrumpled on the ground, you turn around and watch the wall of water rushing towards you in defeat. There is nothing left for you to do.")
  print ("\n~ GAME OVER ~")
def scroll():
  print ("\nYou open the scroll and see that it was actually holding a small flare gun. A wave of relief rushes over you as you crawl to an open space on the island and fire a round into the sky.")
  print("\nThe helicopter sees your shot and begins to lower. A person helps you into the helicopter, and the pilot rises once again.")
  print("\nYou look out the window and watch the spot you were in just moments before become fully submerged by the tsunami. You are mortified, but you are alive.")
  print("\n~ YOU WIN ~")
def climb():
  print ("\n You begin to scale the trunk of the coconut tree, now mutliple stories in the air. Your muscles feel fatigued but the sight of the scroll becoming closer and closer keeps you motivated.")
  print("\nFinally, the scroll is within your reach and you grab for it. As you pull the scroll from its fastened position the branch you are sitting on snaps off, and you hurdle to the ground scroll in hand.") 
  print ("\nYou hit the sandy floor and are immediately disoriented. You are so stunned you almost don't realize your broken ankle.")
  print ("\nYou are in agony, and decide to crawl to the seashore and find something to aid you, but what you are met with is something horrific. A massive tidal wave is rushing towards you. How could you not have noticed it?") 
  print ("\nAs you begin to hobble back for cover you hear the loud whirring of helicopter blades hundreds of feet above you. You also notice a pile of sticks and rocks on the ground, that you think you could use to make a fire to signal the helicopter.")
  print("Do you want to open the scroll or make the fire?")
  choice6 = input("\n Enter S to open the scroll  or F to make a fire: ")
  while choice6 not in ['S', 's', 'F', 'f']:
    print("\nPlease enter a valid input.\n")
    choice6 == input("\n Enter S to open the scroll or F to make a fire: ")
  if choice6 == 'S' or choice6 == 's':
    scroll()
  elif choice6 == 'F' or choice6 == 'f':
    falsefire()
def light():
  print ("\n You hold the sparkling scales to the sky and watch a ginormous beam of purple light fire into the air. Are these scales magical??")
  print ("\nThe beam blinds the pilot and you watch in horror as your only chance of survival violently swirves, nosedives, and crashes into the ocean. A pile of metal and scraps float in the water.")
  print ("\nThe scales start to hum and make a shattering sound, breaking into tiny fragments. You stumble backwards, looking up at the wall of water now upon you. The scales have led you to a salty demise.")
  print("\n~ GAME OVER ~")
def pocketscales():
  print ("\n You put the scales in your pocket. You feel like these will become useful. You decide to walk to the seashore and scout your surroundings, but what you are met with is something horrific. A massive tidal wave is rushing towards you. How could you not have noticed it? As you begin to scramble for cover you hear the loud whirring of helicopter blades hundreds of feet above you." )
  print ("\n You begin to panic, thinking of ways to get its attention. You take the scales out of your pocket looking at their mystical shine. You wonder if you hold them up the sunlight will bounce off of them and signal the pilot. Although signaling the pilot this may disrupt their view and make it very difficult for them to see you.")
  print ("\n Right before you try you also notice rocks scattered on the sandy floor. You realize it may be a smarter choice to try to signal to the pilot by spelling out SOS on the ground. You need to act fast. Which method will you try? ")
  choice5 = input("\n Enter S to send the SOS signal or L to use the scales: ")
  while choice5 not in ['S', 's', 'L', 'l']:
    print("Please enter a valid input.\n")
    choice5 == input("\n Enter S to send the SOS signal or L to use the scales: ")
  if choice5 == 'S' or choice5 == 's':
    sos()
  elif choice5 == 'L' or choice5 == 'l':
    light()
def leavescales():
  print ("\n You leave the scales behind and walk away. How could they be useful anyways?")
  print ("\n You decide to walk to the seashore and scout your surroundings, but what you are met with is something horrific. A massive tidal wave is rushing towards you. How could you not have noticed it? As you begin to scramble for cover you hear the loud whirring of helicopter blades hundreds of feet above you.") 
  print ("\n You begin to panic, thinking of ways to get its attention. You notice a pile of driftwood and stray stones scattered around you. Would you like to spell out 'SOS' using the rocks or send a smoke signal to the helicopter by attempting to make a fire ?")
  choice4 = input("\n Enter F to start the fire or S to spell SOS: ")
  while choice4 not in ['S', 's', 'F', 'f']:
    print("Please enter a valid input.\n")
    choice4 == input("\n Enter F to start the fire or S to spell SOS: ")
  if choice4 == 'S' or choice4 == 's':
    sos()
  elif choice4 == 'F' or choice4 == 'f':
    fire()
def fish():
  print ("\n You walk towards the fish and as you get closer you see its shiny gleaming scales. You notice a sharp rock right next to you. You pick it up and throw it at the fish.")
  print ("\n Good job! You killed it! You crouch down and pick up the fish, admiring it's glimmering coat. After eating the insides you are only left with the scales. Would you like to save these for later usage? They might be useful... ")
  choice2 = input("\n Enter P to pocket the scales, or L to leave them behind: ")
  while choice2 not in ['P', 'p', 'L', 'l']:
    print("Please enter a valid input.\n")
    choice2 == input("\n Enter P to pocket the scales, or L to leave them behind: ")
  if choice2 == 'L' or choice2 == 'l':
    leavescales()
  elif choice2 == 'P' or choice2 == 'p':
    pocketscales()
def coconut():
  print ("\n You walk to the tree and notice its large stature. You also notice a strange scroll tightly fastened to the top of the tree. You will probably only get the scroll if you climb it. Would you like to take your chance and climb the tree or shake it?")
  choice3 = input("\n Enter C to climb or S to shake: ")
  while choice3 not in ['C', 'c', 'S', 's']:
    print("Please enter a valid input.\n")
    choice3 == input("\n Enter C to climb or S to shake: ")
  if choice3 == 'C' or choice3 == 'c':
    climb()
  elif choice3 == 'S' or choice3 == 's':
    shake()
def intro():
  print ("\nYou wake up. You feel sun beating down on your body and you can hardly see because of how bright it is. You are stranded on a deserted island.")
  print ("\nYou notice that you are famished. You see a large coconut tree in the distance, as well as a fish splashing around in the oasis next to you.")
  print ("\nWould you like to go to the coconut tree or the fish?")
  choice = input ("\n Enter F for fish or C for coconuts: ")
  while choice not in ['F', 'f', 'C', 'c']:
    print("Please enter a valid input.\n")
    choice == input("\n Enter F for fish or C for coconuts: ")
  if choice == 'F' or choice == 'f':
    fish()
  elif choice == 'C' or choice == 'c':
    coconut()
intro()