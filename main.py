# -*- coding: utf_8 -*-


from pygame.locals import *
from random import randrange
import os
import pygame
import sys
import time
import pickle
# Import pygameMenu
import pygameMenu
from pygameMenu.locals import *


ABOUT = ['Car Simulator {0}'.format(pygameMenu.__version__),
		 'Author: {0}'.format(pygameMenu.__author__),
		 TEXT_NEWLINE,
		 'Email: {0}'.format(pygameMenu.__email__)]
COLOR_BACKGROUND = (124, 109, 124)
COLOR_BLACK = (255, 255, 255)
COLOR_WHITE = (0,0,0)
FPS = 60.0
MENU_BACKGROUND_COLOR = (255, 255, 255)
WINDOW_SIZE = (640, 480)

# -----------------------------------------------------------------------------
# Init pygame
pygame.init()



os.environ['SDL_VIDEO_CENTERED'] = '1'

# Create pygame screen and objects
surface = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Car Simulator')
clock = pygame.time.Clock()
dt = 1 / FPS
params = {
	"SOUND":    "0",
	"DIFFICULTY":   "1",
	"CAR":  "PINK_CAR"       
}
fichier = open("assets/config/jeu.conf", "r")
#mon_pickler = pickle.Pickler(fichier)
#mon_pickler.dump(params)
settings_load = pickle.Unpickler(fichier)
settings = settings_load.load()
# Global variables
DIFFICULTY = [settings['DIFFICULTY']]
CAR = [settings['CAR']]
SOUND = [settings['SOUND']]
dico_car = {
	"PINK_CAR":   "Purple",
	"BLUE_CAR":     "Blue",
	"GREEN_CAR":    "Green"
}
selected_car = dico_car[settings["CAR"]]

del dico_car[settings["CAR"]]
list_car = dico_car.keys()
print(dico_car)
dico_sound = {
	"1":   "Yes",
	"0":     "No"
}
selected_sound = dico_sound[settings["SOUND"]]
del dico_sound[settings["SOUND"]]
list_sound = dico_sound.keys()
print(dico_sound)
dico_difficult = {
	"1":   "Easy",
	"2":     "Medium",
	"3":    "Hard"
}
selected_diff = dico_difficult[settings["DIFFICULTY"]]
del dico_difficult[settings["DIFFICULTY"]]
list_diff = dico_difficult.keys()
print(dico_difficult)
# -----------------------------------------------------------------------------

def change_difficulty(d):
	"""
	Change difficulty of the game.
	
	:return: 
	"""
	print ('Selected difficulty: {0}'.format(d))
	DIFFICULTY[0] = d
	params['DIFFICULTY'] = d
	fichier2 = open("assets/config/jeu.conf", "w")
	mon_pickler = pickle.Pickler(fichier2)
	mon_pickler.dump(params)
	fichier2.close()
def change_sound(d):
	"""
	Change difficulty of the game.
	
	:return: 
	"""
	print ('Selected SOUND: {0}'.format(d))
	SOUND[0] = d
	if SOUND[0] == "0":
		pygame.mixer.music.set_volume(0)
	if SOUND[0] == "1":
		pygame.mixer.music.set_volume(1)
	params['SOUND'] = d
	fichier2 = open("assets/config/jeu.conf", "w")
	mon_pickler = pickle.Pickler(fichier2)
	mon_pickler.dump(params)
	fichier2.close()
def change_car(d):
	"""
	Change car of the game.
	
	:return: 
	"""
	print ('Selected car: {0}'.format(d))
	CAR[0] = d
	params['CAR'] = d
	fichier2 = open("assets/config/jeu.conf", "w")
	mon_pickler = pickle.Pickler(fichier2)
	mon_pickler.dump(params)
	fichier2.close()


def random_color():
	"""
	Return random color.
	
	:return: Color tuple
	"""
	return randrange(0, 255), randrange(0, 255), randrange(0, 255)


