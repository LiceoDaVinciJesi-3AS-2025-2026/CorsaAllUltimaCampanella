def main() -> None:
    print("Hello from corsaallultimacampanella!")
    
import pygame

pygame.init()

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1005

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("corsa all'ultima campanella!")

#bottone per comicnicare
buttonStart = pygame.Rect(SCREEN_WIDTH // 2.399, SCREEN_HEIGHT // 1.235, 280, 80)

#bottone per visualizzare i personaggi
buttonPersonaggi = pygame.Rect(SCREEN_WIDTH // 2.4, SCREEN_HEIGHT // 1.48, 280, 80)

imgSfondoPrincipale = pygame.image.load("pixelscuola.png") 
imgSfondoPrincipale = pygame.transform.scale(imgSfondoPrincipale,(SCREEN_WIDTH,SCREEN_HEIGHT))

imgSfondoPersonaggi = pygame.image.load("portapersonaggi.png")
imgSfondoPersonaggi = pygame.transform.scale(imgSfondoPersonaggi,(SCREEN_WIDTH,SCREEN_HEIGHT))

Normalfont = pygame.font.SysFont('Impact', 60)
parolaButtonStart = Normalfont.render("start", True, "black")
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
                if home and buttonStart.collidepoint(mPos):
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

        buttonColorS = "white"
        if buttonStart.collidepoint(mPos):
            buttonColorS = "dark grey"
        buttonS = pygame.draw.rect(screen,buttonColorS,buttonStart)
        screen.blit(parolaButtonStart, (SCREEN_WIDTH // 2.18, SCREEN_HEIGHT // 1.235))
        
        buttonColorP = "white"
        if buttonPersonaggi.collidepoint(mPos):
            buttonColorP = "dark grey"
        buttonP = pygame.draw.rect(screen,buttonColorP,buttonPersonaggi)
        screen.blit(parolaButtonPersonaggi, (SCREEN_WIDTH // 2.4, SCREEN_HEIGHT // 1.475))
        
    #se ci troviamo nel gioco
    elif personaggi:
        screen.blit(imgSfondoPersonaggi,(0,0) )
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                home = True 
    
    else:
        screen.fill("red")
        
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
