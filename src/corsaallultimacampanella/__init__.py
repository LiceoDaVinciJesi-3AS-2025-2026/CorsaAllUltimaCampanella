def main() -> None:
    print("Hello from corsaallultimacampanella!")
    
import pygame

pygame.init()

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 925

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("corsa all'ultima campanella!")

#bottone per comicnicare
buttonInfo = pygame.Rect(SCREEN_WIDTH // 2.45, SCREEN_HEIGHT // 1.235, 310, 80)

#bottone per visualizzare i personaggi
buttonPersonaggi = pygame.Rect(SCREEN_WIDTH // 2.4, SCREEN_HEIGHT // 1.48, 280, 80)

imgSfondoPrincipale = pygame.image.load("pixelscuola.png") 
imgSfondoPrincipale = pygame.transform.scale(imgSfondoPrincipale,(SCREEN_WIDTH,SCREEN_HEIGHT))

imgSfondoPersonaggi = pygame.image.load("sfondopersonaggi.png")
imgSfondoPersonaggi = pygame.transform.scale(imgSfondoPersonaggi,(SCREEN_WIDTH,SCREEN_HEIGHT))

imgItaliano = pygame.image.load("pixelita.png") 
imgItaliano = pygame.transform.scale(imgItaliano,(350,350))
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

Normalfont = pygame.font.SysFont('Impact', 60)
parolaButtonInfo = Normalfont.render("informazioni", True, "black")
parolaButtonPersonaggi = Normalfont.render("personaggi", True, "black")

clock = pygame.time.Clock()

running = True
home = True
personaggi = True 
gioco = True

while running:
    mPos = pygame.mouse.get_pos() 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: #click sinistro 
                if home and buttonInfo.collidepoint(mPos):
                    home = False
                    personaggi = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: #click sinistro 
                if personaggi and buttonPersonaggi.collidepoint(mPos):
                    home = False
                    gioco = False

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
        buttonColorP = "white"
        if buttonPersonaggi.collidepoint(mPos):
            buttonColorP = "dark grey"
        buttonP = pygame.draw.rect(screen,buttonColorP,buttonPersonaggi)
        screen.blit(parolaButtonPersonaggi, (SCREEN_WIDTH // 2.4, SCREEN_HEIGHT // 1.475))
        
    #se ci troviamo nel gioco
    elif personaggi:
        screen.blit(imgSfondoPersonaggi,(0,0))
        #inserisco immagine prof di italiano nella schermata dei personaggi
        screen.blit(imgItaliano, (48, 90))
        #inserisco immagine prof di storia e filosofia nella schermata dei personaggi
        screen.blit(imgStofilo, (420, 100))
        #inserisco immagine prof di arte nella schermata dei personaggi
        screen.blit(imgArte, (770, 80))
        #inserisco immagine prof di inglese nella schermata dei personaggi
        screen.blit(imgInglese, (1150, 80))
        #inserisco immagine prof di matematica nella schermata dei personaggi
        screen.blit(imgMatematica, (48, 515))
        #inserisco immagine prof di fisica nella schermata dei personaggi
        screen.blit(imgFisica, (420, 510))
        #inserisco immagine prof di scienze nella schermata dei personaggi
        screen.blit(imgScienze, (770, 490))
        #inserisco immagine prof di informatica nella schermata dei personaggi
        screen.blit(imgInformatica, (1150, 530))
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                home = True 
    
    else:
        screen.fill("red")
        
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