def play_function(difficulty, font,car,sound):
		   
	print(difficulty[0])
	print(car[0])
	import random
	liste_difficult = (5,8,13)


	mscore = open('assets/others/mscore.txt', "r")
	meil_score = mscore.read()
	meil_score = int(meil_score)
	mscore.close()
	pygame.init()




	W, H = 640, 1024

	bkgd = pygame.image.load("assets/others/route2.png").convert()
	y = 0
	surface = pygame.display.set_mode((640, 800))
	explosion = pygame.image.load("assets/others/explosion.png").convert_alpha()
	


	#Chargement et collage du fond
	rel_x = y % bkgd.get_rect().height
	surface.blit(bkgd, (0, rel_x - bkgd.get_rect().height))
	if rel_x < H:
		surface.blit(bkgd, (0, rel_x))
	y += 2
	



	liste = ('assets/ennemies/blue.png','assets/ennemies/formula.png','assets/ennemies/pickup.png','assets/ennemies/voiture_rouge.png')
	#Chargement et collage du personnage
	
	perso = pygame.image.load("assets/perso/"+car[0]+".png").convert_alpha()
	perso_dim = perso.get_size()
	surface.blit(perso, (200,100))
	pos_voiture = [(15,604),(180,620),(325,620),(505,600)]
	pos_possible = [(200,620),(335,620),(32,604),(525,600)]
	cur_pos = 1

	caillou = pygame.image.load(random.choice(liste)).convert_alpha()
	surface.blit(perso, (200,100))
	pos_cail = (200,100)
	pos_cail2 = (200,100)
	caillou_vitesse = 3
	cheat = False
	mps = 1
	bornes = 1



	pygame.display.flip()

	#BOUCLE INFINIE
	continuer = 1   
	nb_joysticks = pygame.joystick.get_count()

	if nb_joysticks > 0:
		mon_joystick = pygame.joystick.Joystick(0)

		mon_joystick.init()

		#On compte les boutons
		nb_boutons = mon_joystick.get_numbuttons()
		hats = mon_joystick.get_numhats()

	while continuer:
	   
		pygame.time.delay(10)
		times = +pygame.time.get_ticks()
		times = times/1000
		
	  

		if cheat == True:
			
			if pos_cail[0] == 200:
				cur_pos = 1
				
				
			if pos_cail[0] == 365:
				cur_pos = 0

			if pos_cail2[0] == 200:
				cur_pos = 1
				
				
			if pos_cail2[0] == 365:
				cur_pos = 0
		
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					if cur_pos == 0:
						pass
					else:
						cur_pos -= 1
					print(cur_pos)
					
				if event.key == pygame.K_RIGHT:
					if cur_pos == 3:
						pass
					else:
						cur_pos += 1
					print(cur_pos)
				if event.key == pygame.K_UP:
					cheat = True
				if event.key == pygame.K_DOWN:
					cheat = False
			if event.type == pygame.USEREVENT:
				pygame.mixer.music.rewind()
				print('Redémarage musique')
				pygame.mixer.music.play()
				pygame.mixer.music.set_endevent(pygame.USEREVENT)


		if difficulty[0] == "1":
			pos_cail = (pos_cail[0],(pos_cail[1]+liste_difficult[0]+(times/100)))
			pos_cail2 = (pos_cail2[0],(pos_cail2[1]+liste_difficult[0]+(times/100)))
		if difficulty[0] == "2":
			pos_cail = (pos_cail[0],(pos_cail[1]+liste_difficult[1]+(times/100)))
			pos_cail2 = (pos_cail2[0],(pos_cail2[1]+liste_difficult[1]+(times/100)))
		if difficulty[0] == "3":
			pos_cail = (pos_cail[0],(pos_cail[1]+liste_difficult[2]+(times
				/100)))
			pos_cail2 = (pos_cail2[0],(pos_cail2[1]+liste_difficult[2]+(times
				/100)))
		if(pos_cail[1]>800):
			caillou = pygame.image.load(random.choice(liste)).convert_alpha()

			pos_cail = (pos_possible[random.randint(0,3)][0],-55)
			pos_cail2 = (pos_possible[random.randint(0,3)][0],-55)

		#detection de collision
	   
		if pos_cail[0]+caillou.get_size()[0] >= pos_voiture[cur_pos][0] and pos_cail[0] < pos_voiture[cur_pos][0] + perso_dim[0] and pos_cail[1]+caillou.get_size()[1] > pos_voiture[cur_pos][1]:

			print('BOUM')
			continuer = False
			explode = pos_cail
		if pos_cail2[0]+caillou.get_size()[0] >= pos_voiture[cur_pos][0] and pos_cail2[0] < pos_voiture[cur_pos][0] + perso_dim[0] and pos_cail2[1]+caillou.get_size()[1] > pos_voiture[cur_pos][1]:
			explode = pos_cail2

			
			
			continuer = False
		if time > meil_score:
			mscore = open('assets/others/mscore.txt', "w")
			mscore.write(str(times))
			mscore.close()


		rel_x = y % bkgd.get_rect().height
		surface.blit(bkgd, (0, rel_x - bkgd.get_rect().height))
		if rel_x < H:
			surface.blit(bkgd, (0, rel_x))
		y += 2
		surface.blit(perso, pos_voiture[cur_pos])
		surface.blit(caillou, pos_cail)
		surface.blit(caillou, pos_cail2)
		

		

		pygame.display.flip()
	mps = 1
	times = None
	bornes = 1
	surface.blit(explosion, pos_voiture[cur_pos])
	surface.blit(explosion, explode)
	pygame.display.flip()  
	pygame.display.flip()
	time.sleep(1)
	surface = pygame.display.set_mode((640, 480))


def main_background():
	"""
	Function used by menus, draw on background while menu is active.
	
	:return: None
	"""
	surface.fill(COLOR_BACKGROUND)


