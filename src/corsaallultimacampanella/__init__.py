def main() -> None:
    print("Hello from corsaallultimacampanella!")

import pygame

pygame.init()

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1005

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("corsa all'ultima campanella!")
buttonRect = pygame.Rect(SCREEN_WIDTH // 2.399, SCREEN_HEIGHT // 1.48, 280, 80)

imgSfondo = pygame.image.load("pixelscuola.png") 
imgSfondo = pygame.transform.scale(imgSfondo,(SCREEN_WIDTH,SCREEN_HEIGHT))


Normalfont = pygame.font.SysFont('Impact', 70)
close_tip = Normalfont.render("start", True, "black")

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
            if buttonRect.collidepoint(mPos):
                running = False
                
    screen.fill("green")
    screen.blit(imgSfondo,(0,0) )

    buttonColor = "white"
    if buttonRect.collidepoint(mPos):
        buttonColor = "yellow"
    button = pygame.draw.rect(screen,buttonColor,buttonRect)
    
    screen.blit(close_tip, (SCREEN_WIDTH // 2.22, SCREEN_HEIGHT // 1.5))
    pygame.display.flip()

# Chiude pygame
pygame.quit()
