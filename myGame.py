from sys import exit
from random import randint

class Scene(object):
	def enter(self):
		self.scene = CentralCorridor()
		print self.scene
		exit(1)

class Engine(object):
	def __init__(self, scene_map):
		print "Engine __init__ has scene_map", scene_map
		self.scene_map = scene_map

	def play(self):
		current_scene = self.scene_map.opening_scene()
		print "Play's first scene", current_scene

		while True:
			print "\n---------"
			next_scene_name = current_scene.enter()
			print "next scene", next_scene_name
			current_scene = self.scene_map.next_scene(next_scene_name)
			# print "map returns new scene", current_scene

class Death(Scene):
	eulogies = [
		"You died. You kinda suck at this.",
		"You falied in your task and evil overtakes your world.",
		"Gandalf cried when he learned of your demise.",
		"You probably got eaten by Shelob, it is truly tragic."
	]

	def enter(self):
		print Death.eulogies[randint(0, len(self.eulogies)-1)]
		print """            Three::rings
          for:::the::Elven-Kings
       under:the:sky,:Seven:for:the
     Dwarf-Lords::in::their::halls:of
    stone,:Nine             for:Mortal
   :::Men:::     ________     doomed::to
 die.:One   _,-'...:... `-.    for:::the
 ::Dark::  ,- .:::::::::::. `.   Lord::on
his:dark ,'  .:::::zzz:::::.  `.  :throne:
In:::the/    ::::dMMMMMb::::    \ Land::of
:Mordor:\    ::::dMMmgJP::::    / :where::
::the::: '.  '::::YMMMP::::'  ,'  Shadows:
 lie.::One  `. ``:::::::::'' ,'    Ring::to
 ::rule::    `-._```:'''_,-'     ::them::
 all,::One      `-----'        ring::to
   ::find:::                  them,:One
    Ring:::::to            bring::them
      all::and::in:the:darkness:bind
        them:In:the:Land:of:Mordor
           where:::the::Shadows
           """
		exit(1)

