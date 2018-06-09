def play_function(difficulty, font,car):
    print(difficulty[0])
    print(car[0])
    import random
    liste_difficult = (5,8,15)

    mscore = open('mscore.txt', "r")
    meil_score = mscore.read()
    meil_score = int(float(meil_score))
    mscore.close()
    pygame.init()




    W, H = 640, 1024
    bkgd = pygame.image.load("route2.png").convert()
    y = 0
    surface = pygame.display.set_mode((640, 800))


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
    pos_voiture = [(200,620),(365,620)]
    cur_pos = 1

    caillou = pygame.image.load(random.choice(liste)).convert_alpha()
    surface.blit(perso, (200,100))
    pos_cail = (200,100)
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
                
   
            


        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    cur_pos = 0
                if event.key == pygame.K_RIGHT:
                    cur_pos = 1
                if event.key == pygame.K_UP:
                    cheat = True
                if event.key == pygame.K_DOWN:
                    cheat = False
            if event.type == pygame.USEREVENT+1:
                print('BORNE')


        if difficulty[0] == "1":
            pos_cail = (pos_cail[0],(pos_cail[1]+liste_difficult[0]+(times/100)))
        if difficulty[0] == "2":
            pos_cail = (pos_cail[0],(pos_cail[1]+liste_difficult[1]+(times/100)))
        if difficulty[0] == "3":
            pos_cail = (pos_cail[0],(pos_cail[1]+liste_difficult[2]+(times
                /100)))
        if(pos_cail[1]>800):
            caillou = pygame.image.load(random.choice(liste)).convert_alpha()
            pos_cail = (pos_voiture[random.randint(0,1)][0],-55)

        #detection de collision
       
        if pos_cail[0]+caillou.get_size()[0] >= pos_voiture[cur_pos][0] and pos_cail[0] < pos_voiture[cur_pos][0] + perso_dim[0] and pos_cail[1]+caillou.get_size()[1] > pos_voiture[cur_pos][1]:
            continuer = False

        if time > meil_score:
            mscore = open('mscore.txt', "w")
            mscore.write(str(times))
            mscore.close()


        rel_x = y % bkgd.get_rect().height
        surface.blit(bkgd, (0, rel_x - bkgd.get_rect().height))
        if rel_x < H:
            surface.blit(bkgd, (0, rel_x))
        y += 2
        surface.blit(perso, pos_voiture[cur_pos])
        surface.blit(caillou, pos_cail)

        

        pygame.display.flip()
    mps = 1
    times = None
    bornes = 1
    time.sleep(1.5)
    surface = pygame.display.set_mode((640, 480))