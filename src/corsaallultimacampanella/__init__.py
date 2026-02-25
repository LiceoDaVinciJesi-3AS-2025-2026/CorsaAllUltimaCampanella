def main() -> None:
    print("Hello from corsaallultimacampanella!")
    
import pygame

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
imgGinnastica = pygame.transform.scale(imgGinnastica,(350,350))
imgStofilo = pygame.image.load("pixelstofilo.png") 
imgStofilo = pygame.transform.scale(imgStofilo,(350,350))
imgArte = pygame.image.load("pixelarte.png") 
imgArte = pygame.transform.scale(imgArte,(380,380))
imgInglese = pygame.image.load("pixeling.png") 
imgInglese = pygame.transform.scale(imgInglese,(370,370))
imgMatematica = pygame.image.load("pixelmate.png") 
imgMatematica = pygame.transform.scale(imgMatematica,(350,350))
imgFisica = pygame.image.load("pixelfisica.png") 
imgFisica = pygame.transform.scale(imgFisica,(350,350))
imgScienze = pygame.image.load("pixelscienze.png") 
imgScienze = pygame.transform.scale(imgScienze,(380,380))
imgInformatica = pygame.image.load("pixelinfo.png") 
imgInformatica = pygame.transform.scale(imgInformatica,(350,350))

#sfondo dei livelli
imgLivello = pygame.image.load("sfondoLivello.png") 
imgLivello = pygame.transform.scale(imgLivello, (SCREEN_WIDTH, SCREEN_HEIGHT))

#font delle parole nei bottoni e parole 
Normalfont = pygame.font.SysFont('Impact', 60)
parolaButtonInfo = Normalfont.render("informazioni", True, "black")
parolaButtonStart = Normalfont.render("start", True, "black")

# Dati dei giocatori
player_rect = pygame.Rect(100, 0, 470, 470)
vel_y = 0 #velocità iniziale
gravita = 0.8
salto = -22
al_suolo = True
is_crouching = False
altezza_normale = 470
altezza_crouch = 350
ground_y = 800  # altezza del pavimento nel livello
larghezza_player = 470
# Player Rect
player_rect = pygame.Rect(100, 0, larghezza_player, altezza_normale)
player_rect.bottom = ground_y

#immagini giocatori
imgPers1 = pygame.image.load("pixelginnastica.png").convert_alpha()
imgPers1 = pygame.transform.scale(imgPers1, (larghezza_player, altezza_normale))
imgPers1Crouch = pygame.image.load("ginnasticasdraiato.png").convert_alpha()
imgPers1Crouch = pygame.transform.scale(imgPers1Crouch, (larghezza_player, altezza_crouch))
imgPers1Jump = pygame.image.load("ginnasticasalto.png").convert_alpha()
imgPers1Jump = pygame.transform.scale(imgPers1Jump, (larghezza_player, altezza_normale))

imgPers2 = pygame.image.load("pixelstofilo.png").convert_alpha()
imgPers2 = pygame.transform.scale(imgPers2, (larghezza_player, altezza_normale))
imgPers2Crouch = pygame.image.load("stofilosdraiato.png").convert_alpha()
imgPers2Crouch = pygame.transform.scale(imgPers2Crouch, (larghezza_player, altezza_crouch + 60))

imgPers3 = pygame.image.load("pixelarte.png").convert_alpha()
imgPers3 = pygame.transform.scale(imgPers3, (larghezza_player, altezza_normale))
imgPers3Crouch = pygame.image.load("artesdraiato.png").convert_alpha()
imgPers3Crouch = pygame.transform.scale(imgPers3Crouch, (larghezza_player, altezza_crouch +50))

imgPers4 = pygame.image.load("pixeling.png").convert_alpha()
imgPers4 = pygame.transform.scale(imgPers4, (larghezza_player, altezza_normale))
imgPers4Crouch = pygame.image.load("inglesesdraiato.png").convert_alpha()
imgPers4Crouch = pygame.transform.scale(imgPers4Crouch, (larghezza_player, altezza_crouch + 30))

imgPers5 = pygame.image.load("pixelmate.png").convert_alpha()
imgPers5 = pygame.transform.scale(imgPers5, (larghezza_player, altezza_normale))
imgPers5Crouch = pygame.image.load("ginnasticasdraiato.png").convert_alpha()
imgPers5Crouch = pygame.transform.scale(imgPers5Crouch, (larghezza_player, altezza_crouch))

