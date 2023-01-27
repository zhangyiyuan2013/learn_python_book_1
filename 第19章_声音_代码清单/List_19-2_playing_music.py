import pygame,sys
pygame.init()

screen = pygame.display.set_mode([640,480])

# These are the two changed lines.
pygame.mixer.music.load("bg_music.mp3")
pygame.mixer.music.play()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