class TheShire(Scene):
	def enter(self):
		print """                  . .:.:.:.:. .:\     /:. .:.:.:.:. ,
               .-._  `..:.:. . .:.:`- -':.:. . .:.:.,'  _.-.
              .:.:.`-._`-._..-''_...---..._``-.._.-'_.-'.:.:.
           .:.:. . .:_.`' _..-''._________,``-.._ `.._:. . .:.:.
        .:.:. . . ,-'_.-''      ||_-(O)-_||      ``-._`-. . . .:.:.
       .:. . . .,'_.'           '---------'           `._`.. . . .:.
     :.:. . . ,','               _________               `.`. . . .:.:
    `.:.:. .,','            _.-''_________``-._            `._.     _.'
  -._  `._./ /            ,'_.-'' ,       ``-._`.          ,' '`:..'  _.-
 .:.:`-.._' /           ,','                   `.`.       /'  '  \\.-':.:.
 :.:. . ./ /          ,','               ,       `.`.    / '  '  '\\. .:.: 
:.:. . ./ /          / /    ,                      \ \  :  '  '  ' \\. .:.:
.:. . ./ /          / /            ,          ,     \ \ :  '  '  ' '::. .:.
:. . .: :    o     / /                               \ ;'  '  '  ' ':: . .:
.:. . | |   /_\   : :     ,                      ,    : '  '  '  ' ' :: .:.
:. . .| |  ((<))  | |,          ,       ,             |\'__',-._.' ' ||. .:
.:.:. | |   `-'   | |---....____                      | ,---\/--/  ' ||:.:.
------| |         : :    ,.     ```--..._   ,         |''  '  '  ' ' ||----
_...--. |  ,       \ \             ,.    `-._     ,  /: '  '  '  ' ' ;;..._
:.:. .| | -O-       \ \    ,.                `._    / /:'  '  '  ' ':: .:.:
.:. . | |_(`__       \ \                        `. / / :'  '  '  ' ';;. .:.
:. . .<' (_)  `>      `.`.          ,.    ,.     ,','   \  '  '  ' ;;. . .:
.:. . |):-.--'(         `.`-._  ,.           _,-','      \ '  '  '//| . .:.
:. . .;)()(__)(___________`-._`-.._______..-'_.-'_________\'  '  //_:. . .:
.:.:,' \/\/--\/--------------------------------------------`._',;'`. `.:.:.
:.,' ,' ,'  ,'  /   /   /   ,-------------------.   \   \   \  `. `.`. `..:
,' ,'  '   /   /   /   /   //                   \\   \   \   \   \  ` `.SSt
"""
		print "Good evening Frodo Baggins of The Shire, My name is Gandalf and I intend to help you with your quest."
		print "By now we know that the ring of power yearns for it's master."
		print "The council of Elrond has chosen you to bear the burden,"
		print "and I will try my very best to guide you along this treacherous path. "
		print "Everything in my power little Frodo."
		print "\n"
		print "Every step you take you must be chosen very wisely for it could very well be your last."
		print "We will head east for the misty mountains and from there"
		print "fdescending into the lands of men, who we should hope will aid us."
		print "And you alone will face the danger of Mt. Doom. For you are brave beyond your knowldge."
		print "We leave now young master."
		print "Your first challenge is to decide whether we head through the (M)ines of Moria, the path through (W)eathertop or the (L)ong road."

		action = raw_input("> ")

		if action == "M":
			print "The mines are treacherous and who knows what evil lurks."
			print "But if that is your choice, then we shall go you Frodo."
			print "Be careful and quiet or we will wake an awful beast!"
			print "FRODO!! Run!! They've heard us!!"
			print "You try and flee but encounter a great beast of a troll."
			print "You fight valiantly but are no match and are slain."
			return 'death' 

		elif action == "W":
			print "These paths are filled with bandits, be on the watch."
			print "We have made it safley, you must sleep and I must meet a friend."
			print "In the middle of the night you awake with a start."
			print "The ring wraiths are upon you Frodo!"
			print "You are stabbed brutally in the shoulder!"
			print "As you drift away you see a brave man come to your rescue, "
			print "but it is no use, you slip beyond the realms of men."
			return 'death'

		elif action == "L":
			print "Excellent idea, we will head for the secret passageway."
			print "Your journey is swift and safe,"
			print "your step is soft and light."
			print "The ring weighs heavy but you press on, recognizing your place"
			print "in the world of men. You can change the future."
			print "You come across the stairs."
			return 'shelobs_lair'

		elif action == "Fly":
			print "I am truly surprised at your wisdom young Frodo. Well played."
			return 'cheater'

		else:
			print "DO NOT MISTAKE ME FOR SOME CONJUROR OF CHEAP TRICKS!"
			return 'the_shire'

class ShelobsLair(Scene):

	def enter(self):
		print "There is something strange about the air in the cave."
		print "There are thick spider webs everywhere"
		print "and you continue through cautiously."
		print "There is a strange, strange sound echoing in the walls."
		print "You are frightened young Frodo, and you"
		print "happen upon a giant, evil spider!"
		print "You run for your life, but you must make precise cuts"
		print "through the webs in front of you! A combo of 2 numbers!"
		code = "%d%d" % (randint(1,9), randint(1,9))
		guess = raw_input("[sword combos]> ")
		guesses = 0

		if guess == 'cheat':
			print 'Well, I will turn a blind eye to that. You are a sneaky buglar little Frodo.'
			return 'the_plains_of_doom'

		while guess != code and guesses < 10:
			print "THE WEBS ARE TIGHTENING!"
			guesses += 1
			guess = raw_input("[sword combos]> ")

		if guess == code:
			print "You break free of the vast labrynth of Shelobs webs!"
			print "You flee as fast as you can,"
			print "you can feel that the completion of your journey"
			print "is upon you. Press on you Frodo!"
			return 'the_plains_of_doom'

		else:
			print "The webs are becoming thicker and thicker"
			print "you feel the sticky webs closing in on you."
			print "Your movement is becoming restricted,"
			print "Shelob is upon you poor Frodo."
			return 'death'