imgPers6 = pygame.image.load("pixelfisica.png").convert_alpha()
imgPers6 = pygame.transform.scale(imgPers6, (larghezza_player, altezza_normale))
imgPers6Crouch = pygame.image.load("ginnasticasdraiato.png").convert_alpha()
imgPers6Crouch = pygame.transform.scale(imgPers6Crouch, (larghezza_player, altezza_crouch))

imgPers7 = pygame.image.load("pixelscienze.png").convert_alpha()
imgPers7 = pygame.transform.scale(imgPers7, (larghezza_player, altezza_normale))
imgPers7Crouch = pygame.image.load("ginnasticasdraiato.png").convert_alpha()
imgPers7Crouch = pygame.transform.scale(imgPers7Crouch, (larghezza_player, altezza_crouch))

imgPers8 = pygame.image.load("pixelinfo.png").convert_alpha()
imgPers8 = pygame.transform.scale(imgPers8, (larghezza_player, altezza_normale))
imgPers8Crouch = pygame.image.load("ginnasticasdraiato.png").convert_alpha()
imgPers8Crouch = pygame.transform.scale(imgPers8Crouch, (larghezza_player, altezza_crouch))

clock = pygame.time.Clock()

running = True
home = True
informazioni = False
personaggi = False 
gioco = False 
Livello1 = False 
Livello2 = False 
Livello3 = False 
Livello4 = False 
Livello5 = False 
Livello6 = False 
Livello7 = False 
Livello8 = False 

