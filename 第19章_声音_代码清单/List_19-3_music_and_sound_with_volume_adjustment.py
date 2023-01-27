import pygame,sys
pygame.init()
screen = pygame.display.set_mode([640,480])
pygame.mixer.music.load("bg_music.mp3")
pygame.mixer.music.set_volume(0.30) # Adjusts the volume of the musec
pygame.mixer.music.play()
splat = pygame.mixer.Sound("splat.wav")
splat.set_volume(0.50)  # Adjusts the volume of the sound effect
splat.play()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
                                        