# -----------------------------------------------------------------------------
# PLAY MENU
play_menu = pygameMenu.Menu(surface,
							window_width=WINDOW_SIZE[0],
							window_height=WINDOW_SIZE[1],
							font=pygameMenu.fonts.FONT_BEBAS,
							title='Play menu',
							menu_alpha=100,
							font_size=30,
							menu_width=int(WINDOW_SIZE[0] * 0.6),
							menu_height=int(WINDOW_SIZE[1] * 0.6),
							bgfun=main_background,
							menu_color=MENU_BACKGROUND_COLOR,
							option_shadow=False,
							font_color=COLOR_WHITE,
							color_selected=COLOR_WHITE,
							onclose=PYGAME_MENU_DISABLE_CLOSE
							)

# When pressing return -> play(DIFFICULTY[0], font)
settings_menu = pygameMenu.Menu(surface,
							window_width=WINDOW_SIZE[0],
							window_height=WINDOW_SIZE[1],
							font=pygameMenu.fonts.FONT_BEBAS,
							title='Settings menu',
							menu_alpha=100,
							font_size=30,
							menu_width=int(WINDOW_SIZE[0] * 0.6),
							menu_height=int(WINDOW_SIZE[1] * 0.6),
							bgfun=main_background,
							menu_color=MENU_BACKGROUND_COLOR,
							option_shadow=False,
							font_color=COLOR_WHITE,
							color_selected=COLOR_WHITE,
							onclose=PYGAME_MENU_DISABLE_CLOSE
							)
play_menu.add_option('Play', play_function, DIFFICULTY,
					 pygame.font.Font(pygameMenu.fonts.FONT_FRANCHISE, 30), CAR, SOUND)
play_menu.add_selector('Select difficulty', [(selected_diff, settings["DIFFICULTY"]),
											 (dico_difficult[list_diff[0]], list_diff[0]),
											 (dico_difficult[list_diff[1]], list_diff[1])],
					   onreturn=None,
					   onchange=change_difficulty)
play_menu.add_option('Return to main menu', PYGAME_MENU_BACK)
settings_menu.add_selector('Music', [(selected_sound, settings['SOUND']),
									(dico_sound[list_sound[0]], list_sound[0])],
					   onreturn=None,
					   onchange=change_sound)
settings_menu.add_selector('Select car', [(selected_car, settings['CAR']),
											 (dico_car[list_car[0]], list_car[0]),
											 ( dico_car[list_car[1]],list_car[1])],
					   onreturn=None,
					   onchange=change_car)
settings_menu.add_option('Return to main menu', PYGAME_MENU_BACK)

# ABOUT MENU
about_menu = pygameMenu.TextMenu(surface,
								 window_width=WINDOW_SIZE[0],
								 window_height=WINDOW_SIZE[1],
								 font=pygameMenu.fonts.FONT_BEBAS,
								 font_title=pygameMenu.fonts.FONT_8BIT,
								 title='About',
								 # Disable menu close (ESC button)
								 onclose=PYGAME_MENU_DISABLE_CLOSE,
								 font_color=COLOR_WHITE,
								 text_fontsize=20,
								 font_size_title=30,
								 menu_color_title=COLOR_WHITE,
								 menu_color=MENU_BACKGROUND_COLOR,
								 menu_width=int(WINDOW_SIZE[0] * 0.6),
								 menu_height=int(WINDOW_SIZE[1] * 0.6),
								 option_shadow=False,
								 color_selected=COLOR_WHITE,
								 text_color=COLOR_WHITE,
								 bgfun=main_background)
for m in ABOUT:
	about_menu.add_line(m)
about_menu.add_line(TEXT_NEWLINE)
about_menu.add_option('Return to menu', PYGAME_MENU_BACK)

# MAIN MENU
main_menu = pygameMenu.Menu(surface,
							window_width=WINDOW_SIZE[0],
							window_height=WINDOW_SIZE[1],
							font=pygameMenu.fonts.FONT_BEBAS,
							title='Menu Principal',
							menu_alpha=100,
							font_size=30,
							menu_width=int(WINDOW_SIZE[0] * 0.6),
							menu_height=int(WINDOW_SIZE[1] * 0.6),
							onclose=PYGAME_MENU_DISABLE_CLOSE,  # ESC disabled
							bgfun=main_background,
							menu_color=MENU_BACKGROUND_COLOR,
							option_shadow=False,
							font_color=COLOR_WHITE,
							color_selected=COLOR_WHITE,
							)
main_menu.add_option('Play', play_menu)
main_menu.add_option('Settings', settings_menu)
main_menu.add_option('About', about_menu)
main_menu.add_option('Quit', PYGAME_MENU_EXIT)
nbr = 100
def test():
	print('fin !')
#------------
#-----------------------------------------------------------------
# Main loop
while True:

	# Tick
	clock.tick(60)
	if SOUND[0] == "0":
		pygame.mixer.music.set_volume(0)
	if SOUND[0] == "1":
		pygame.mixer.music.set_volume(1)
	pygame.mixer.music.load("assets/others/StayFastStayFree.wav")
	pygame.mixer.music.play()
	pygame.mixer.music.set_endevent(pygame.USEREVENT)
	
	# Application events
	events = pygame.event.get()
	for event in events:
		if event.type == QUIT:
			exit()

	# Main  menu
	main_menu.mainloop(events)



	# Flip surface
	pygame.display.flip()
