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

imgSfondo = pygame.image.load("pixelscuola.png") 
imgSfondo = pygame.transform.scale(imgSfondo,(SCREEN_WIDTH,SCREEN_HEIGHT))


Normalfont = pygame.font.SysFont('Impact', 60)
parolaButtonStart = Normalfont.render("start", True, "black")
parolaButtonPersonaggi = Normalfont.render("personaggi", True, "black")

running = True

while running:
    mPos = pygame.mouse.get_pos() 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if buttonStart.collidepoint(mPos):
                running = True
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if buttonPersonaggi.collidepoint(mPos):
                running = True
                
    screen.fill("green")
    screen.blit(imgSfondo,(0,0) )

    buttonColorS = "white"
    if buttonStart.collidepoint(mPos):
        buttonColorS = "grey"
    buttonS = pygame.draw.rect(screen,buttonColorS,buttonStart)
    screen.blit(parolaButtonStart, (SCREEN_WIDTH // 2.18, SCREEN_HEIGHT // 1.235))
    
    buttonColorP = "white"
    if buttonPersonaggi.collidepoint(mPos):
        buttonColorP = "grey"
    buttonP = pygame.draw.rect(screen,buttonColorP,buttonPersonaggi)
    screen.blit(parolaButtonPersonaggi, (SCREEN_WIDTH // 2.4, SCREEN_HEIGHT // 1.475))
    
    pygame.display.flip()


pygame.quit()
