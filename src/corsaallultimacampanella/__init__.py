def main() -> None:
    print("Hello from corsaallultimacampanella!")
    
    import pygame
    import random #Per generare le posizioni casuali 

    pygame.init() #Inzia pygame

    suono_home = pygame.mixer.music("suonoHome.mp3") #Carica il file musicale che viene riprodotto nella schermata home e nei vari livelli
    suono_vittoria = pygame.mixer.Sound("suonoVittoria.mp3") #Carica il suono che verrà riprodotto quando il giocatore vince
    suono_fineGioco = pygame.mixer.Sound("suonoPerdita.mp3") #Carica il suono che verrà riprodotto quando il giocatore perde
    pygame.mixer.init() #Inizializza il sistema audio di pygame (senza i suoni non partono)
    pygame.mixer.music.load("suonoHome.mp3") #Carica il file della home nel mixer di pygame
    pygame.mixer.music.set_volume(0.5) #Imposta il volume della canzone al 50%
    suono_home.play(-1) #Riproduce il suono, all'infinito, nella schermata home e nei veri livelli
    
    #Dimesioni finestra del gioco
    SCREEN_WIDTH = 1600
    SCREEN_HEIGHT = 925
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #Imposta il titolo
    pygame.display.set_caption("corsa all'ultima campanella!")

    #Inserimento bottoni per ogni materia
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

    #Imposta lo sfondo della schermata HOME
    imgSfondoPrincipale = pygame.image.load("pixelscuola.png") 
    imgSfondoPrincipale = pygame.transform.scale(imgSfondoPrincipale,(SCREEN_WIDTH,SCREEN_HEIGHT))
    #Imposta lo sfondo della schermata START/PERSONAGGI
    imgSfondoPersonaggi = pygame.image.load("sfondopersonaggi.png")
    imgSfondoPersonaggi = pygame.transform.scale(imgSfondoPersonaggi,(SCREEN_WIDTH,SCREEN_HEIGHT))
    #Imposta lo sfondo della schermata INFORMAZIONI
    imgInformazioni = pygame.image.load("sfondoInformazioni.png") 
    imgInformazioni = pygame.transform.scale(imgInformazioni, (SCREEN_WIDTH, SCREEN_HEIGHT))
    
    #Inserisce le immagini dei prof nella schermata START/PERSONAGGI
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

    #Inserisce lo sfondo per ogni livello, per quando perdi o vinci
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

    #Font delle parole nei bottoni e parole 
    Normalfont = pygame.font.SysFont('Impact', 60)
    parolaButtonInfo = Normalfont.render("informazioni", True, "black")
    parolaButtonStart = Normalfont.render("start", True, "black")

    # Dati dei giocatori
    vel_y = 0 #Velocità iniziale
    gravita = 0.8
    salto = -25
    al_suolo = True #In piedi
    is_crouching = False #Sdraiato
    altezza_normale = 350
    altezza_crouch = 330
    ground_y = 800  #Altezza del pavimento nel livello
    larghezza_player = 400
    
    #Player Rect --> rettangolo pygame per disegnare e gestire il giocatore e le collisioni
    player_rect = pygame.Rect(100, 0, larghezza_player, altezza_normale)
    player_rect.bottom = ground_y

    #Immagini di ogni personaggio (in piedi, sdraiato e in aria)
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
    imgPers6Crouch = pygame.transform.scale(imgPers6Crouch, (larghezza_player - 10, altezza_crouch - 75))
    imgPers6Jump = pygame.image.load("fisicasalto.png").convert_alpha()
    imgPers6Jump = pygame.transform.scale(imgPers6Jump, (larghezza_player - 50, altezza_normale - 100))

    imgPers7 = pygame.image.load("pixelscienze.png").convert_alpha()
    imgPers7 = pygame.transform.scale(imgPers7, (larghezza_player - 230, altezza_normale))
    imgPers7Crouch = pygame.image.load("scienzesdraiato.png").convert_alpha()
    imgPers7Crouch = pygame.transform.scale(imgPers7Crouch, (larghezza_player - 40, altezza_crouch - 160))
    imgPers7Jump = pygame.image.load("scienzesalto.png").convert_alpha()
    imgPers7Jump = pygame.transform.scale(imgPers7Jump, (larghezza_player -50, altezza_normale - 150))

    imgPers8 = pygame.image.load("pixelinfo.png").convert_alpha()
    imgPers8 = pygame.transform.scale(imgPers8, (larghezza_player - 200, altezza_normale - 10))
    imgPers8Crouch = pygame.image.load("informaticasdraiato.png").convert_alpha()
    imgPers8Crouch = pygame.transform.scale(imgPers8Crouch, (larghezza_player - 5, altezza_crouch - 60))
    imgPers8Jump = pygame.image.load("infosalto.png").convert_alpha()
    imgPers8Jump = pygame.transform.scale(imgPers8Jump, (larghezza_player - 60, altezza_normale - 75))

    # - NEMICO SEDIA
    sedia_width = 160 #Larghezza sedia
    sedia_height = 190 #Altezza sedia
    sedia_rect = pygame.Rect(1200, 0, sedia_width, sedia_height) #Rettangolo pygame per disegnare e gestire la sedia e le collisioni
    sedia_rect.bottom = ground_y #Sedia si trova all'altezza del terreno
    sedia_rect.left = 1200
    sedia_speed = 15 #Velocità sedia
    imgSedia = pygame.image.load("sedia.png").convert_alpha() #Inserimento dell'immagine della sedia
    imgSedia = pygame.transform.scale(imgSedia, (sedia_width, sedia_height)) #Ridimensione dell'immagine della sedia

    # - NEMICO BANCO
    banco_width = 380 #Larghezza banco
    banco_height = 200 #Altezza banco
    banco_rect = pygame.Rect(1200, 0, banco_width, banco_height) #Rettangolo pygame per disegnare e gestire il banco e le collisioni
    banco_rect.bottom = ground_y + 15 #Il banco si trova leggermente più alto del terreno
    banco_rect.left = 1200 + 1000 
    banco_speed = 15 #Velocità banco
    banco_active = False #All'inzio il banco è inattivo(fermo)
    banco_start_time = pygame.time.get_ticks()
    imgBanco = pygame.image.load("banco.png").convert_alpha() #Inserimento dell'immagine del banco
    imgBanco = pygame.transform.scale(imgBanco, (banco_width, banco_height)) #Ridimensione dell'immagine del banco
    
    # - NEMICO LIBRO 
    libro_rect = pygame.Rect(800, -100, 100, 100) #Rettangolo pygame per disegnare e gestire il libro e le collisioni
    libro_vel = 0 #Velocità libro
    gravita_libro = 1
    libro_attivo = True
    shake_timer = 0 # tempo per cui lo schermo trema
    imgLibroScienze = pygame.image.load("libroScienze.png").convert_alpha() #Inserimento dell'immagine del libro
    imgLibroScienze = pygame.transform.scale(imgLibroScienze, ( 100, 100)) #Ridimensione dell'immagine del libro
    
    # - NEMICO COMPUTER
    computer_rect = pygame.Rect(800, -100, 100, 100) #Rettangolo pygame per disegnare e gestire il computer e le collisioni
    computer_vel = 0 #Velocità computer
    gravita_computer = 1
    computer_attivo = True
    shake_timer = 0 # tempo per cui lo schermo trema
    imgComputer = pygame.image.load("computer.png").convert_alpha() #Inserimento dell'immagine del computer
    imgComputer = pygame.transform.scale(imgComputer, ( 100, 100)) #Ridimensione dell'immagine del computer

    # - PUNTEGGIO 
    punteggio = 0 #Parte da zero ad aumenta quando il giocatore passa il nemico
    font_punti = pygame.font.SysFont('Impact', 50)
    sedia_passata = False
    banco_passato = False
    
    # - CAMPANELLA
    campanella_attiva = False #Quando arrivi alla fine del livello arriva la campanella --> hai vinto!
    campanella_rect = pygame.Rect(1200, ground_y - 200, 120, 120) #Rettangolo pygame per disegnare e gestire la campanella e le collisioni
    imgCampanella = pygame.image.load("campanella.png").convert_alpha() #Inserimento dell'immagine della campanella 
    imgCampanella = pygame.transform.scale(imgCampanella,(200,200)) #Ridimensione dell'immagine della campanella

    #Oscillazione nemici
    oscillazione_sedia = 0
    direzione_sedia = 1
    oscillazione_banco = 0
    direzione_banco = 1
    offset = 0
    vel_oscillazione = 0.05
    ampiezza = 40

    clock = pygame.time.Clock()
    
    #Inizializza tutti gli stati del gioco (schermate, livelli, vittoria, perdita)
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

    # - INIZIALIZZAZIONE LIVELLI
    livello_corrente = None  #livello in cui ti trovi (Livello1, Livello2,....)
    fineGioco = False

    # FUNZIONE RESET --> resetta ogni schermata, livello, nemico, giocatore quando si perde o si vince 
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
        
        #Reset giocatore
        player_rect.x = 100
        player_rect.height = altezza_normale
        player_rect.bottom = ground_y
        vel_y = 0
        al_suolo = True
        is_crouching = False
        
        #Reset nemici
        sedia_rect.x = 1200
        sedia_rect.bottom = ground_y
        banco_rect.x = 1200
        banco_rect.bottom = ground_y + 15  #Banco parte più avanti della sedia
        
        #Reset banco attivo e punteggio
        banco_active = False
        banco_start_time = pygame.time.get_ticks()
        sedia_passata = False
        banco_passato = False
        campanella_attiva = False
        punteggio = 0
        
        #Resetta tutti i livelli
        Livello1 = Livello2 = Livello3 = Livello4 = False
        Livello5 = Livello6 = Livello7 = Livello8 = False

        #Reset fine gioco e vittoria
        fineGioco = False
        vittoria = False

    while running:
        mPos = pygame.mouse.get_pos() 
        keys = pygame.key.get_pressed()
        
        #Premendo ESC si chiude la finestra del gioco
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            
            #Premendo ENTER/INVIO dopo la sconfitta il gioco si resetta
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and fineGioco:
                    reset_gioco()
                    fineGioco = False
                    banco_rect.x = SCREEN_WIDTH
                    player_rect.x = 100
                    player_rect.bottom = ground_y
                    vel_y = 0
                    banco_passato = False
                    campanella_attiva = False
                    home = True
                    personaggi = False
                    punteggio = 0
                    suono_fineGioco.stop()
                    suono_home.play()
                    
            #Premendo ENTER/INVIO dopo la vittoria il gioco si resetta           
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and vittoria:
                    reset_gioco()
                    fineGioco = False
                    banco_rect.x = SCREEN_WIDTH
                    player_rect.x = 100
                    player_rect.bottom = ground_y
                    vel_y = 0
                    banco_passato = False
                    campanella_attiva = False
                    home = True
                    personaggi = True
                    punteggio = 0
                    suono_vittoria.stop()
                    suono_home.play()
                        
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: #Click sul tasto SINISTRO del mouse 
                    #Se sono in Home e clicco Start --> vado a Personaggi
                    if home and buttonStart.collidepoint(mPos):
                        home = False
                        personaggi = True
                    #Se sono in Personaggi e clicco Livello1 entro nel livello
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
                    #Se sono in Personaggi e clicco Livello2 entro nel livello  
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
                    #Se sono in Personaggi e clicco Livello3 entro nel livello    
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
                    #Se sono in Personaggi e clicco Livello4 entro nel livello    
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
                    #Se sono in Personaggi e clicco Livello5 entro nel livello
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
                    #Se sono in Personaggi e clicco Livello6 entro nel livello 
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
                    #Se sono in Personaggi e clicco Livello7 entro nel livello
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
                    #Se sono in Personaggi e clicco Livello8 entro nel livello   
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
                    #Se sono nella schermata Home e clicco INFORMAZIONI posso leggere il regolamento  
                    elif home and buttonInfo.collidepoint(mPos):
                        home = False
                        personaggi = False
                        informazioni = True
                                       
        #Se ci troviamo nella schermata home
        if home: 
            screen.blit(imgSfondoPrincipale,(0,0) )
            
            #Bottone INFORMAZIONI
            buttonColorI = "white"
            if buttonInfo.collidepoint(mPos):
                buttonColorI = "dark grey"
            buttonI = pygame.draw.rect(screen,buttonColorI,buttonInfo)
            screen.blit(parolaButtonInfo, (SCREEN_WIDTH // 2.445, SCREEN_HEIGHT // 1.235))
            
            #Bottone START/PERSONAGGI
            buttonColorS = "white"
            if buttonStart.collidepoint(mPos):
                buttonColorS = "dark grey"
            buttonS = pygame.draw.rect(screen,buttonColorS,buttonStart)
            screen.blit(parolaButtonStart, (SCREEN_WIDTH // 2.16, SCREEN_HEIGHT // 1.475))
       
        #Se ci troviamo in start/personaggi
        elif personaggi:
            screen.blit(imgSfondoPersonaggi,(0,0)) #Inserisco sfondo 
            
            #Inserisco immagine prof di ginnastica e bottone livello1
            screen.blit(imgGinnastica, (48, 100))
            buttonGinnastica = pygame.Rect(SCREEN_WIDTH // 14.4, SCREEN_HEIGHT // 2.25, 230, 60)
            parolaButtonGinn = Normalfont.render("Livello 1", True, "black")
            
            buttonColorG = "white"
            if buttonGinnastica.collidepoint(mPos):
                buttonColorG = "dark grey"
            buttonG = pygame.draw.rect(screen,buttonColorG,buttonGinnastica)
            screen.blit(parolaButtonGinn, (SCREEN_WIDTH // 12.5, SCREEN_HEIGHT // 2.3))
            
            #Inserisco immagine prof di storia e filosofia e bottone livello2
            screen.blit(imgStofilo, (510, 140))
            buttonStoFilo = pygame.Rect(SCREEN_WIDTH // 3.37, SCREEN_HEIGHT // 2.25, 230, 60)
            parolaButtonStoFilo = Normalfont.render("Livello 2", True, "black")
            
            buttonColorStoFilo = "white"
            if buttonStoFilo.collidepoint(mPos):
                buttonColorStoFilo = "dark grey"
            buttonSF = pygame.draw.rect(screen,buttonColorStoFilo,buttonStoFilo)
            screen.blit(parolaButtonStoFilo, (SCREEN_WIDTH // 3.27, SCREEN_HEIGHT // 2.3))
            
            #Inserisco immagine prof di arte e bottone livello3
            screen.blit(imgArte, (870, 135))
            buttonArte = pygame.Rect(SCREEN_WIDTH // 1.89, SCREEN_HEIGHT // 2.25, 230, 60)
            parolaButtonArte = Normalfont.render("Livello 3", True, "black")
            
            buttonColorArte = "white"
            if buttonArte.collidepoint(mPos):
                buttonColorArte = "dark grey"
            buttonArte = pygame.draw.rect(screen,buttonColorArte,buttonArte)
            screen.blit(parolaButtonArte, (SCREEN_WIDTH // 1.85, SCREEN_HEIGHT // 2.3))
            
            #Inserisco immagine prof di inglese e bottone livello4
            screen.blit(imgInglese, (1250, 130))
            buttonInglese = pygame.Rect(SCREEN_WIDTH // 1.32, SCREEN_HEIGHT // 2.25, 230, 60)
            parolaButtonInglese = Normalfont.render("Livello 4", True, "black")
            
            buttonColorInglese = "white"
            if buttonInglese.collidepoint(mPos):
                buttonColorInglese = "dark grey"
            buttonInglese = pygame.draw.rect(screen,buttonColorInglese,buttonInglese)
            screen.blit(parolaButtonInglese, (SCREEN_WIDTH // 1.3, SCREEN_HEIGHT // 2.3))
            
            #inserisco immagine prof di matematica e bottone livello5
            screen.blit(imgMatematica, (140, 557))
            buttonMatematica = pygame.Rect(SCREEN_WIDTH // 14.4, SCREEN_HEIGHT // 1.14, 230, 60)
            parolaButtonMatematica = Normalfont.render("Livello 5", True, "black")
            
            buttonColorMatematica = "white"
            if buttonMatematica.collidepoint(mPos):
                buttonColorMatematica = "dark grey"
            buttonMatematica = pygame.draw.rect(screen,buttonColorMatematica,buttonMatematica)
            screen.blit(parolaButtonMatematica, (SCREEN_WIDTH // 12.5, SCREEN_HEIGHT // 1.15))
            
            #inserisco immagine prof di fisica e bottone livello6
            screen.blit(imgFisica, (500, 535))
            buttonFisica = pygame.Rect(SCREEN_WIDTH // 3.37, SCREEN_HEIGHT // 1.13, 230, 60)
            parolaButtonFisica = Normalfont.render("Livello 6", True, "black")
            
            buttonColorFisica = "white"
            if buttonFisica.collidepoint(mPos):
                buttonColorFisica = "dark grey"
            buttonFisica = pygame.draw.rect(screen,buttonColorFisica,buttonFisica)
            screen.blit(parolaButtonFisica, (SCREEN_WIDTH // 3.27, SCREEN_HEIGHT // 1.14))
            
            #inserisco immagine prof di scienze e bottone livello7
            screen.blit(imgScienze, (890, 522))
            buttonScienze = pygame.Rect(SCREEN_WIDTH // 1.89, SCREEN_HEIGHT // 1.14, 230, 60)
            parolaButtonScienze = Normalfont.render("Livello 7", True, "black")
            
            buttonColorScienze = "white"
            if buttonScienze.collidepoint(mPos):
                buttonColorScienze = "dark grey"
            buttonScienze = pygame.draw.rect(screen,buttonColorScienze,buttonScienze)
            screen.blit(parolaButtonScienze, (SCREEN_WIDTH // 1.85, SCREEN_HEIGHT // 1.15))
            
            #inserisco immagine prof di informatica e bottone livello8
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
        
        #Se ci troviamo in informazioni
        elif informazioni:
            screen.blit(imgInformazioni, (0, 0)) #Inserisco sfondo
            #Se premo ENTER/INVIO torno alla schermata home
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    informazioni = False
                    home = True
                    personaggi = False
                    
        #Se ci troviamo nel Livello1             
        elif Livello1:
            screen.blit(imgLivello, (0, 0)) #Inserisco sfondo
            keys = pygame.key.get_pressed() #Legge quali tasti della tastiera sono premuti nei vari momenti

            #SALTO --> se premo SPACE il giocatore SALTA
            if keys[pygame.K_SPACE] and al_suolo:
                vel_y = salto
                al_suolo = False

            #Gravità
            vel_y += gravita
            player_rect.y += vel_y
            #Collisione col terreno
            if player_rect.bottom >= ground_y:
                player_rect.bottom = ground_y
                vel_y = 0
                al_suolo = True
                
            #Cambia immagine e altezza
            if not al_suolo:
                screen.blit(imgPers1Jump, player_rect) #Se salta --> imgPersJump
            else:
                screen.blit(imgPers1, player_rect) #Se torna a terra --> imgPers
            
            #Movimento sedia solo se la campanella NON è attiva
            if not campanella_attiva:
                sedia_rect.x -= sedia_speed
                #Se esce dallo schermo ricompare a destra
                if sedia_rect.right < 0:
                    sedia_rect.left = SCREEN_WIDTH
                
            #Quando il giovatore passa la sedia
            if sedia_rect.right < player_rect.left and not sedia_passata:
                punteggio += 10 #Aggiunge 10 punti
                sedia_passata = True

            if sedia_rect.left > player_rect.right:
                sedia_passata = False
            
            #Disegno sedia
            screen.blit(imgSedia, sedia_rect)
            
            #Hitbox --> Riduce area del giocatore, della sedia e della camopanella
            sedia_hitbox = sedia_rect.inflate(-100, -100)
            player_hitbox = player_rect.inflate(-100, -100)
            campanella_hitbox = campanella_rect.inflate(-100, -100)
            
            #Se il giocatore colpisce la sedia
            if player_hitbox.colliderect(sedia_hitbox):
                fineGioco = True #Perde
                punteggio = - 10 #Azzerra il punteggio
                suono_home.stop() #Ferma la musica che sta suonando
                pygame.mixer.music.load("suonoPerdita.mp3") #Carica il nuovo file musicale di sconfitta nel mixer di pygame
                pygame.mixer.music.set_volume(0.5) #Imposta il volume della canzone
                suono_fineGioco.play() #Riproduce il suono di sconfitta

            #Inserimento del testo del punteggio nella schermata di gioco (in alto a sinistra)
            testo_punti = font_punti.render("Punti: " + str(punteggio), True, "black")
            screen.blit(testo_punti,(50,50))
            
            #Raggiungo 100 punti --> compare la campanella
            if punteggio >= 100:
                campanella_attiva = True   
            if campanella_attiva:
                campanella_rect.x -= 10
                screen.blit(imgCampanella, campanella_rect)
            
            #Se il giocatore colpisce la campanella --> hai vinto
            if campanella_attiva and player_hitbox.colliderect(campanella_hitbox):
                Livello1 = False
                vittoria = True
                screen.blit(imgHaiVinto1,(0,0))
                suono_home.stop() #Ferma la musica che sta suonando
                pygame.mixer.music.load("suonoVittoria.mp3") #Carica il nuovo file musicale di vittoria nel mixer di pygame
                pygame.mixer.music.set_volume(0.5) #Imposta il volume della canzone
                suono_vittoria.play() #Riproduce il suono di vittoria
                
            if fineGioco:
                screen.blit(imgHaiPerso, (0, 0))
                
        #Se ci troviamo nel Livello2        
        elif Livello2:
            screen.blit(imgLivello, (0, 0)) #Inserisce sfondo
            keys = pygame.key.get_pressed() #Legge quali tasti della tastiera sono premuti nei vari momenti

            #STRISCIARE --> se premo FRECCETTA IN BASSO il giocatore STRISCIA
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
                    
            #Gravità
            vel_y += gravita
            player_rect.y += vel_y
            #Collisione col terreno
            if player_rect.bottom >= ground_y:
                player_rect.bottom = ground_y
                vel_y = 0
                al_suolo = True
                
            #Cambia immagine e altezza
            if is_crouching:
                screen.blit(imgPers2Crouch, player_rect) #Se striscia --> imgPersCrouch
            else:
                screen.blit(imgPers2, player_rect) #Se torna in piedi --> imgPers
                
            #Movimento sedia solo se la campanella NON è attiva
            if not campanella_attiva:
                banco_rect.x -= banco_speed
                #Se esce dallo schermo ricompare a destra
                if banco_rect.right < 0:
                    banco_rect.left = SCREEN_WIDTH
                
            #Quando il giocatore passa il banco
            if banco_rect.right < player_rect.left and not banco_passato:
                punteggio += 15 #Aggiunge 15 punti
                banco_passato = True

            if banco_rect.left > player_rect.right:
                banco_passato = False
                
            #Disegno banco
            screen.blit(imgBanco, banco_rect)
            
            #Hitbox --> Riduce area del giocatore, del banco e della camopanella
            banco_hitbox = banco_rect.inflate(-50, -50)
            player_hitbox = player_rect.inflate(-100, -100)
            campanella_hitbox = campanella_rect.inflate(-100, -100)
            
            #Se il giocatore colpisce la sedia
            if player_hitbox.colliderect(banco_hitbox) and not is_crouching:
                fineGioco = True #Perde
                punteggio = -15 #Azzera punteggio
                suono_home.stop() #Ferma la musica che sta suonando
                pygame.mixer.music.load("suonoPerdita.mp3") #Carica il nuovo file musicale di sconfitta nel mixer di pygame
                pygame.mixer.music.set_volume(0.5) #Imposta il volume della canzone
                suono_fineGioco.play() #Riproduce il suono di sconfitta

            #Inserimento del testo del punteggio nella schermata di gioco (in alto a sinistra)
            testo_punti = font_punti.render("Punti: " + str(punteggio), True, "black")
            screen.blit(testo_punti,(50,50))
            
            #Raggiungimento 150 punti --> compare la campanella
            if punteggio >= 150:
                campanella_attiva = True   
            if campanella_attiva:
                campanella_rect.x -= 10
                screen.blit(imgCampanella, campanella_rect)
            
            #Se il giocatore colpisce la campanella --> hai vinto
            if campanella_attiva and player_hitbox.colliderect(campanella_hitbox):
                Livello2 = False
                vittoria = True
                screen.blit(imgHaiVinto2,(0,0))
                suono_home.stop() #Ferma la musica che sta suonando
                pygame.mixer.music.load("suonoVittoria.mp3") #Carica il nuovo file musicale di vittoria nel mixer di pygame
                pygame.mixer.music.set_volume(0.5) #Imposta il volume della canzone
                suono_vittoria.play() #Riproduce il suono di vittoria
                
            if fineGioco:
                screen.blit(imgHaiPerso, (0, 0))
        
        #Se ci troviamo nel Livello3
        elif Livello3:
            screen.blit(imgLivello, (0,0)) #Inserisce sfondo
            keys = pygame.key.get_pressed() #Legge quali tasti della tastiera sono premuti nei vari momenti

            #SALTO --> se premo SPACE il giocatore SALTA
            if keys[pygame.K_SPACE] and al_suolo:
                vel_y = salto
                al_suolo = False
            #STRISCIARE --> se premo FRECCETTA IN BASSO il giocatore STRISCIA
            if keys[pygame.K_DOWN] and al_suolo:
                is_crouching = True
                player_rect.height = altezza_crouch
                player_rect.bottom = ground_y
            else:
                is_crouching = False
                player_rect.height = altezza_normale
                if al_suolo:
                    player_rect.bottom = ground_y
            
            #Gravità
            vel_y += gravita
            player_rect.y += vel_y
            #Collisione col terreno
            if player_rect.bottom >= ground_y:
                player_rect.bottom = ground_y
                vel_y = 0
                al_suolo = True

            #Cambia immagine e altezza
            if not al_suolo:
                screen.blit(imgPers3Jump, player_rect) #Se salta --> imgPersJump
            elif is_crouching:
                screen.blit(imgPers3Crouch, player_rect) #Se striscia --> imgpersCrouch
            else:
                screen.blit(imgPers3, player_rect) #Se sta in piedi --> imgPers

            #Movimento sedia e banco (insieme)
            if not campanella_attiva:
                sedia_rect.x -= sedia_speed
                banco_rect.x -= banco_speed 
                # Se i nemici escono dallo schermo, ricompaiono a destra
                if sedia_rect.right < 0 and banco_rect.right < 0:
                    sedia_rect.left = SCREEN_WIDTH
                    banco_rect.left = SCREEN_WIDTH + 1000  #Distanza tra sedia e banco
                    sedia_passata = False
                    banco_passato = False

            #Disegna sedia e banco
            screen.blit(imgSedia, sedia_rect)
            screen.blit(imgBanco, banco_rect)

            #Hitbox --> Riduce area del giocatore, del banco e della camopanella
            sedia_hitbox = sedia_rect.inflate(-100, -100)
            banco_hitbox = banco_rect.inflate(-50, -50)
            player_hitbox = player_rect.inflate(-100, -100)
            campanella_hitbox = campanella_rect.inflate(-100, -100)

            #Se il giocatore colpisce la sedia o il banco
            if player_hitbox.colliderect(sedia_hitbox) or (player_hitbox.colliderect(banco_hitbox) and not is_crouching):
                fineGioco = True #Perdi
                punteggio = - 15 #Azzera punteggio
                suono_home.stop() #Ferma la musica che sta suonando
                pygame.mixer.music.load("suonoPerdita.mp3") #Carica il nuovo file musicale di sconfitta nel mixer di pygame
                pygame.mixer.music.set_volume(0.5) #Imposta il volume della canzone
                suono_fineGioco.play() #Riproduce il suono di sconfitta

            #Se il giocatore passa la sedia 
            if sedia_rect.right < player_rect.left and not sedia_passata:
                punteggio += 10 #Aggiunge 10 punti
                sedia_passata = True
            #Se il giocatore passa il banco
            if banco_rect.right < player_rect.left and not banco_passato:
                punteggio += 15 #Aggiunge 15 punti
                banco_passato = True

            #Inserimento del testo del punteggio nella schermata di gioco (in alto a sinistra)
            testo_punti = font_punti.render("Punti: " + str(punteggio), True, "black")
            screen.blit(testo_punti, (50,50))
            
            #Raggiungimento 200 punti --> compare la campanella
            if punteggio >= 200:
                campanella_attiva = True
            if campanella_attiva:
                campanella_rect.x -= 10
                screen.blit(imgCampanella, campanella_rect)

            #Se il giocatore colpisce la campanella --> hai vinto
            if campanella_attiva and player_hitbox.colliderect(campanella_hitbox):
                Livello3 = False
                vittoria = True
                screen.blit(imgHaiVinto3,(0,0))
                suono_home.stop() #Ferma la musica che sta suonando
                pygame.mixer.music.load("suonoVittoria.mp3") #Carica il nuovo file musicale di vittoria nel mixer di pygame
                pygame.mixer.music.set_volume(0.5) #Imposta il volume della canzone
                suono_vittoria.play() #Riproduce il suono di vittoria
                
            if fineGioco:
                screen.blit(imgHaiPerso, (0,0))
                
        #Se ci troviamo nel Livello4       
        elif Livello4:
            screen.blit(imgLivello, (0, 0)) #Inserisce sfondo
            keys = pygame.key.get_pressed() #Legge quali tasti della tastiera sono premuti nei vari momenti

            #SALTO --> se premo SPACE il giocatore SALTA
            if keys[pygame.K_SPACE] and al_suolo:
                vel_y = salto
                al_suolo = False

            #Gravità
            vel_y += gravita
            player_rect.y += vel_y
            #Collisione col terreno
            if player_rect.bottom >= ground_y:
                player_rect.bottom = ground_y
                vel_y = 0
                al_suolo = True

            #Cambia immagine e altezza
            if not al_suolo:
                screen.blit(imgPers4Jump, player_rect) #Se salta --> imgPersJump
            else:
                screen.blit(imgPers4, player_rect) #Se sta in piedi --> imgPers

            #Movimento sedia
            sedia_rect.x -= sedia_speed

            #Oscillazione sedia
            oscillazione_sedia += direzione_sedia * 2
            if oscillazione_sedia > 80 or oscillazione_sedia < -80:
                direzione_sedia *= -1
            sedia_rect.bottom = ground_y + oscillazione_sedia

            #Reset posizione sedia
            if sedia_rect.right < 0:
                sedia_rect.left = SCREEN_WIDTH
                sedia_passata = False

            #Disegno sedia
            screen.blit(imgSedia, sedia_rect)

            #Hitbox --> Riduce area del giocatore, della sedia e della campanella
            sedia_hitbox = sedia_rect.inflate(-100, -100)
            player_hitbox = player_rect.inflate(-100, -100)
            campanella_hitbox = campanella_rect.inflate(-100, -100)

            #Se il giocatore colpisce la sedia
            if player_hitbox.colliderect(sedia_hitbox):
                fineGioco = True #Perde
                punteggio = -25 #Azzera punteggio
                suono_home.stop() #Ferma la musica che sta suonando
                pygame.mixer.music.load("suonoPerdita.mp3") #Carica il nuovo file musicale di sconfitta nel mixer di pygame
                pygame.mixer.music.set_volume(0.5) #Imposta il volume della canzone
                suono_fineGioco.play() #Riproduce il suono di sconfitta

            #Se il giocatore passa la sedia 
            if sedia_rect.right < player_rect.left and not sedia_passata:
                punteggio += 25 #Aggiunge 25 punti
                sedia_passata = True
            
            #Inserimento del testo del punteggio nella schermata di gioco (in alto a sinistra)
            testo_punti = font_punti.render("Punti: " + str(punteggio), True, "black")
            screen.blit(testo_punti,(50,50))
            
            # Raggiungimento 250 punti --> compare la campanella
            if punteggio >= 250:
                campanella_attiva = True
            if campanella_attiva:
                campanella_rect.x -= 10
                screen.blit(imgCampanella, campanella_rect)

            #Se il giocatore colpisce la campanella --> hai vinto
            if campanella_attiva and player_hitbox.colliderect(campanella_hitbox):
                Livello4 = False
                vittoria = True
                screen.blit(imgHaiVinto4,(0,0))
                suono_home.stop() #Ferma la musica che sta suonando
                pygame.mixer.music.load("suonoVittoria.mp3") #Carica il nuovo file musicale di vittoria nel mixer di pygame
                pygame.mixer.music.set_volume(0.5) #Imposta il volume della canzone
                suono_vittoria.play() #Riproduce il suono di vittoria

            if fineGioco:
                screen.blit(imgHaiPerso, (0,0))
                
        #Se ci troviamo nel Livello5        
        elif Livello5:
            screen.blit(imgLivello, (0, 0)) #Inserisce sfondo
            keys = pygame.key.get_pressed() #Legge quali tasti della tastiera sono premuti nei vari momenti

            #STRISCIARE --> se premo FRECCETTA IN BASSO il giocatore STRISCIA
            if keys[pygame.K_DOWN] and al_suolo:
                is_crouching = True
                player_rect.height = altezza_crouch
                player_rect.bottom = ground_y
            else:
                is_crouching = False
                player_rect.height = altezza_normale
                if al_suolo:
                    player_rect.bottom = ground_y

            #Gravità
            vel_y += gravita
            player_rect.y += vel_y
            #Collisione col terreno
            if player_rect.bottom >= ground_y:
                player_rect.bottom = ground_y
                vel_y = 0
                al_suolo = True

            #Cambia immagine e altezza
            if is_crouching:
                screen.blit(imgPers5Crouch, player_rect) #Se striscia --> imgPersCrouch
            else:
                screen.blit(imgPers5, player_rect) #Se torna in piedi --> imgPers

            #Movimento banco
            banco_rect.x -= banco_speed

            #Oscillazione banco
            oscillazione_banco += direzione_banco * 2
            if oscillazione_banco > 80 or oscillazione_banco < -80:
                direzione_banco *= -1
            banco_rect.bottom = ground_y + oscillazione_banco

            #Reset posizione banco
            if banco_rect.right < 0:
                banco_rect.left = SCREEN_WIDTH
                banco_passato = False

            #Disegno banco
            screen.blit(imgBanco, banco_rect)

            #Hitbox --> Riduce area del giocatore, del banco e della campanella
            banco_hitbox = banco_rect.inflate(-50, -50)
            player_hitbox = player_rect.inflate(-100, -100)
            campanella_hitbox = campanella_rect.inflate(-100, -100)

            #Se il giocatore colpisce il banco
            if player_hitbox.colliderect(banco_hitbox) and not is_crouching:
                fineGioco = True #Perde
                punteggio = - 30 #Azzzera punteggio
                suono_home.stop() #Ferma la musica che sta suonando
                pygame.mixer.music.load("suonoPerdita.mp3") #Carica il nuovo file musicale di sconfitta nel mixer di pygame
                pygame.mixer.music.set_volume(0.5) #Imposta il volume della canzone
                suono_fineGioco.play() #Riproduce il suono di sconfitta
                
            #Se il giocatore passa il banco
            if banco_rect.right < player_rect.left and not banco_passato:
                punteggio += 30 #Aggiunge 30 punti
                banco_passato = True

            #Inserimento del testo del punteggio nella schermata di gioco (in alto a sinistra)
            testo_punti = font_punti.render("Punti: " + str(punteggio), True, "black")
            screen.blit(testo_punti, (50,50))

            #Raggiungimento 300 punti --> compare la campanella
            if punteggio >= 300:
                campanella_attiva = True   
            if campanella_attiva:
                campanella_rect.x -= 10
                screen.blit(imgCampanella, campanella_rect)

            #Se il giocatore colpisce la campanella --> hai vinto
            if campanella_attiva and player_hitbox.colliderect(campanella_hitbox):
                Livello5 = False
                vittoria = True
                screen.blit(imgHaiVinto5, (0,0))
                suono_home.stop() #Ferma la musica che sta suonando
                pygame.mixer.music.load("suonoVittoria.mp3") #Carica il nuovo file musicale di vittoria nel mixer di pygame
                pygame.mixer.music.set_volume(0.5) #Imposta il volume della canzone
                suono_vittoria.play() #Riproduce il suono di vittoria
                
            if fineGioco:
                screen.blit(imgHaiPerso, (0,0))
                
        #Se ci troviamo nel Livello6
        elif Livello6:
            screen.blit(imgLivello, (0, 0)) #Inserisce sfondo
            keys = pygame.key.get_pressed() #Legge quali tasti della tastiera sono premuti nei vari momenti

            #SALTO --> se premo SPACE il giocatore SALTA
            if keys[pygame.K_SPACE] and al_suolo:
                vel_y = salto
                al_suolo = False
        
            #STRISCIARE --> se premo FRECCETTA IN BASSO il giocatore STRISCIA
            if keys[pygame.K_DOWN] and al_suolo:
                is_crouching = True
                player_rect.height = altezza_crouch
                player_rect.bottom = ground_y
            else:
                is_crouching = False
                player_rect.height = altezza_normale
                if al_suolo:
                    player_rect.bottom = ground_y

            #Gravità
            vel_y += gravita
            player_rect.y += vel_y
            #Collisione col terreno
            if player_rect.bottom >= ground_y:
                player_rect.bottom = ground_y
                vel_y = 0
                al_suolo = True

            #Cambia immagine e altezza
            if not al_suolo:
                screen.blit(imgPers6Jump, player_rect) #Se salta --> imgPersJump
            elif is_crouching:
                screen.blit(imgPers6Crouch, player_rect) #Se striscia --> imgPersCrouch
            else:
                screen.blit(imgPers6, player_rect) #Se torna in piedi --> imgPers

            #Movimento nemici
            sedia_rect.x -= sedia_speed
            banco_rect.x -= banco_speed

            #Oscillazione sedia
            oscillazione_sedia += direzione_sedia * 2
            if oscillazione_sedia > 80 or oscillazione_sedia < -80:
                direzione_sedia *= -1
            sedia_rect.bottom = ground_y + oscillazione_sedia

            #Oscillazione banco
            oscillazione_banco += direzione_banco * 2
            if oscillazione_banco > 80 or oscillazione_banco < -80:
                direzione_banco *= -1
            banco_rect.bottom = ground_y + oscillazione_banco
            
            #Movimento sedia e banco (insieme)
            if not campanella_attiva:
                sedia_rect.x -= sedia_speed - 15
                banco_rect.x -= banco_speed  - 15 
                #Se i nemici escono dallo schermo, ricompaiono a destra
                if sedia_rect.right < 0 and banco_rect.right < 0:
                    sedia_rect.left = SCREEN_WIDTH
                    banco_rect.left = SCREEN_WIDTH + 1000  #Distanza tra sedia e banco
                    sedia_passata = False
                    banco_passato = False

            #Disegno nemici
            screen.blit(imgSedia, sedia_rect)
            screen.blit(imgBanco, banco_rect)

            #Hitbox --> Riduce area del giocatore, dei nemici e della campanella
            sedia_hitbox = sedia_rect.inflate(-100, -100)
            banco_hitbox = banco_rect.inflate(-50, -50)
            player_hitbox = player_rect.inflate(-100, -100)
            campanella_hitbox = campanella_rect.inflate(-100, -100)

            #Se il giocatore colpisce la sedia
            if player_hitbox.colliderect(sedia_hitbox):
                fineGioco = True #Perde
                punteggio = - 15 #Azzera puntezzio
                suono_home.stop() #Ferma la musica che sta suonando
                pygame.mixer.music.load("suonoPerdita.mp3") #Carica il nuovo file musicale di sconfitta nel mixer di pygame
                pygame.mixer.music.set_volume(0.5) #Imposta il volume della canzone
                suono_fineGioco.play() #Riproduce il suono di sconfitta
            #Se il giocatore colpisce il banco
            if player_hitbox.colliderect(banco_hitbox) and not is_crouching:
                fineGioco = True #Perde
                punteggio = - 20 #Azzera punteggio
                suono_home.stop() #Ferma la musica che sta suonando
                pygame.mixer.music.load("suonoPerdita.mp3") #Carica il nuovo file musicale di sconfitta nel mixer di pygame
                pygame.mixer.music.set_volume(0.5) #Imposta il volume della canzone
                suono_fineGioco.play() #Riproduce il suono di sconfitta

            #Se il giocatore passa la sedia 
            if sedia_rect.right < player_rect.left and not sedia_passata:
                punteggio += 15 #Aggiungi 15 punti
                sedia_passata = True
            #Se il giocatore passa il banco
            if banco_rect.right < player_rect.left and not banco_passato:
                punteggio += 20 #Aggiungi 20 punti
                banco_passato = True
            
            #Inserimento del testo del punteggio nella schermata di gioco (in alto a sinistra)
            testo_punti = font_punti.render("Punti: " + str(punteggio), True, "black")
            screen.blit(testo_punti,(50,50))

            #Raggiungimento 350 punti --> compare la campanella
            if punteggio >= 350:
                campanella_attiva = True
            if campanella_attiva:
                campanella_rect.x -= 10
                screen.blit(imgCampanella, campanella_rect)

            #Se il giocatore colpisce la campanella --> hai vinto
            if campanella_attiva and player_hitbox.colliderect(campanella_hitbox):
                Livello6 = False
                vittoria = True
                screen.blit(imgHaiVinto6,(0,0))
                suono_home.stop() #Ferma la musica che sta suonando
                pygame.mixer.music.load("suonoVittoria.mp3") #Carica il nuovo file musicale di vittoria nel mixer di pygame
                pygame.mixer.music.set_volume(0.5) #Imposta il volume della canzone
                suono_vittoria.play() #Riproduce il suono di vittoria

            if fineGioco:
                screen.blit(imgHaiPerso, (0,0))
                
        #Se ci troviamo nel Livello7           
        elif Livello7:
            #Tremore schermo
            #Spostamento temporaneo dello schermo
            offset_x = 0
            offset_y = 0

            if shake_timer > 0: #Timer tremore attivo
                #Spostamento casuale della schermata (effetto "scossa")
                offset_x = random.randint(-10,10)
                offset_y = random.randint(-10,10)
                shake_timer -= 1 #Riduce il timer del tremore ad ogni frame fino a 0

            screen.blit(imgLivello, (offset_x, offset_y)) #Immagine sfondo spostato (trema)
            keys = pygame.key.get_pressed() #Legge quali tasti della tastiera sono premuti nei vari momenti
            
            #SALTO --> se premo SPACE il giocatore SALTA
            if keys[pygame.K_SPACE] and al_suolo:
                vel_y = salto
                al_suolo = False

            #STRISCIARE --> se premo FRECCETTA IN BASSO il giocatore STRISCIA
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
                    
            #Gravità
            vel_y += gravita
            player_rect.y += vel_y
            #Collisione col terreno
            if player_rect.bottom >= ground_y:
                player_rect.bottom = ground_y
                vel_y = 0
                al_suolo = True
                
            #Cambia immagine e altezza
            if not al_suolo:
                screen.blit(imgPers7Jump, player_rect) #Se salta --> imgPersJump
            elif is_crouching:
                screen.blit(imgPers7Crouch, player_rect) #Se striscia --> imgPersCrouch
            else:
                screen.blit(imgPers7, player_rect) #Se torna in piedi --> imgPers
            
            #Movimento sedia e banco (insieme)
            if not campanella_attiva:
                sedia_rect.x -= sedia_speed
                banco_rect.x -= banco_speed
                # Se escono dallo schermo, ricompaiono a destra
                if sedia_rect.right < 0 and banco_rect.right < 0:
                    sedia_rect.left = SCREEN_WIDTH
                    banco_rect.left = SCREEN_WIDTH + 1000  #Distanza tra sedia e banco
                    sedia_passata = False
                    banco_passato = False

            #Disegna sedia e banco
            screen.blit(imgSedia, sedia_rect)
            screen.blit(imgBanco, banco_rect)

            #Hitbox --> Riduce area del giocatore, dei nemici e della campanella
            sedia_hitbox = sedia_rect.inflate(-100, -100)
            banco_hitbox = banco_rect.inflate(-50, -50)
            player_hitbox = player_rect.inflate(-100, -100)
            campanella_hitbox = campanella_rect.inflate(-100, -100)
            
            #Libro che cade
            if libro_attivo:
                libro_vel += gravita_libro
                libro_rect.y += libro_vel
                screen.blit(imgLibroScienze, libro_rect)
                #Libro tocca terra
                if libro_rect.bottom >= ground_y:
                    libro_rect.bottom = ground_y
                    libro_vel = 0
                    shake_timer = 15 #Fa tremare lo sfondo
                    libro_attivo = False
            else:
                # reset libro
                libro_rect.x = random.randint(600,1200)
                libro_rect.y = -100
                libro_vel = 0
                libro_attivo = True
            
            #Se il giocatore colpisce la sedia
            if player_hitbox.colliderect(sedia_hitbox):
                fineGioco = True #Perde
                punteggio = - 15 #Azzera punteggio
                suono_home.stop() #Ferma la musica che sta suonando
                pygame.mixer.music.load("suonoPerdita.mp3") #Carica il nuovo file musicale di sconfitta nel mixer di pygame
                pygame.mixer.music.set_volume(0.5) #Imposta il volume della canzone
                suono_fineGioco.play() #Riproduce il suono di sconfitta                suono_fineGioco.play() #Riproduce il suono
            #Se il giocatore colpisce il banco
            if player_hitbox.colliderect(banco_hitbox) and not is_crouching:
                fineGioco = True #Perde
                punteggio = - 25 #Azzzera punteggio
                suono_home.stop() #Ferma la musica che sta suonando
                pygame.mixer.music.load("suonoPerdita.mp3") #Carica il nuovo file musicale di sconfitta nel mixer di pygame
                pygame.mixer.music.set_volume(0.5) #Imposta il volume della canzone
                suono_fineGioco.play() #Riproduce il suono di sconfitta
            
            #Se il giocatore passa la sedia
            if sedia_rect.right < player_rect.left and not sedia_passata:
                punteggio += 15 #Aggiunge 15 punti
                sedia_passata = True
            #Se il giocatore passa il banco
            if banco_rect.right < player_rect.left and not banco_passato:
                punteggio += 25 #Aggiunge 25 punti
                banco_passato = True
            
            #Inserimento del testo del punteggio nella schermata di gioco (in alto a sinistra)
            testo_punti = font_punti.render("Punti: " + str(punteggio), True, "black")
            screen.blit(testo_punti,(50,50))

            # Raggiungimento 400 punti --> compare la campanella
            if punteggio >= 400:
                campanella_attiva = True
            if campanella_attiva:
                campanella_rect.x -= 10
                screen.blit(imgCampanella, campanella_rect)

            #Se il giocatore colpisce la campanella --> hai vinto
            if campanella_attiva and player_hitbox.colliderect(campanella_hitbox):
                Livello6 = False
                vittoria = True
                screen.blit(imgHaiVinto7,(0,0))
                suono_home.stop() #Ferma la musica che sta suonando
                pygame.mixer.music.load("suonoVittoria.mp3") #Carica il nuovo file musicale di vittoria nel mixer di pygame
                pygame.mixer.music.set_volume(0.5) #Imposta il volume della canzone
                suono_vittoria.play() #Riproduce il suono di vittoria

            if fineGioco:
                screen.blit(imgHaiPerso, (0,0))
                
        #Se ci troviamo nel Livello8         
        elif Livello8:            
            #Tremore schermo
            #Spostamento temporaneo dello schermo
            offset_x = 0
            offset_y = 0

            if shake_timer > 0: #Timer tremore attivo
                #Spostamento casuale della schermata (effetto "scossa")
                offset_x = random.randint(-10,10)
                offset_y = random.randint(-10,10)
                shake_timer -= 1 #Riduce il timer del tremore ad ogni frame fino a 0

            screen.blit(imgLivello, (offset_x, offset_y)) #Immagine sfondo spostato (trema) 
            keys = pygame.key.get_pressed() #Legge quali tasti della tastiera sono premuti nei vari momenti

            #SALTO --> se premo SPACE il giocatore SALTA
            if keys[pygame.K_SPACE] and al_suolo:
                vel_y = salto
                al_suolo = False
        
            #STRISCIARE --> se premo FRECCETTA IN BASSO il giocatore STRISCIA
            if keys[pygame.K_DOWN] and al_suolo:
                is_crouching = True
                player_rect.height = altezza_crouch
                player_rect.bottom = ground_y
            else:
                is_crouching = False
                player_rect.height = altezza_normale
                if al_suolo:
                    player_rect.bottom = ground_y

            #Gravità
            vel_y += gravita
            player_rect.y += vel_y
            #Collisone col terreno
            if player_rect.bottom >= ground_y:
                player_rect.bottom = ground_y
                vel_y = 0
                al_suolo = True

            #Cambia immagine e altezza
            if not al_suolo:
                screen.blit(imgPers8Jump, player_rect) #Se salta --> imgPerJump
            elif is_crouching:
                screen.blit(imgPers8Crouch, player_rect) #Se striscia --> imgPerCrouch
            else:
                screen.blit(imgPers8, player_rect) #Se torna in piedi --> imgPer

            #Movimento nemici
            sedia_rect.x -= sedia_speed
            banco_rect.x -= banco_speed

            #Oscillazione sedia
            oscillazione_sedia += direzione_sedia * 2
            if oscillazione_sedia > 80 or oscillazione_sedia < -80:
                direzione_sedia *= -1
            sedia_rect.bottom = ground_y + oscillazione_sedia

            #Oscillazione banco
            oscillazione_banco += direzione_banco * 2
            if oscillazione_banco > 80 or oscillazione_banco < -80:
                direzione_banco *= -1
            banco_rect.bottom = ground_y + oscillazione_banco
            
            #Movimento sedia e banco (insieme)
            if not campanella_attiva:
                sedia_rect.x -= sedia_speed - 15
                banco_rect.x -= banco_speed  - 15 
                #Se escono dallo schermo, ricompaiono a destra
                if sedia_rect.right < 0 and banco_rect.right < 0:
                    sedia_rect.left = SCREEN_WIDTH
                    banco_rect.left = SCREEN_WIDTH + 1000  #Distanza tra sedia e banco
                    sedia_passata = False
                    banco_passato = False

            #Disegno nemici
            screen.blit(imgSedia, sedia_rect)
            screen.blit(imgBanco, banco_rect)

            #Hitbox --> Riduce area del giocatore, dei nemici e della campanella
            sedia_hitbox = sedia_rect.inflate(-100, -100)
            banco_hitbox = banco_rect.inflate(-50, -50)
            player_hitbox = player_rect.inflate(-100, -100)
            campanella_hitbox = campanella_rect.inflate(-100, -100)
            computer_hitbox = computer_rect.inflate(-20,-20)
            
            #Computer che cade e trema lo sfondo
            if computer_attivo:
                computer_vel += gravita_libro
                computer_rect.y += computer_vel
                screen.blit(imgComputer, computer_rect)
                #COmputer tocca il terreno
                if computer_rect.bottom >= ground_y:
                    computer_rect.bottom = ground_y
                    computer_vel = 0
                    shake_timer = 15   #Fa tremare lo schermo
                    computer_attivo = False

            else:
                #reset libro
                computer_rect.x = random.randint(600,1200)
                computer_rect.y = -100
                computer_vel = 0
                computer_attivo = True

            #Se il giocatore colpisce la sedia
            if player_hitbox.colliderect(sedia_hitbox):
                fineGioco = True #Perde
                punteggio = - 20 #Azzera punteggio
                suono_home.stop() #Ferma la musica che sta suonando
                pygame.mixer.music.load("suonoPerdita.mp3") #Carica il nuovo file musicale di sconfitta nel mixer di pygame
                pygame.mixer.music.set_volume(0.5) #Imposta il volume della canzone
                suono_fineGioco.play() #Riproduce il suono di sconfitta
            #Se il giocatore colpisce il banco
            if player_hitbox.colliderect(banco_hitbox) and not is_crouching:
                fineGioco = True #Perde
                punteggio = - 25 #Azzera punteggio
                suono_home.stop() #Ferma la musica che sta suonando
                pygame.mixer.music.load("suonoPerdita.mp3") #Carica il nuovo file musicale di sconfitta nel mixer di pygame
                pygame.mixer.music.set_volume(0.5) #Imposta il volume della canzone
                suono_fineGioco.play() #Riproduce il suono di sconfitta

            #Se il giocatore passa la sedia
            if sedia_rect.right < player_rect.left and not sedia_passata:
                punteggio += 20 #Aggiunge 20 punti
                sedia_passata = True
            #Se il giocatore passa il banco
            if banco_rect.right < player_rect.left and not banco_passato:
                punteggio += 25 #Aggiunge 25 punti
                banco_passato = True
                
            #Inserimento del testo del punteggio nella schermata di gioco (in alto a sinistra)
            testo_punti = font_punti.render("Punti: " + str(punteggio), True, "black")
            screen.blit(testo_punti,(50,50))
            
            # Raggiungimento 450 punti --> compare la campanella
            if punteggio >= 450:
                campanella_attiva = True
            if campanella_attiva:
                campanella_rect.x -= 10
                screen.blit(imgCampanella, campanella_rect)

            #Se il giocatore colpisce la campanella --> hai vinto
            if campanella_attiva and player_hitbox.colliderect(campanella_hitbox):
                vittoria = True   
            if vittoria:
                screen.blit(imgHaiVinto8,(0,0))
                suono_home.stop() #Ferma la musica che sta suonando
                pygame.mixer.music.load("suonoVittoria.mp3") #Carica il nuovo file musicale di vittoria nel mixer di pygame
                pygame.mixer.music.set_volume(0.5) #Imposta il volume della canzone
                suono_vittoria.play() #Riproduce il suono di vittoria

            if fineGioco:
                screen.blit(imgHaiPerso, (0,0))             

        pygame.display.flip() #Aggiorna il display
        clock.tick(60) #Limita il gioco a 60 FPS

    pygame.quit() #Chiude pygame
    
if __name__ == "__main__":
    main()
