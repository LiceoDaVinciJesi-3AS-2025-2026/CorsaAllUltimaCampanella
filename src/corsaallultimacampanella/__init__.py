def main() -> None:
    print("Hello from corsaallultimacampanella!")
    
    import pygame
    import random
    import math

    pygame.init()

    SCREEN_WIDTH = 1600
    SCREEN_HEIGHT = 925

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("corsa all'ultima campanella!")

    #bottoni vari
    buttonInfo = pygame.Rect(SCREEN_WIDTH // 2.45, SCREEN_HEIGHT // 1.235, 310, 80)
    buttonStart = pygame.Rect(SCREEN_WIDTH // 2.4, SCREEN_HEIGHT // 1.48, 280, 80)
    buttonGinnastica = pygame.Rect(SCREEN_WIDTH // 14.4, SCREEN_HEIGHT // 2.25, 230, 60)
    buttonStoFilo = pygame.Rect(SCREEN_WIDTH // 3.37, SCREEN_HEIGHT // 2.25, 230, 60)
    buttonArte = pygame.Rect(SCREEN_WIDTH // 1.89, SCREEN_HEIGHT // 2.25, 230, 60)
    buttonInglese = pygame.Rect(SCREEN_WIDTH // 1.32, SCREEN_HEIGHT // 2.25, 230, 60)
    buttonMatematica = pygame.Rect(SCREEN_WIDTH // 14.4, SCREEN_HEIGHT // 1.14, 230, 60)
    buttonFisica = pygame.Rect(SCREEN_WIDTH // 3.37, SCREEN_HEIGHT // 1.13, 230, 60)
    buttonScienze = pygame.Rect(SCREEN_WIDTH // 1.89, SCREEN_HEIGHT // 1.14, 230, 60)
    buttonInformatica = pygame.Rect(SCREEN_WIDTH // 1.32, SCREEN_HEIGHT // 1.14, 230, 60)

    #sfondo nella home
    imgSfondoPrincipale = pygame.image.load("pixelscuola.png") 
    imgSfondoPrincipale = pygame.transform.scale(imgSfondoPrincipale,(SCREEN_WIDTH,SCREEN_HEIGHT))

    #sfondo nella schermata dei personaggi
    imgSfondoPersonaggi = pygame.image.load("sfondopersonaggi.png")
    imgSfondoPersonaggi = pygame.transform.scale(imgSfondoPersonaggi,(SCREEN_WIDTH,SCREEN_HEIGHT))

    #immagini dei prof
    imgGinnastica = pygame.image.load("pixelginnastica.png") 
    imgGinnastica = pygame.transform.scale(imgGinnastica,(320,310))
    imgStofilo = pygame.image.load("pixelstofilo.png") 
    imgStofilo = pygame.transform.scale(imgStofilo,(170,270))
    imgArte = pygame.image.load("pixelarte.png") 
    imgArte = pygame.transform.scale(imgArte,(150,275))
    imgInglese = pygame.image.load("pixeling.png") 
    imgInglese = pygame.transform.scale(imgInglese,(145,280))
    imgMatematica = pygame.image.load("pixelmate.png") 
    imgMatematica = pygame.transform.scale(imgMatematica,(170,250))
    imgFisica = pygame.image.load("pixelfisica.png") 
    imgFisica = pygame.transform.scale(imgFisica,(150,280))
    imgScienze = pygame.image.load("pixelscienze.png") 
    imgScienze = pygame.transform.scale(imgScienze,(130,285))
    imgInformatica = pygame.image.load("pixelinfo.png") 
    imgInformatica = pygame.transform.scale(imgInformatica,(170,270))

    #sfondo dei livelli
    imgLivello = pygame.image.load("sfondoLivello.png") 
    imgLivello = pygame.transform.scale(imgLivello, (SCREEN_WIDTH, SCREEN_HEIGHT))
    imgHaiPerso = pygame.image.load("sfondoHaiPerso.png")
    imgHaiPerso = pygame.transform.scale(imgHaiPerso, (SCREEN_WIDTH, SCREEN_HEIGHT))
    imgHaiVinto1 = pygame.image.load("sfondoHaiVinto100.png")
    imgHaiVinto1 = pygame.transform.scale(imgHaiVinto1, (SCREEN_WIDTH, SCREEN_HEIGHT))
    imgHaiVinto2 = pygame.image.load("sfondoHaiVinto150.png")
    imgHaiVinto2 = pygame.transform.scale(imgHaiVinto2, (SCREEN_WIDTH, SCREEN_HEIGHT))
    imgHaiVinto3 = pygame.image.load("sfondoHaiVinto200.png")
    imgHaiVinto3 = pygame.transform.scale(imgHaiVinto3, (SCREEN_WIDTH, SCREEN_HEIGHT))
    imgHaiVinto4 = pygame.image.load("sfondoHaiVinto250.png")
    imgHaiVinto4 = pygame.transform.scale(imgHaiVinto4, (SCREEN_WIDTH, SCREEN_HEIGHT))
    imgHaiVinto5 = pygame.image.load("sfondoHaiVinto300.png")
    imgHaiVinto5 = pygame.transform.scale(imgHaiVinto5, (SCREEN_WIDTH, SCREEN_HEIGHT))
    imgHaiVinto6 = pygame.image.load("sfondoHaiVinto350.png")
    imgHaiVinto6 = pygame.transform.scale(imgHaiVinto6, (SCREEN_WIDTH, SCREEN_HEIGHT))
    imgHaiVinto7 = pygame.image.load("sfondoHaiVinto400.png")
    imgHaiVinto7 = pygame.transform.scale(imgHaiVinto7, (SCREEN_WIDTH, SCREEN_HEIGHT))
    imgHaiVinto8 = pygame.image.load("sfondoHaiVinto450.png")
    imgHaiVinto8 = pygame.transform.scale(imgHaiVinto8, (SCREEN_WIDTH, SCREEN_HEIGHT))
    imgInformazioni = pygame.image.load("sfondoInformazioni.png") 
    imgInformazioni = pygame.transform.scale(imgInformazioni, (SCREEN_WIDTH, SCREEN_HEIGHT))

    #font delle parole nei bottoni e parole 
    Normalfont = pygame.font.SysFont('Impact', 60)
    parolaButtonInfo = Normalfont.render("informazioni", True, "black")
    parolaButtonStart = Normalfont.render("start", True, "black")

    # Dati dei giocatori
    vel_y = 0 #velocità iniziale
    gravita = 0.8
    salto = -25
    al_suolo = True
    is_crouching = False
    altezza_normale = 350
    altezza_crouch = 330
    ground_y = 800  # altezza del pavimento nel livello
    larghezza_player = 400
    
    # Player Rect
    player_rect = pygame.Rect(100, 0, larghezza_player, altezza_normale)
    player_rect.bottom = ground_y

    #immagini giocatori
    imgPers1 = pygame.image.load("pixelginnastica.png").convert_alpha()
    imgPers1 = pygame.transform.scale(imgPers1, (larghezza_player, altezza_normale))
    imgPers1Jump = pygame.image.load("ginnasticasalto.png").convert_alpha()
    imgPers1Jump = pygame.transform.scale(imgPers1Jump, (larghezza_player, altezza_normale))

    imgPers2 = pygame.image.load("pixelstofilo.png").convert_alpha()
    imgPers2 = pygame.transform.scale(imgPers2, (larghezza_player - 180, altezza_normale - 10))
    imgPers2Crouch = pygame.image.load("stofilosdraiato.png").convert_alpha()
    imgPers2Crouch = pygame.transform.scale(imgPers2Crouch, (larghezza_player, altezza_crouch - 175))

    imgPers3 = pygame.image.load("pixelarte.png").convert_alpha()
    imgPers3 = pygame.transform.scale(imgPers3, (larghezza_player - 200, altezza_normale - 20))
    imgPers3Crouch = pygame.image.load("artesdraiato.png").convert_alpha()
    imgPers3Crouch = pygame.transform.scale(imgPers3Crouch, (larghezza_player + 40, altezza_crouch - 175))
    imgPers3Jump = pygame.image.load("artesalto.png").convert_alpha()
    imgPers3Jump = pygame.transform.scale(imgPers3Jump, (larghezza_player - 120, altezza_normale - 90))

    imgPers4 = pygame.image.load("pixeling.png").convert_alpha()
    imgPers4 = pygame.transform.scale(imgPers4, (larghezza_player - 250, altezza_normale - 25))
    imgPers4Jump = pygame.image.load("inglesesalto.png").convert_alpha()
    imgPers4Jump = pygame.transform.scale(imgPers4Jump, (larghezza_player - 30, altezza_normale - 90))

    imgPers5 = pygame.image.load("pixelmate.png").convert_alpha()
    imgPers5 = pygame.transform.scale(imgPers5, (larghezza_player - 200, altezza_normale - 10))
    imgPers5Crouch = pygame.image.load("matesdraiato.png").convert_alpha()
    imgPers5Crouch = pygame.transform.scale(imgPers5Crouch, (larghezza_player - 5, altezza_crouch + 75))

    imgPers6 = pygame.image.load("pixelfisica.png").convert_alpha()
    imgPers6 = pygame.transform.scale(imgPers6, (larghezza_player - 200, altezza_normale + 20))
    imgPers6Crouch = pygame.image.load("fisicasdraiato.png").convert_alpha()
    imgPers6Crouch = pygame.transform.scale(imgPers6Crouch, (larghezza_player - 30, altezza_crouch - 75))
    imgPers6Jump = pygame.image.load("fisicasalto.png").convert_alpha()
    imgPers6Jump = pygame.transform.scale(imgPers6Jump, (larghezza_player - 50, altezza_normale - 100))

    imgPers7 = pygame.image.load("pixelscienze.png").convert_alpha()
    imgPers7 = pygame.transform.scale(imgPers7, (larghezza_player - 230, altezza_normale))
    imgPers7Crouch = pygame.image.load("scienzesdraiato.png").convert_alpha()
    imgPers7Crouch = pygame.transform.scale(imgPers7Crouch, (larghezza_player + 16, altezza_crouch - 35))
    imgPers7Jump = pygame.image.load("scienzesalto.png").convert_alpha()
    imgPers7Jump = pygame.transform.scale(imgPers7Jump, (larghezza_player - 30, altezza_normale - 90))

    imgPers8 = pygame.image.load("pixelinfo.png").convert_alpha()
    imgPers8 = pygame.transform.scale(imgPers8, (larghezza_player - 200, altezza_normale - 10))
    imgPers8Crouch = pygame.image.load("informaticasdraiato.png").convert_alpha()
    imgPers8Crouch = pygame.transform.scale(imgPers8Crouch, (larghezza_player + 15, altezza_crouch - 55))
    imgPers8Jump = pygame.image.load("infosalto.png").convert_alpha()
    imgPers8Jump = pygame.transform.scale(imgPers8Jump, (larghezza_player - 30, altezza_normale - 70))

    # --- NEMICO SEDIA ---
    sedia_width = 160
    sedia_height = 190
    sedia_rect = pygame.Rect(1200, 0, sedia_width, sedia_height)
    sedia_rect.bottom = ground_y
    sedia_rect.left = 1200
    sedia_speed = 15
    imgSedia = pygame.image.load("sedia.png").convert_alpha()
    imgSedia = pygame.transform.scale(imgSedia, (sedia_width, sedia_height))

    # --- NEMICO BANCO ---
    banco_width = 380
    banco_height = 200
    banco_rect = pygame.Rect(1200, 0, banco_width, banco_height)
    banco_rect.bottom = ground_y + 15 # leggermente più alto del terreno
    banco_rect.left = 1200 + 1000 
    banco_speed = 15
    banco_active = False
    banco_start_time = pygame.time.get_ticks()
    imgBanco = pygame.image.load("banco.png").convert_alpha()
    imgBanco = pygame.transform.scale(imgBanco, (banco_width, banco_height))

    # --- Punteggio ---
    punteggio = 0
    font_punti = pygame.font.SysFont('Impact', 50)
    sedia_passata = False
    banco_passato = False
    campanella_attiva = False
    campanella_rect = pygame.Rect(1200, ground_y - 200, 120, 120)
    imgCampanella = pygame.image.load("campanella.png").convert_alpha()
    imgCampanella = pygame.transform.scale(imgCampanella,(200,200))

    # oscillazione nemici
    oscillazione_sedia = 0
    direzione_sedia = 1
    oscillazione_banco = 0
    direzione_banco = 1
    offset = 0
    vel_oscillazione = 0.05
    ampiezza = 40

    clock = pygame.time.Clock()

    running = True
    home = True
    vittoria = False
    informazioni = False
    personaggi = False 
    gioco = False
    fineGioco = False 
    Livello1 = False 
    Livello2 = False 
    Livello3 = False 
    Livello4 = False 
    Livello5 = False 
    Livello6 = False 
    Livello7 = False 
    Livello8 = False

    # --- INIZIALIZZAZIONE LIVELLI ---
    livello_corrente = None  # es: "Livello1", "Livello2", ...
    fineGioco = False

    # --- FUNZIONE RESET ---
    def reset_gioco():
        global player_rect, sedia_rect, banco_rect
        global vel_y, al_suolo, is_crouching
        global banco_active, banco_start_time
        global punteggio, sedia_passata, banco_passata, campanella_attiva
        global Livello1, Livello2, Livello3, Livello4, Livello5, Livello6, Livello7, Livello8
        global fineGioco, vittoria
        global oscillazione_sedia, direzione_sedia
        global home, informazioni, personaggi
        
        home = False
        informazioni = False
        personaggi = False
        
        oscillazione_sedia = 0
        direzione_sedia = 1

        oscillazione_banco = 0
        direzione_banco = 1 
        
        player_rect = pygame.Rect(100, 0, larghezza_player, altezza_normale)
        player_rect.bottom = ground_y
        sedia_rect = pygame.Rect(1200, 0, sedia_width, sedia_height)
        sedia_rect.bottom = ground_y
        banco_rect = pygame.Rect(1200, 0, banco_width, banco_height)
        banco_rect.bottom = ground_y + 15
        
        # Reset giocatore
        player_rect.x = 100
        player_rect.height = altezza_normale
        player_rect.bottom = ground_y
        vel_y = 0
        al_suolo = True
        is_crouching = False
        
        # Reset nemici
        sedia_rect.x = 1200
        sedia_rect.bottom = ground_y
        banco_rect.x = 1200
        banco_rect.bottom = ground_y + 15  # banco parte più avanti della sedia
        
        # --- Reset banco attivo e punteggio ---
        banco_active = False
        banco_start_time = pygame.time.get_ticks()
        sedia_passata = False
        banco_passato = False
        campanella_attiva = False
        punteggio = 0

        Livello1 = Livello2 = Livello3 = Livello4 = False
        Livello5 = Livello6 = Livello7 = Livello8 = False

        # Reset fine gioco e vittoria
        fineGioco = False
        vittoria = False

    while running:
        mPos = pygame.mouse.get_pos() 
        keys = pygame.key.get_pressed()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and fineGioco:
                    reset_gioco()
                    fineGioco = False
                    banco_rect.x = SCREEN_WIDTH
                    player_rect.bottom = ground_y
                    vel_y = 0
                    banco_passato = False
                    campanella_attiva = False
                    home = True
                    personaggi = False
                    punteggio = 0
                    
                    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and vittoria:
                    reset_gioco()
                    fineGioco = False
                    banco_rect.x = SCREEN_WIDTH
                    player_rect.bottom = ground_y
                    vel_y = 0
                    banco_passato = False
                    campanella_attiva = False
                    home = True
                    personaggi = True
                    punteggio = 0
                        
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # Click sinistro 
                    # 1. Se sono in Home e clicco Start -> vado a Personaggi
                    if home and buttonStart.collidepoint(mPos):
                        home = False
                        personaggi = True
                    # 2. Se sono in Personaggi e clicco Livello 1 -> vado a Schermata Rossa
                    elif personaggi and buttonGinnastica.collidepoint(mPos):
                        personaggi = False
                        Livello1 = True
                        Livello2 = False
                        Livello3 = False
                        Livello4 = False
                        Livello5 = False
                        Livello6 = False
                        Livello7 = False
                        Livello8 = False
                        home = False
                       
                    elif personaggi and buttonStoFilo.collidepoint(mPos):
                        personaggi = False
                        Livello1 = False
                        Livello2 = True
                        Livello3 = False
                        Livello4 = False
                        Livello5 = False
                        Livello6 = False
                        Livello7 = False
                        Livello8 = False
                        home = False
                        screen.blit(imgLivello, (0, 0))
                        
                    elif personaggi and buttonArte.collidepoint(mPos):
                        personaggi = False
                        Livello1 = False
                        Livello2 = False
                        Livello3 = True
                        Livello4 = False
                        Livello5 = False
                        Livello6 = False
                        Livello7 = False
                        Livello8 = False
                        home = False
                        screen.blit(imgLivello, (0, 0))
                        
                    elif personaggi and buttonInglese.collidepoint(mPos):
                        personaggi = False
                        Livello1 = False
                        Livello2 = False
                        Livello3 = False
                        Livello4 = True
                        Livello5 = False
                        Livello6 = False
                        Livello7 = False
                        Livello8 = False
                        home = False
                        screen.blit(imgLivello, (0, 0))
                    
                    elif personaggi and buttonMatematica.collidepoint(mPos):
                        personaggi = False
                        Livello1 = False
                        Livello2 = False
                        Livello3 = False
                        Livello4 = False
                        Livello5 = True
                        Livello6 = False
                        Livello7 = False
                        Livello8 = False
                        home = False
                        screen.blit(imgLivello, (0, 0))
                     
                    elif personaggi and buttonFisica.collidepoint(mPos):
                        personaggi = False
                        Livello1 = False
                        Livello2 = False
                        Livello3 = False
                        Livello4 = False
                        Livello5 = False
                        Livello6 = True
                        Livello7 = False
                        Livello8 = False
                        home = False
                        screen.blit(imgLivello, (0, 0))
                    
                    elif personaggi and buttonScienze.collidepoint(mPos):
                        personaggi = False
                        Livello1 = False
                        Livello2 = False
                        Livello3 = False
                        Livello4 = False
                        Livello5 = False
                        Livello6 = False
                        Livello7 = True
                        Livello8 = False
                        home = False
                        screen.blit(imgLivello, (0, 0))
                        
                    elif personaggi and buttonInformatica.collidepoint(mPos):
                        personaggi = False
                        Livello1 = False
                        Livello2 = False
                        Livello3 = False
                        Livello4 = False
                        Livello5 = False
                        Livello6 = False
                        Livello7 = False
                        Livello8 = True
                        home = False
                        screen.blit(imgLivello, (0, 0))
                        
                    elif home and buttonInfo.collidepoint(mPos):
                        home = False
                        personaggi = False
                        informazioni = True 
                        
                        
        #se ci troviamo nella schermata home
        if home: 
            screen.blit(imgSfondoPrincipale,(0,0) )
            
            #bottone start
            buttonColorI = "white"
            if buttonInfo.collidepoint(mPos):
                buttonColorI = "dark grey"
            buttonI = pygame.draw.rect(screen,buttonColorI,buttonInfo)
            screen.blit(parolaButtonInfo, (SCREEN_WIDTH // 2.445, SCREEN_HEIGHT // 1.235))
            
            #bottone personaggi
            buttonColorS = "white"
            if buttonStart.collidepoint(mPos):
                buttonColorS = "dark grey"
            buttonS = pygame.draw.rect(screen,buttonColorS,buttonStart)
            screen.blit(parolaButtonStart, (SCREEN_WIDTH // 2.16, SCREEN_HEIGHT // 1.475))
       
        #se ci troviamo nel gioco
        elif personaggi:
            screen.blit(imgSfondoPersonaggi,(0,0))
            
            #inserisco immagine prof di ginnastica e bottone livello 1 nella schermata dei personaggi
            screen.blit(imgGinnastica, (48, 100))
            buttonGinnastica = pygame.Rect(SCREEN_WIDTH // 14.4, SCREEN_HEIGHT // 2.25, 230, 60)
            parolaButtonGinn = Normalfont.render("Livello 1", True, "black")
            
            buttonColorG = "white"
            if buttonGinnastica.collidepoint(mPos):
                buttonColorG = "dark grey"
            buttonG = pygame.draw.rect(screen,buttonColorG,buttonGinnastica)
            screen.blit(parolaButtonGinn, (SCREEN_WIDTH // 12.5, SCREEN_HEIGHT // 2.3))
            
            #inserisco immagine prof di storia e filosofia e bottone livello 2 nella schermata dei personaggi
            screen.blit(imgStofilo, (510, 140))
            buttonStoFilo = pygame.Rect(SCREEN_WIDTH // 3.37, SCREEN_HEIGHT // 2.25, 230, 60)
            parolaButtonStoFilo = Normalfont.render("Livello 2", True, "black")
            
            buttonColorStoFilo = "white"
            if buttonStoFilo.collidepoint(mPos):
                buttonColorStoFilo = "dark grey"
            buttonSF = pygame.draw.rect(screen,buttonColorStoFilo,buttonStoFilo)
            screen.blit(parolaButtonStoFilo, (SCREEN_WIDTH // 3.27, SCREEN_HEIGHT // 2.3))
            
            #inserisco immagine prof di arte e bottone livello 3 nella schermata dei personaggi
            screen.blit(imgArte, (870, 135))
            buttonArte = pygame.Rect(SCREEN_WIDTH // 1.89, SCREEN_HEIGHT // 2.25, 230, 60)
            parolaButtonArte = Normalfont.render("Livello 3", True, "black")
            
            buttonColorArte = "white"
            if buttonArte.collidepoint(mPos):
                buttonColorArte = "dark grey"
            buttonArte = pygame.draw.rect(screen,buttonColorArte,buttonArte)
            screen.blit(parolaButtonArte, (SCREEN_WIDTH // 1.85, SCREEN_HEIGHT // 2.3))
            
            #inserisco immagine prof di inglese e bottone livello 4 nella schermata dei personaggi
            screen.blit(imgInglese, (1250, 130))
            buttonInglese = pygame.Rect(SCREEN_WIDTH // 1.32, SCREEN_HEIGHT // 2.25, 230, 60)
            parolaButtonInglese = Normalfont.render("Livello 4", True, "black")
            
            buttonColorInglese = "white"
            if buttonInglese.collidepoint(mPos):
                buttonColorInglese = "dark grey"
            buttonInglese = pygame.draw.rect(screen,buttonColorInglese,buttonInglese)
            screen.blit(parolaButtonInglese, (SCREEN_WIDTH // 1.3, SCREEN_HEIGHT // 2.3))
            
            #inserisco immagine prof di matematica e bottone livello 5 nella schermata dei personaggi
            screen.blit(imgMatematica, (140, 557))
            buttonMatematica = pygame.Rect(SCREEN_WIDTH // 14.4, SCREEN_HEIGHT // 1.14, 230, 60)
            parolaButtonMatematica = Normalfont.render("Livello 5", True, "black")
            
            buttonColorMatematica = "white"
            if buttonMatematica.collidepoint(mPos):
                buttonColorMatematica = "dark grey"
            buttonMatematica = pygame.draw.rect(screen,buttonColorMatematica,buttonMatematica)
            screen.blit(parolaButtonMatematica, (SCREEN_WIDTH // 12.5, SCREEN_HEIGHT // 1.15))
            
            #inserisco immagine prof di fisica e bottone livello 6 nella schermata dei personaggi
            screen.blit(imgFisica, (500, 535))
            buttonFisica = pygame.Rect(SCREEN_WIDTH // 3.37, SCREEN_HEIGHT // 1.13, 230, 60)
            parolaButtonFisica = Normalfont.render("Livello 6", True, "black")
            
            buttonColorFisica = "white"
            if buttonFisica.collidepoint(mPos):
                buttonColorFisica = "dark grey"
            buttonFisica = pygame.draw.rect(screen,buttonColorFisica,buttonFisica)
            screen.blit(parolaButtonFisica, (SCREEN_WIDTH // 3.27, SCREEN_HEIGHT // 1.14))
            
            #inserisco immagine prof di scienze e bottone livello 7 nella schermata dei personaggi
            screen.blit(imgScienze, (890, 522))
            buttonScienze = pygame.Rect(SCREEN_WIDTH // 1.89, SCREEN_HEIGHT // 1.14, 230, 60)
            parolaButtonScienze = Normalfont.render("Livello 7", True, "black")
            
            buttonColorScienze = "white"
            if buttonScienze.collidepoint(mPos):
                buttonColorScienze = "dark grey"
            buttonScienze = pygame.draw.rect(screen,buttonColorScienze,buttonScienze)
            screen.blit(parolaButtonScienze, (SCREEN_WIDTH // 1.85, SCREEN_HEIGHT // 1.15))
            
            #inserisco immagine prof di informatica e bottone livello 8 nella schermata dei personaggi
            screen.blit(imgInformatica, (1240, 537))
            buttonInformatica = pygame.Rect(SCREEN_WIDTH // 1.32, SCREEN_HEIGHT // 1.14, 230, 60)
            parolaButtonInformatica = Normalfont.render("Livello 8", True, "black")
            
            buttonColorInformatica = "white"
            if buttonInformatica.collidepoint(mPos):
                buttonColorInformatica = "dark grey"
            buttonInformatica = pygame.draw.rect(screen,buttonColorInformatica,buttonInformatica)
            screen.blit(parolaButtonInformatica, (SCREEN_WIDTH // 1.3, SCREEN_HEIGHT // 1.15))
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    home = True
                    
        elif informazioni:
            screen.blit(imgInformazioni, (0, 0))

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    informazioni = False
                    home = True
                    personaggi = False
                
                    
        elif Livello1:
            screen.blit(imgLivello, (0, 0))
            keys = pygame.key.get_pressed()

            # -------- SALTO --------
            if keys[pygame.K_SPACE] and al_suolo:
                vel_y = salto
                al_suolo = False

            # -------- GRAVITÀ --------
            vel_y += gravita
            player_rect.y += vel_y

            # Collisione col terreno
            if player_rect.bottom >= ground_y:
                player_rect.bottom = ground_y
                vel_y = 0
                al_suolo = True
                
            # --- Cambia immagine e altezza ---
            if not al_suolo:
                screen.blit(imgPers1Jump, player_rect)
            else:
                screen.blit(imgPers1, player_rect)
            
            # --- Movimento sedia solo se la campanella NON è attiva ---
            if not campanella_attiva:
                sedia_rect.x -= sedia_speed
                # Se esce dallo schermo ricompare a destra
                if sedia_rect.right < 0:
                    sedia_rect.left = SCREEN_WIDTH
                
            # quando la sedia passa il player
            if sedia_rect.right < player_rect.left and not sedia_passata:
                punteggio += 10
                sedia_passata = True

            if sedia_rect.left > player_rect.right:
                sedia_passata = False
            
            # --- Disegno sedia ---
            screen.blit(imgSedia, sedia_rect)
            
            # ---Riduce area dei nemici e personaggio ---
            sedia_hitbox = sedia_rect.inflate(-100, -100)
            player_hitbox = player_rect.inflate(-100, -100)
            campanella_hitbox = campanella_rect.inflate(-100, -100)
            
            # --- Collisione con sedia---
            if player_hitbox.colliderect(sedia_hitbox):
                fineGioco = True
                punteggio = - 10

            # Raggiungimento 100 punti --> compare la campanella
            testo_punti = font_punti.render("Punti: " + str(punteggio), True, "black")
            screen.blit(testo_punti,(50,50))
            
            if punteggio >= 100:
                campanella_attiva = True
                
            if campanella_attiva:
                campanella_rect.x -= 10
                screen.blit(imgCampanella, campanella_rect)
            
            # --- Vittoria ---
            if campanella_attiva and player_hitbox.colliderect(campanella_hitbox):
                Livello1 = False
                vittoria = True
                screen.blit(imgHaiVinto1,(0,0))
                
            if fineGioco:
                screen.blit(imgHaiPerso, (0, 0))
                # Resetta le posizioni dei nemici
                
        elif Livello2:
            screen.blit(imgLivello, (0, 0))
            keys = pygame.key.get_pressed()

            # -------- STRISCIARE --------
            if keys[pygame.K_DOWN] and al_suolo:
                is_crouching = True
                player_rect.height = altezza_crouch
                player_rect.bottom = ground_y 
            else:
                is_crouching = False
                player_rect.height = altezza_normale
                # Se non sta saltando, assicurati che i piedi tocchino terra
                if al_suolo:
                    player_rect.bottom = ground_y
                    
            # -------- GRAVITÀ --------
            vel_y += gravita
            player_rect.y += vel_y

            # Collisione col terreno
            if player_rect.bottom >= ground_y:
                player_rect.bottom = ground_y
                vel_y = 0
                al_suolo = True
                
            # --- Cambia immagine e altezza ---
            if is_crouching:
                screen.blit(imgPers2Crouch, player_rect)
            else:
                screen.blit(imgPers2, player_rect)
                
           # --- Movimento banco ---
            if not campanella_attiva:
                banco_rect.x -= banco_speed
                if banco_rect.right < 0:
                    banco_rect.left = SCREEN_WIDTH
                
            # quando il banco passa il player
            if banco_rect.right < player_rect.left and not banco_passato:
                punteggio += 15
                banco_passato = True

            if banco_rect.left > player_rect.right:
                banco_passato = False
                
            # --- Disegno banco ---
            screen.blit(imgBanco, banco_rect)
            
            # ---Riduce area dei nemici e personaggio ---
            banco_hitbox = banco_rect.inflate(-50, -50)
            player_hitbox = player_rect.inflate(-100, -100)
            campanella_hitbox = campanella_rect.inflate(-100, -100)
            
            # Collisione banco: perde solo se NON striscia
            if player_hitbox.colliderect(banco_hitbox) and not is_crouching:
                fineGioco = True
                punteggio = -15

            # Raggiungimento 150 punti --> compare la campanella
            testo_punti = font_punti.render("Punti: " + str(punteggio), True, "black")
            screen.blit(testo_punti,(50,50))
            
            if punteggio >= 150:
                campanella_attiva = True
                
            if campanella_attiva:
                campanella_rect.x -= 10
                screen.blit(imgCampanella, campanella_rect)
            
            # --- Vittoria ---
            if campanella_attiva and player_hitbox.colliderect(campanella_hitbox):
                Livello2 = False
                vittoria = True
                screen.blit(imgHaiVinto2,(0,0))
                
            if fineGioco:
                screen.blit(imgHaiPerso, (0, 0))
                # Resetta le posizioni dei nemici
                
        elif Livello3:
            screen.blit(imgLivello, (0,0))
            keys = pygame.key.get_pressed()

            # --- GESTIONE PLAYER ---
            if keys[pygame.K_SPACE] and al_suolo:
                vel_y = salto
                al_suolo = False
                
            if keys[pygame.K_DOWN] and al_suolo:
                is_crouching = True
                player_rect.height = altezza_crouch
                player_rect.bottom = ground_y
                
            else:
                is_crouching = False
                player_rect.height = altezza_normale
                if al_suolo:
                    player_rect.bottom = ground_y

            vel_y += gravita
            player_rect.y += vel_y
            if player_rect.bottom >= ground_y:
                player_rect.bottom = ground_y
                vel_y = 0
                al_suolo = True

            # --- Cambio immagine ---
            if not al_suolo:
                screen.blit(imgPers3Jump, player_rect)
            elif is_crouching:
                screen.blit(imgPers3Crouch, player_rect)
            else:
                screen.blit(imgPers3, player_rect)

            # --- Muove sedia e banco insieme ---
            if not campanella_attiva:
                sedia_rect.x -= sedia_speed
                banco_rect.x -= banco_speed  # stessa velocità per semplicità

                # Se escono dallo schermo, ricompaiono a destra
                if sedia_rect.right < 0 and banco_rect.right < 0:
                    sedia_rect.left = SCREEN_WIDTH
                    banco_rect.left = SCREEN_WIDTH + 1000  # distanza tra sedia e banco
                    sedia_passata = False
                    banco_passato = False

            # --- Disegna sedia e banco ---
            screen.blit(imgSedia, sedia_rect)
            screen.blit(imgBanco, banco_rect)

            # --- Riduzione hitbox ---
            sedia_hitbox = sedia_rect.inflate(-100, -100)
            banco_hitbox = banco_rect.inflate(-50, -50)
            player_hitbox = player_rect.inflate(-100, -100)
            campanella_hitbox = campanella_rect.inflate(-100, -100)

            # --- Collisione ---
            if player_hitbox.colliderect(sedia_hitbox) or (player_hitbox.colliderect(banco_hitbox) and not is_crouching):
                fineGioco = True
                punteggio = - 15
                reset_gioco()

            # --- Punti quando passano ---
            if sedia_rect.right < player_rect.left and not sedia_passata:
                punteggio += 10
                sedia_passata = True
            if banco_rect.right < player_rect.left and not banco_passato:
                punteggio += 15
                banco_passato = True

            # Raggiungimento 200 punti --> compare la campanella
            testo_punti = font_punti.render("Punti: " + str(punteggio), True, "black")
            screen.blit(testo_punti, (50,50))

            if punteggio >= 200:
                campanella_attiva = True
                
            if campanella_attiva:
                campanella_rect.x -= 10
                screen.blit(imgCampanella, campanella_rect)

            # --- Vittoria ---
            if campanella_attiva and player_hitbox.colliderect(campanella_hitbox):
                Livello3 = False
                vittoria = True
                screen.blit(imgHaiVinto3,(0,0))  # puoi cambiare immagine livello3

            if fineGioco:
                screen.blit(imgHaiPerso, (0,0))   
                
        elif Livello4:
            screen.blit(imgLivello, (0, 0))
            keys = pygame.key.get_pressed()

            # -------- SALTO --------
            if keys[pygame.K_SPACE] and al_suolo:
                vel_y = salto
                al_suolo = False

            # -------- GRAVITÀ --------
            vel_y += gravita
            player_rect.y += vel_y

            if player_rect.bottom >= ground_y:
                player_rect.bottom = ground_y
                vel_y = 0
                al_suolo = True

            # --- Disegno player ---
            if not al_suolo:
                screen.blit(imgPers4Jump, player_rect)
            else:
                screen.blit(imgPers4, player_rect)

            # --- Movimento sedia ---
            sedia_rect.x -= sedia_speed

            # --- Oscillazione verticale ---
            oscillazione_sedia += direzione_sedia * 2

            if oscillazione_sedia > 80 or oscillazione_sedia < -80:
                direzione_sedia *= -1

            sedia_rect.bottom = ground_y + oscillazione_sedia

            # --- Reset posizione sedia ---
            if sedia_rect.right < 0:
                sedia_rect.left = SCREEN_WIDTH
                sedia_passata = False

            # --- Disegno sedia ---
            screen.blit(imgSedia, sedia_rect)

            # --- Hitbox ---
            sedia_hitbox = sedia_rect.inflate(-100, -100)
            player_hitbox = player_rect.inflate(-100, -100)
            campanella_hitbox = campanella_rect.inflate(-100, -100)

            # --- Collisione con la sedia ---
            if player_hitbox.colliderect(sedia_hitbox):
                fineGioco = True
                punteggio = 0

            # --- Punteggio nello schermo ---
            if sedia_rect.right < player_rect.left and not sedia_passata:
                punteggio += 25
                sedia_passata = True
            
            # Raggiungimento 250 punti --> compare la campanella
            testo_punti = font_punti.render("Punti: " + str(punteggio), True, "black")
            screen.blit(testo_punti,(50,50))

            if punteggio >= 250:
                campanella_attiva = True

            if campanella_attiva:
                campanella_rect.x -= 10
                screen.blit(imgCampanella, campanella_rect)

            # vittoria
            if campanella_attiva and player_hitbox.colliderect(campanella_hitbox):
                Livello4 = False
                vittoria = True
                screen.blit(imgHaiVinto4,(0,0))

            if fineGioco:
                screen.blit(imgHaiPerso, (0,0))
                
        elif Livello5:
            screen.blit(imgLivello, (0, 0))
            keys = pygame.key.get_pressed()

            # -------- STRISCIARE --------
            if keys[pygame.K_DOWN] and al_suolo:
                is_crouching = True
                player_rect.height = altezza_crouch
                player_rect.bottom = ground_y
            else:
                is_crouching = False
                player_rect.height = altezza_normale
                if al_suolo:
                    player_rect.bottom = ground_y

            # -------- GRAVITÀ --------
            vel_y += gravita
            player_rect.y += vel_y

            if player_rect.bottom >= ground_y:
                player_rect.bottom = ground_y
                vel_y = 0
                al_suolo = True

            # --- Disegno player ---
            if is_crouching:
                screen.blit(imgPers5Crouch, player_rect)
            else:
                screen.blit(imgPers5, player_rect)

            # --- Movimento banco ---
            banco_rect.x -= banco_speed

            # --- Oscillazione verticale ---
            oscillazione_banco += direzione_banco * 2

            if oscillazione_banco > 80 or oscillazione_banco < -80:
                direzione_banco *= -1

            banco_rect.bottom = ground_y + oscillazione_banco

            # Reset posizione
            if banco_rect.right < 0:
                banco_rect.left = SCREEN_WIDTH
                banco_passato = False

            # --- Disegno banco ---
            screen.blit(imgBanco, banco_rect)

            # --- Hitbox ---
            banco_hitbox = banco_rect.inflate(-50, -50)
            player_hitbox = player_rect.inflate(-100, -100)
            campanella_hitbox = campanella_rect.inflate(-100, -100)

            # --- Collisione con il banco ---
            if player_hitbox.colliderect(banco_hitbox) and not is_crouching:
                fineGioco = True
                punteggio = - 30

            # --- Punteggio nello schermo ---
            if banco_rect.right < player_rect.left and not banco_passato:
                punteggio += 30
                banco_passato = True

            # Raggiungimento 300 punti --> compare la campanella
            testo_punti = font_punti.render("Punti: " + str(punteggio), True, "black")
            screen.blit(testo_punti,(50,50))

            if punteggio >= 300:
                campanella_attiva = True

            if campanella_attiva:
                campanella_rect.x -= 10
                screen.blit(imgCampanella, campanella_rect)

            # --- Vittoria ---
            if campanella_attiva and player_hitbox.colliderect(campanella_hitbox):
                Livello5 = False
                vittoria = True
                screen.blit(imgHaiVinto5,(0,0))

            if fineGioco:
                screen.blit(imgHaiPerso, (0,0))    
        
        elif Livello6:
            screen.blit(imgLivello, (0, 0))
            keys = pygame.key.get_pressed()

            # -------- SALTO --------
            if keys[pygame.K_SPACE] and al_suolo:
                vel_y = salto
                al_suolo = False
        
            # -------- STRISCIARE --------
            if keys[pygame.K_DOWN] and al_suolo:
                is_crouching = True
                player_rect.height = altezza_crouch
                player_rect.bottom = ground_y
            else:
                is_crouching = False
                player_rect.height = altezza_normale
                if al_suolo:
                    player_rect.bottom = ground_y

            # -------- GRAVITÀ --------
            vel_y += gravita
            player_rect.y += vel_y

            if player_rect.bottom >= ground_y:
                player_rect.bottom = ground_y
                vel_y = 0
                al_suolo = True

            # --- Disegno player ---
            if not al_suolo:
                screen.blit(imgPers6Jump, player_rect)
            elif is_crouching:
                screen.blit(imgPers6Crouch, player_rect)
            else:
                screen.blit(imgPers6, player_rect)

            # --- Movimento nemici ---
            sedia_rect.x -= sedia_speed
            banco_rect.x -= banco_speed

            # --- Oscillazione sedia ---
            oscillazione_sedia += direzione_sedia * 2
            if oscillazione_sedia > 80 or oscillazione_sedia < -80:
                direzione_sedia *= -1

            sedia_rect.bottom = ground_y + oscillazione_sedia

            # --- Oscillazione banco ---
            oscillazione_banco += direzione_banco * 2
            if oscillazione_banco > 80 or oscillazione_banco < -80:
                direzione_banco *= -1

            banco_rect.bottom = ground_y + oscillazione_banco

            # --- Reset posizione nemici con distanza minima ---
            distanza_min = 900
            distanza_max = 1200
            spazio_minimo = 1000  # distanza minima tra sedia e banco

            # Sedia
            if sedia_rect.right < 0:
                nuova_pos_sedia = SCREEN_WIDTH + random.randint(distanza_min, distanza_max)
                # Assicura distanza dal banco
                if abs(nuova_pos_sedia - banco_rect.x) < spazio_minimo:
                    nuova_pos_sedia = banco_rect.x + spazio_minimo
                sedia_rect.left = nuova_pos_sedia
                sedia_passata = False

            # Banco
            if banco_rect.right < 0:
                nuova_pos_banco = SCREEN_WIDTH + random.randint(distanza_min, distanza_max)
                # Assicura distanza dalla sedia
                if abs(nuova_pos_banco - sedia_rect.x) < spazio_minimo:
                    nuova_pos_banco = sedia_rect.x + spazio_minimo
                banco_rect.left = nuova_pos_banco
                banco_passato = False

            # --- Disegno nemici ---
            screen.blit(imgSedia, sedia_rect)
            screen.blit(imgBanco, banco_rect)

            # --- Hitbox ---
            sedia_hitbox = sedia_rect.inflate(-100, -100)
            banco_hitbox = banco_rect.inflate(-50, -50)
            player_hitbox = player_rect.inflate(-100, -100)
            campanella_hitbox = campanella_rect.inflate(-100, -100)

            # --- Collisioni ---
            if player_hitbox.colliderect(sedia_hitbox):
                fineGioco = True
                punteggio = - 15

            if player_hitbox.colliderect(banco_hitbox) and not is_crouching:
                fineGioco = True
                punteggio = - 20

            # --- Punteggio passaggio nemici ---
            if sedia_rect.right < player_rect.left and not sedia_passata:
                punteggio += 15
                sedia_passata = True

            if banco_rect.right < player_rect.left and not banco_passato:
                punteggio += 20
                banco_passato = True
            
            # Raggiungimento 350 punti --> compare la campanella
            testo_punti = font_punti.render("Punti: " + str(punteggio), True, "black")
            screen.blit(testo_punti,(50,50))

            if punteggio >= 350:
                campanella_attiva = True

            if campanella_attiva:
                campanella_rect.x -= 10
                screen.blit(imgCampanella, campanella_rect)

            # --- Vittoria ---
            if campanella_attiva and player_hitbox.colliderect(campanella_hitbox):
                Livello6 = False
                vittoria = True
                screen.blit(imgHaiVinto6,(0,0))

            if fineGioco:
                screen.blit(imgHaiPerso, (0,0))
                   
        elif Livello7:
            screen.blit(imgLivello, (0, 0))
            keys = pygame.key.get_pressed()
            
            # --- Movimento nemico ---
            sedia_rect.x -= sedia_speed
            # Se esce dallo schermo ricompare a destra
            if sedia_rect.right < 0:
                sedia_rect.left = SCREEN_WIDTH
            
            # -------- SALTO --------
            if keys[pygame.K_SPACE] and al_suolo:
                vel_y = salto
                al_suolo = False

            # -------- STRISCIARE --------
            if keys[pygame.K_DOWN] and al_suolo:
                is_crouching = True
                player_rect.height = altezza_crouch
                player_rect.bottom = ground_y 
            else:
                is_crouching = False
                player_rect.height = altezza_normale
                # Se non sta saltando, assicurati che i piedi tocchino terra
                if al_suolo:
                    player_rect.bottom = ground_y
                    
            # -------- GRAVITÀ --------
            vel_y += gravita
            player_rect.y += vel_y

            # Collisione col terreno
            if player_rect.bottom >= ground_y:
                player_rect.bottom = ground_y
                vel_y = 0
                al_suolo = True
                
            # --- Cambia immagine e altezza ---
            if not al_suolo:
                screen.blit(imgPers7Jump, player_rect)
            elif is_crouching:
                screen.blit(imgPers7Crouch, player_rect)
            else:
                screen.blit(imgPers7, player_rect)
                
            # --- Disegno nemico ---
            screen.blit(imgSedia, sedia_rect)
            
            # ---Riduce area del nemico e personaggio ---
            sedia_hitbox = sedia_rect.inflate(-100, -100)
            player_hitbox = player_rect.inflate(-100, -100)
            
            # --- Collisione con nemico---
            if player_hitbox.colliderect(sedia_hitbox):
                fineGioco = True
                
            if fineGioco:
                screen.blit(imgHaiPerso, (0,0))
                # reset dei nemici alla posizione iniziale del livello
                sedia_rect.left = SCREEN_WIDTH
                banco_rect.left = SCREEN_WIDTH + 500
                sedia_passata = False
                banco_passata = False    
                
        elif Livello8:
            screen.blit(imgLivello, (0, 0))
            keys = pygame.key.get_pressed()
            
            # --- Movimento nemico ---
            sedia_rect.x -= sedia_speed
            # Se esce dallo schermo ricompare a destra
            if sedia_rect.right < 0:
                sedia_rect.left = SCREEN_WIDTH
            
            # -------- SALTO --------
            if keys[pygame.K_SPACE] and al_suolo:
                vel_y = salto
                al_suolo = False

            # -------- STRISCIARE --------
            if keys[pygame.K_DOWN] and al_suolo:
                is_crouching = True
                player_rect.height = altezza_crouch
                player_rect.bottom = ground_y 
            else:
                is_crouching = False
                player_rect.height = altezza_normale
                # Se non sta saltando, assicurati che i piedi tocchino terra
                if al_suolo:
                    player_rect.bottom = ground_y
                    
            # -------- GRAVITÀ --------
            vel_y += gravita
            player_rect.y += vel_y

            # Collisione col terreno
            if player_rect.bottom >= ground_y:
                player_rect.bottom = ground_y
                vel_y = 0
                al_suolo = True
                
            # --- Cambia immagine e altezza ---
            if not al_suolo:
                screen.blit(imgPers8Jump, player_rect)
            elif is_crouching:
                screen.blit(imgPers8Crouch, player_rect)
            else:
                screen.blit(imgPers8, player_rect)
            
            # --- Disegno nemico ---
            screen.blit(imgSedia, sedia_rect)
            
            # ---Riduce area del nemico e personaggio ---
            sedia_hitbox = sedia_rect.inflate(-100, -100)
            player_hitbox = player_rect.inflate(-100, -100)
            
            
            # --- Collisione con nemico---
            if player_hitbox.colliderect(sedia_hitbox):
                fineGioco = True
                
            if fineGioco:
                screen.blit(imgHaiPerso, (0, 0))
               

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    
if __name__ == "__main__":
    main()