class ThePlainsOfDoom(Scene):

	def enter(self):
		print "You burst through the caves, run Frodo!"
		print "This is not the end of the journey, not yet,"
		print "be strong Frodo, you are so very close!"
		print "You see that a battle is raging before you"
		print "and Mt. Doom is erupting before your eyes."
		print "Do you (f)ight or (r)un for the heart of Mt. Doom."

		action = raw_input("> ")

		if action == "f":
			print "In a panic you help your comrades in battle upon"
			print "the plains of Mt. Doom."
			print "You fight valiantly, Frodo"
			print "But Sauron feels you and will not let "
			print "you live on this day, on htis battle field."
			print "You are overcome and your death is swift."
			return 'death'

		elif action == "r":
			print "You focus on the entrance to the heart of "
			print "Mt Doom. This is your time to change Middle Earth."
			print "You inch towards the edge of the cliff"
			print "and gather your strenght."
			print "You then jump back as if an outer force is taking you"
			print "away from the firey pits of Mt. Doom."
			print "You fight the urge to surrender and with a defiant grin"
			print "cast the Ring of Power into the pits of Mt. Doom"
			return 'mt_doom'
		else:
			print "CHOOSE WISELY FRODO!"
			return "the_plains_of_doom"


class MtDoom(Scene):

	def enter(self):
		print "Shock overcomes your body. You are not sure what has happened."
		print "You flee from Mt. Doom"
		print "the walls are crumbling before you."
		print "You are tired and have little desire to continue on."
		print "But something inside urges you to keep moving."
		print "The end is near Frodo, and you have been brave."
		print "Your mind is playing tricks on you, can you"
		print "discern which way is out and which way is in?"

		get_out = randint(1,5)
		guess = raw_input("[you can move 1-5]> ")


		if int(guess) != get_out:
			print "Your mind sees %s and your body cannot comprehend." % guess
			print "The journey has taken it's toll on you Frodo."
			print "You are a hero to all."
			print "Farwell old friend."
			return 'death'
		else:
			print "Your mind sees %s and your feel strength." % guess
			print "The number tells your body to keep moving"
			print "and you escape the pits of Mt. Doom."
			print "You hardly belive your eyes when your rescuer arrives. A"
			print "beautiful giant Eagle, takes you up into"
			print "the heavens.  You did it Frodo!"

			return 'finished'


class Cheater(object):
	def enter(self):
		print """ 
         ___ . .  _                                                                                             
"T$$$P"   |  |_| |_                                                                                             
 :$$$     |  | | |_                                                                                             
 :$$$                                                      "T$$$$$$$b.                                          
 :$$$     .g$$$$$p.   T$$$$b.    T$$$$$bp.                   BUG    "Tb      T$b      T$P   .g$P^^T$$  ,gP^^T$$ 
  $$$    d^"     "^b   $$  "Tb    $$    "Tb    .s^s. :sssp   $$$     :$; T$$P $^b.     $   dP"     `T :$P    `T
  :$$   dP         Tb  $$   :$;   $$      Tb  d'   `b $      $$$     :$;  $$  $ `Tp    $  d$           Tbp.   
  :$$  :$;         :$; $$   :$;   $$      :$; T.   .P $^^    $$$    .dP   $$  $   ^b.  $ :$;            "T$$p.  
  $$$  :$;         :$; $$...dP    $$      :$;  `^s^' .$.     $$$...dP"    $$  $    `Tp $ :$;     "T$$      "T$b 
  $$$   Tb.       ,dP  $$" Tb    $$      dP ""$""$" "$"$^^  $$$""T$b     $$  $      ^b$  T$       T$ ;      $$
  $$$    Tp._   _,gP   $$   `Tb.  $$    ,dP    $  $..$ $..  $$$   T$b    :$  $       `$   Tb.     :$ T.    ,dP 
  $$$;    "^$$$$$^"   d$$     `T.d$$$$$P^"     $  $"-$ $"", $$$    T$b  d$$bd$b      d$b   "^TbsssP" 'T$bgd$P ' 
  $$$b.____.dP                                 $ .$. .$.$ss,d$$$b.   T$b.                                       
.d$$$$$$$$$$P                                                        `T$b.                                     
                                                                        "^^"      
"""

class Map(object):
	scenes = {
		'the_shire': TheShire(),
		'shelobs_lair': ShelobsLair(),
		'the_plains_of_doom': ThePlainsOfDoom(),
		'mt_doom': MtDoom(),
		'death': Death(),
		'cheater': Cheater()
	}

	def __init__(self, start_scene):
		self.start_scene = start_scene
		# print "start_scene in __init__", self.start_scene

	def next_scene(self, scene_name):
		# print "start_scene in next_scene"
		val = Map.scenes.get(scene_name)
		# print "next_scene returns", val
		return val

	def opening_scene(self):
		return self.next_scene(self.start_scene)

a_map = Map('the_shire')
a_game = Engine(a_map)
a_game.play()