while running:
    mPos = pygame.mouse.get_pos() 
    keys = pygame.key.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                            
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
                    home = False
                   
                elif personaggi and buttonStoFilo.collidepoint(mPos):
                    personaggi = False
                    Livello2 = True
                    home = False
                    screen.blit(imgLivello, (0, 0))
                    
                elif personaggi and buttonArte.collidepoint(mPos):
                    personaggi = False
                    Livello3 = True
                    home = False
                    screen.blit(imgLivello, (0, 0))
                    
                elif personaggi and buttonInglese.collidepoint(mPos):
                    personaggi = False
                    Livello4 = True
                    home = False
                    screen.blit(imgLivello, (0, 0))
                
                elif personaggi and buttonMatematica.collidepoint(mPos):
                    personaggi = False
                    Livello5 = True
                    home = False
                    screen.blit(imgLivello, (0, 0))
                 
                elif personaggi and buttonFisica.collidepoint(mPos):
                    personaggi = False
                    Livello6 = True
                    home = False
                    screen.blit(imgLivello, (0, 0))
                
                elif personaggi and buttonScienze.collidepoint(mPos):
                    personaggi = False
                    Livello7 = True
                    home = False
                    screen.blit(imgLivello, (0, 0))
                    
                elif personaggi and buttonInformatica.collidepoint(mPos):
                    personaggi = False
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
        screen.blit(imgGinnastica, (48, 90))
        buttonGinnastica = pygame.Rect(SCREEN_WIDTH // 14.4, SCREEN_HEIGHT // 2.25, 230, 60)
        parolaButtonGinn = Normalfont.render("Livello 1", True, "black")
        
        buttonColorG = "white"
        if buttonGinnastica.collidepoint(mPos):
            buttonColorG = "dark grey"
        buttonG = pygame.draw.rect(screen,buttonColorG,buttonGinnastica)
        screen.blit(parolaButtonGinn, (SCREEN_WIDTH // 12.5, SCREEN_HEIGHT // 2.3))
        
        #inserisco immagine prof di storia e filosofia e bottone livello 2 nella schermata dei personaggi
        screen.blit(imgStofilo, (420, 100))
        buttonStoFilo = pygame.Rect(SCREEN_WIDTH // 3.37, SCREEN_HEIGHT // 2.25, 230, 60)
        parolaButtonStoFilo = Normalfont.render("Livello 2", True, "black")
        
        buttonColorStoFilo = "white"
        if buttonStoFilo.collidepoint(mPos):
            buttonColorStoFilo = "dark grey"
        buttonSF = pygame.draw.rect(screen,buttonColorStoFilo,buttonStoFilo)
        screen.blit(parolaButtonStoFilo, (SCREEN_WIDTH // 3.27, SCREEN_HEIGHT // 2.3))
        
        #inserisco immagine prof di arte e bottone livello 3 nella schermata dei personaggi
        screen.blit(imgArte, (770, 80))
        buttonArte = pygame.Rect(SCREEN_WIDTH // 1.89, SCREEN_HEIGHT // 2.25, 230, 60)
        parolaButtonArte = Normalfont.render("Livello 3", True, "black")
        
        buttonColorArte = "white"
        if buttonArte.collidepoint(mPos):
            buttonColorArte = "dark grey"
        buttonArte = pygame.draw.rect(screen,buttonColorArte,buttonArte)
        screen.blit(parolaButtonArte, (SCREEN_WIDTH // 1.85, SCREEN_HEIGHT // 2.3))
        
        #inserisco immagine prof di inglese e bottone livello 4 nella schermata dei personaggi
        screen.blit(imgInglese, (1150, 80))
        buttonInglese = pygame.Rect(SCREEN_WIDTH // 1.32, SCREEN_HEIGHT // 2.25, 230, 60)
        parolaButtonInglese = Normalfont.render("Livello 4", True, "black")
        
        buttonColorInglese = "white"
        if buttonInglese.collidepoint(mPos):
            buttonColorInglese = "dark grey"
        buttonInglese = pygame.draw.rect(screen,buttonColorInglese,buttonInglese)
        screen.blit(parolaButtonInglese, (SCREEN_WIDTH // 1.3, SCREEN_HEIGHT // 2.3))
        
        #inserisco immagine prof di matematica e bottone livello 5 nella schermata dei personaggi
        screen.blit(imgMatematica, (48, 515))
        buttonMatematica = pygame.Rect(SCREEN_WIDTH // 14.4, SCREEN_HEIGHT // 1.14, 230, 60)
        parolaButtonMatematica = Normalfont.render("Livello 5", True, "black")
        
        buttonColorMatematica = "white"
        if buttonMatematica.collidepoint(mPos):
            buttonColorMatematica = "dark grey"
        buttonMatematica = pygame.draw.rect(screen,buttonColorMatematica,buttonMatematica)
        screen.blit(parolaButtonMatematica, (SCREEN_WIDTH // 12.5, SCREEN_HEIGHT // 1.15))
        
        #inserisco immagine prof di fisica e bottone livello 6 nella schermata dei personaggi
        screen.blit(imgFisica, (420, 510))
        buttonFisica = pygame.Rect(SCREEN_WIDTH // 3.37, SCREEN_HEIGHT // 1.13, 230, 60)
        parolaButtonFisica = Normalfont.render("Livello 6", True, "black")
        
        buttonColorFisica = "white"
        if buttonFisica.collidepoint(mPos):
            buttonColorFisica = "dark grey"
        buttonFisica = pygame.draw.rect(screen,buttonColorFisica,buttonFisica)
        screen.blit(parolaButtonFisica, (SCREEN_WIDTH // 3.27, SCREEN_HEIGHT // 1.14))
        
        #inserisco immagine prof di scienze e bottone livello 7 nella schermata dei personaggi
        screen.blit(imgScienze, (770, 490))
        buttonScienze = pygame.Rect(SCREEN_WIDTH // 1.89, SCREEN_HEIGHT // 1.14, 230, 60)
        parolaButtonScienze = Normalfont.render("Livello 7", True, "black")
        
        buttonColorScienze = "white"
        if buttonScienze.collidepoint(mPos):
            buttonColorScienze = "dark grey"
        buttonScienze = pygame.draw.rect(screen,buttonColorScienze,buttonScienze)
        screen.blit(parolaButtonScienze, (SCREEN_WIDTH // 1.85, SCREEN_HEIGHT // 1.15))
        
        #inserisco immagine prof di informatica e bottone livello 8 nella schermata dei personaggi
        screen.blit(imgInformatica, (1150, 530))
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
        screen.fill("red")

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                home = True
                personaggi = True
                
    elif Livello1:
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
            screen.blit(imgPers1Jump, player_rect)
        elif is_crouching:
            screen.blit(imgPers1Crouch, player_rect)
        else:
            screen.blit(imgPers1, player_rect)
            
    elif Livello2:
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
        
    elif Livello3:
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
            screen.blit(imgPers3Crouch, player_rect)
        else:
            screen.blit(imgPers3, player_rect)
            
    elif Livello4:
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
            screen.blit(imgPers4Crouch, player_rect)
        else:
            screen.blit(imgPers4, player_rect)
            
    elif Livello5:
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
            screen.blit(imgPers5Crouch, player_rect)
        else:
            screen.blit(imgPers5, player_rect)
    
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
            screen.blit(imgPers6Crouch, player_rect)
        else:
            screen.blit(imgPers6, player_rect)
            
    elif Livello7:
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
            screen.blit(imgPers7Crouch, player_rect)
        else:
            screen.blit(imgPers7, player_rect)
            
    elif Livello8:
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
            screen.blit(imgPers8Crouch, player_rect)
        else:
            screen.blit(imgPers8, player_rect)
               

    pygame.display.flip()
    clock.tick(60)

pygame.quit()



